import unittest
from src.rawDataCreators.daywisePairAnglDataCreator import createPairAnglesRawData
import datetime as dt
from src.config.appConfig import getConfig


class TestDaywisePairAnglRawDataCreator(unittest.TestCase):
    def setUp(self):
        self.appConfig = getConfig()

    def test_run(self) -> None:
        """tests the function that fetches the ouatges from reporting software
        """
        startDt = dt.datetime(2020, 8, 5)
        endDt = dt.datetime(2020, 8, 19)
        anglFolderPath = self.appConfig['anglFolderPath']
        appDbConnStr = self.appConfig['appDbConStr']
        isRawCreationSuccess = createPairAnglesRawData(
            appDbConnStr, anglFolderPath, startDt, endDt)
        self.assertTrue(isRawCreationSuccess)
