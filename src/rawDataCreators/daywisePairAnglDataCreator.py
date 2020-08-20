from src.fetchers.dayAngleSummaryFetcher import fetchAngleSummaryForDate
import datetime as dt
import cx_Oracle
from typing import List
from src.repos.dailyPairAnglDataRepo import DailyPairAnglesDataRepo


def createPairAnglesRawData(appDbConStr: str, anglFolderPath: str, startDate: dt.datetime, endDate: dt.datetime) -> bool:
    """fetches the angle pairs data from excel files 
    and pushes it to the raw data table
    Args:
        appDbConStr (str): application db connection string
        anglFolderPath (str): folder path of angles data excel files
        startDate (dt.datetime): start date
        endDate (dt.datetime): end date
    Returns:
        [bool]: returns True if succeded
    """
    isRawDataInsSuccess = False

    reqStartDt = startDate.date()
    reqEndDt = endDate.date()

    if reqEndDt < reqStartDt:
        return False

    # get the instance of outages repository
    anglesDatRepo = DailyPairAnglesDataRepo(appDbConStr)
    currDate = reqStartDt

    while currDate <= reqEndDt:
        # fetch angles data
        dayAnglesData = fetchAngleSummaryForDate(anglFolderPath, currDate)

        # insert outages into db via the repository instance
        isRawDataInsSuccess = anglesDatRepo.insertPairAnglesData(dayAnglesData)

        # update currDate
        currDate += dt.timedelta(days=1)

    return isRawDataInsSuccess
