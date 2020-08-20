import unittest
from src.fetchers.dayAngleSummaryFetcher import fetchAngleSummaryForDate
import datetime as dt
from src.config.appConfig import getConfig


class TestFetchAnglesData(unittest.TestCase):
    appConfig = None

    def setUp(self):
        self.appConfig = getConfig()

    def test_run(self) -> None:
        """tests the function that fetches the ouatges from reporting software
        """
        targetDt = dt.datetime(2020, 8, 9)
        anglFolderPath = self.appConfig['anglFolderPath']
        anglRecords = fetchAngleSummaryForDate(anglFolderPath, targetDt)
        targetColumns = ['pairName', 'angularLim', 'violPerc', 'maxDeg',
                         'minDeg']
        self.assertFalse(len(anglRecords) == 0)
        self.assertFalse(False in [(col in anglRecords[0])
                                   for col in targetColumns])
