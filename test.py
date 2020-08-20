# %%
from src.fetchers.dayAngleSummaryFetcher import fetchAngleSummaryForDate
from src.config.appConfig import getConfig
import datetime as dt

# %%
appConf = getConfig()

# %%
targetDt = dt.datetime(2020, 8, 9)

data = fetchAngleSummaryForDate(appConf['anglFolderPath'], targetDt)

# %%

