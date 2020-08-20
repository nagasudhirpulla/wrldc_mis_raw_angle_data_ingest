from typing import List, Tuple, TypedDict
import cx_Oracle
from src.typeDefs.pairAngleSummary import IPairAngleSummary


class Outages(TypedDict):
    columns: List[str]
    rows: List[Tuple]


class DailyPairAnglesDataRepo():
    """Repository class for daywise angle summary data of substation pairs
    """
    localConStr: str = ""

    def __init__(self, dbConStr: str) -> None:
        """constructor method
        Args:
            dbConf (DbConfig): database connection string
        """
        self.localConStr = dbConStr

    def insertPairAnglesData(self, angleDataRecords: List[IPairAngleSummary]) -> bool:
        """inserts angles date of station pairs into the app db
        Args:
            angleDataRecords (List[IPairAngleSummary]): daywise angle data to be inserted
        Returns:
            bool: returns true if process is ok
        """
        # get connection with raw data table
        conLocal = cx_Oracle.connect(self.localConStr)

        isInsertSuccess = True
        if len(angleDataRecords) == 0:
            return isInsertSuccess
        try:
            # keyNames names of the raw data
            keyNames = ['pairName', 'angularLim', 'violPerc', 'maxDeg',
                        'minDeg', 'dataDate', 'dataType']
            colNames = ['ANGLE_PAIR', 'ANGULAR_LIMIT', 'VIOL_PERC', 'MAX_VIOL',
                        'MIN_VIOL', 'DATA_DATE', 'DATA_TYPE']
            # get cursor for raw data table
            curLocal = conLocal.cursor()

            # text for sql place holders
            sqlPlceHldrsTxt = ','.join([':{0}'.format(x+1)
                                        for x in range(len(keyNames))])

            # delete the rows which are already present
            existingAnglePairs = [(x['dataDate'], x['pairName'])
                                  for x in angleDataRecords]
            curLocal.executemany(
                "delete from mis_warehouse.daily_angles_data where DATA_DATE=:1 and ANGLE_PAIR=:2", existingAnglePairs)

            # insert the raw data
            anglesDataInsSql = 'insert into mis_warehouse.daily_angles_data({0}) values ({1})'.format(
                ','.join(colNames), sqlPlceHldrsTxt)

            curLocal.executemany(anglesDataInsSql, [tuple(
                [r[col] for col in keyNames]) for r in angleDataRecords])

            # commit the changes
            conLocal.commit()
        except Exception as e:
            isInsertSuccess = False
            print('Error while bulk insertion of daily angles data into raw data db')
            print(e)
        finally:
            # closing database cursor and connection
            if curLocal is not None:
                curLocal.close()
            conLocal.close()
        return isInsertSuccess
