'''
This script creates the data mart for pair angles data in weekly report
## Steps
* read data from excel files
* transform it to fit the local raw data table and push into it
'''
import argparse
import datetime as dt
from src.config.appConfig import getConfig
from src.rawDataCreators.daywisePairAnglDataCreator import createPairAnglesRawData

# get start and end dates from command line
endDate = dt.datetime.now() - dt.timedelta(days=1)
startDate = endDate - dt.timedelta(days=3)
# get an instance of argument parser from argparse module
parser = argparse.ArgumentParser()
# setup firstname, lastname arguements
parser.add_argument('--start_date', help="Enter Start date in yyyy-mm-dd format",
                    default=dt.datetime.strftime(startDate, '%Y-%m-%d'))
parser.add_argument('--end_date', help="Enter last date in yyyy-mm-dd format",
                    default=dt.datetime.strftime(endDate, '%Y-%m-%d'))
# get the dictionary of command line inputs entered by the user
args = parser.parse_args()
# access each command line input from the dictionary
startDate = dt.datetime.strptime(args.start_date, '%Y-%m-%d')
endDate = dt.datetime.strptime(args.end_date, '%Y-%m-%d')

startDate = startDate.replace(hour=0, minute=0, second=0, microsecond=0)
endDate = endDate.replace(hour=0, minute=0, second=0, microsecond=0)
print('startDate = {0}, endDate = {1}'.format(dt.datetime.strftime(
    startDate, '%Y-%m-%d'), dt.datetime.strftime(endDate, '%Y-%m-%d')))

# get application config
appConfig = getConfig()

# create outages raw data between start and end dates
anglFolderPath = appConfig['anglFolderPath']
appDbConnStr = appConfig['appDbConStr']

isRawCreationSuccess = createPairAnglesRawData(
    appDbConnStr, anglFolderPath, startDate, endDate)

if isRawCreationSuccess:
    print('pair angles raw data creation done')
else:
    print('pair angles raw data creation failure')
