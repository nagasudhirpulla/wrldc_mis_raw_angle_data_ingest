import pandas as pd
from src.typeDefs.appConfig import IAppConfig


def getConfig(configFilename='config.xlsx') -> IAppConfig:
    """
    Get the application config from config.xlsx file
    Returns:
        IAppConfig: The application configuration as a dictionary
    """

    df = pd.read_excel(configFilename, header=None, index_col=0)
    configDict = df[1].to_dict()
    return configDict
