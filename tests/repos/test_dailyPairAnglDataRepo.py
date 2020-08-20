import unittest
from src.repos.dailyPairAnglDataRepo import DailyPairAnglesDataRepo
import datetime as dt
from typing import List
from src.typeDefs.pairAngleSummary import IPairAngleSummary
from src.config.appConfig import getConfig


class TestDailyPairAnglDataRepo(unittest.TestCase):
    appConfig = None

    def setUp(self):
        self.appConfig = getConfig()

    def test_run(self) -> None:
        """tests the function that fetches the ouatges from reporting software
        """
        appDbConnStr = self.appConfig['appDbConStr']
        anglDataRepo = DailyPairAnglesDataRepo(appDbConnStr)
        testData: List[IPairAngleSummary] = [{
            'pairName': 'test',
            'dataDate': dt.datetime(1990, 1, 1),
            'angularLim': 0,
            'violPerc': 0,
            'maxDeg': -1,
            'minDeg': -1,
            'dataType': 'test'
        }]
        isInsertionSuccess = anglDataRepo.insertPairAnglesData(testData)
        self.assertTrue(isInsertionSuccess)
