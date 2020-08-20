import datetime as dt
from src.typeDefs.pairAngleSummary import IPairAngleSummary
from typing import List
import os
import pandas as pd


def fetchAngleSummaryForDate(anglFolderPath: str, targetDt: dt.datetime) -> List[IPairAngleSummary]:
    """fetched angle summary data rows for a date from excel file

    Args:
        targetDt (dt.datetime): date for which data is to be extracted

    Returns:
        List[IPairAngleSummary]: list of angles records fetched from the excel data
    """
    # sample excel filename - ANGLES__05_08_2020.xlsx
    fileDateStr = dt.datetime.strftime(targetDt, '%d_%m_%Y')
    targetFilename = 'ANGLES__{0}.xlsx'.format(fileDateStr)
    targetFilePath = os.path.join(anglFolderPath, targetFilename)

    # check if excel file is present
    if not os.path.isfile(targetFilePath):
        return []

    # read excel sheet named final
    excelDf = pd.read_excel(targetFilePath, 'Final', skiprows=6, skipfooter=1)
    
    # remove 1st column from df
    excelDf = excelDf.iloc[:, 1:]

    firstTableEndInd = 0
    secondTableStartInd = 0

    # find the index at which Sr.No is Nan
    for rIter in range(excelDf.shape[0]):
        serialNumVal = excelDf[excelDf.columns[0]].iloc[rIter]
        if pd.isna(serialNumVal):
            firstTableEndInd = rIter-1
            break

    wideAnglDf = excelDf.iloc[0:firstTableEndInd+1, :]
    wideAnglDf = wideAnglDf.iloc[:, 1:]
    wideAnglDf['dataDate'] = targetDt
    wideAnglDf['dataType'] = 'wide'

    # find the start of second table
    for rIter in range(firstTableEndInd, excelDf.shape[0]):
        serialNumVal = excelDf[excelDf.columns[0]].iloc[rIter]
        if serialNumVal == 1:
            secondTableStartInd = rIter
            break

    adjAnglDf = excelDf.iloc[secondTableStartInd:, :]
    adjAnglDf = adjAnglDf.iloc[:, 1:]
    adjAnglDf['dataDate'] = targetDt
    adjAnglDf['dataType'] = 'adj'

    # append wide and adj dataframes
    resDf = wideAnglDf.append(adjAnglDf)

    # rename columns to suite output requirements
    resDf.rename(columns={
        "Wide Angle pair": "pairName",
        "Angular limit": "angularLim",
        "% violation": 'violPerc',
        'max (degrees)': 'maxDeg',
        'min (degrees)': 'minDeg'
    }, inplace=True)

    # convert nan to None
    resDf = resDf.where(pd.notnull(resDf), None)

    # convert dataframe to list of dictionaries
    resRecords = resDf.to_dict('records')
    return resRecords
