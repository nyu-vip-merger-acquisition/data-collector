
import os

FINANCE_API_KEY = os.getenv('FINANCIALMODELINGPREP_API_KEY')
RAW_FILE_DATA_PATH = "./data/raw_files/"


# 600 Requests per Minute
ONE_MINUTE = 60
MAX_CALLS_PER_MINUTE = 600