'''
This is the web server that acts as a service that creates raw pair angle separations data
'''
import datetime as dt
from src.config.appConfig import getConfig
from src.rawDataCreators.daywisePairAnglDataCreator import createPairAnglesRawData
from flask import Flask, request, jsonify
from src.typeDefs.appConfig import IAppConfig

app = Flask(__name__)

# get application config
appConfig: IAppConfig = getConfig()

# Set the secret key to some random bytes
app.secret_key = appConfig['flaskSecret']
appDbConnStr = appConfig['appDbConStr']
anglFolderPath = appConfig['anglFolderPath']


@app.route('/')
def hello():
    return "This is the web server that acts as a service that creates raw pair angle separations data"


@app.route('/raw_pair_angles', methods=['POST'])
def createRawPairAngles():
    # get start and end dates from post request body
    reqData = request.get_json()
    try:
        startDate = dt.datetime.strptime(reqData['startDate'], '%Y-%m-%d')
        endDate = dt.datetime.strptime(reqData['endDate'], '%Y-%m-%d')
    except Exception as ex:
        return jsonify({'message': 'Unable to parse start and end dates of this request body'}), 400
    # create outages raw pair angles between start and end dates
    isRawDataCreationSuccess = createPairAnglesRawData(appDbConnStr, anglFolderPath,
                                                       startDate, endDate)
    if isRawDataCreationSuccess:
        return jsonify({'message': 'raw pair angles data creation successful!!!', 'startDate': startDate, 'endDate': endDate})
    else:
        return jsonify({'message': 'raw pair angles data creation was not success'}), 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(appConfig['flaskPort']), debug=True)
