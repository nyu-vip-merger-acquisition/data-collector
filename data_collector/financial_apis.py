import requests
import orjson

from config import FINANCE_API_KEY
from utils import throttled_api_request

def get_eligible_entities():
    uri = "https://financialmodelingprep.com/api/v3/stock/list"
    raw_response = requests.get(uri,params={'apikey':FINANCE_API_KEY})
    return [data['symbol'] for data in orjson.loads(raw_response.text) if data['type']=='stock']

def get_company_info(symbol):
    '''
    Refer to the API page for details: https://site.financialmodelingprep.com/developer/docs/company-outlook-api
    '''
    uri = "https://financialmodelingprep.com/api/v4/company-outlook"
    response = throttled_api_request(uri,params={'symbol':symbol,'apikey':FINANCE_API_KEY})
    return response.get("profile")

def get_company_financial(symbol,type):
    '''
    Refer to the API page for details: https://site.financialmodelingprep.com/developer/docs/financial-statement-free-api/
    and https://site.financialmodelingprep.com/developer/docs/financial-statement-as-reported-api/ 
    '''
    if type=="income_statement":
        uri = "https://financialmodelingprep.com/api/v3/income-statement/{}".format(symbol)
    elif type=="reported_financial_statement":
        uri = "https://financialmodelingprep.com/api/v3/financial-statement-full-as-reported/{}".format(symbol)
    elif type=="balance_sheet_statement":
        uri = "https://financialmodelingprep.com/api/v3/balance-sheet-statement/{}".format(symbol)
    elif type=="cash_flow_statement":
        uri = "https://financialmodelingprep.com/api/v3/cash-flow-statement/{}".format(symbol)

    limit = 120
    return throttled_api_request(uri,params={'limit':limit,'period':'annual','apikey':FINANCE_API_KEY})

def get_company_financial_ratios(symbol):
    '''
    Refer to the API page for details: https://site.financialmodelingprep.com/developer/docs/financial-ratio-free-api/
    '''
    limit = 120
    uri = "https://financialmodelingprep.com/api/v3/ratios/{}".format(symbol)
    return throttled_api_request(uri,params={'limit':limit,'period':'annual','apikey':FINANCE_API_KEY})

def get_key_metrics(symbol):
    '''
    Refer to the API page for details: https://site.financialmodelingprep.com/developer/docs/company-key-metrics-api/
    period: quarter|annual
    '''
    limit = 120
    uri = "https://financialmodelingprep.com/api/v3/key-metrics/{}".format(symbol)
    return throttled_api_request(uri,params={'period':'annual','limit':limit,'apikey':FINANCE_API_KEY})

def get_company_enterprise_value(symbol):
    '''
    Refer to the API page for details: https://site.financialmodelingprep.com/developer/docs/company-enterprise-value-api/
    '''
    limit = 120
    uri = "https://financialmodelingprep.com/api/v3/enterprise-values/{}".format(symbol)
    return throttled_api_request(uri,params={'period':'annual','limit':limit,'apikey':FINANCE_API_KEY})

def get_financial_growth(symbol):
    limit = 120
    uri = "https://financialmodelingprep.com/api/v3/financial-growth/{}".format(symbol)
    return throttled_api_request(uri,params={'period':'annual','limit':limit,'apikey':FINANCE_API_KEY})

############TODO

def get_institutional_stock_ownership(symbol):
    '''
    Refer to the API page for details: 
    '''
    uri = "https://financialmodelingprep.com/api/v4/institutional-ownership/symbol-ownership"
    response = requests.get(uri,params={'symbol':symbol,'includeCurrentQuarter':'false','apikey':FINANCE_API_KEY})
    return response

def get_sectors_pe():
    '''
    Refer to the API page for details: 
    '''
    uri = "https://financialmodelingprep.com/api/v4/sector_price_earning_ratio?date=2021-05-07&exchange=NYSE&apikey={}"
    response = requests.get(uri,params={'date':'','exchange':'','apikey':FINANCE_API_KEY})

def get_industry_pe():
    pass

def get_stock_peers(symbol):
    '''
    Refer to the API page for details: 
    '''
    uri = "https://financialmodelingprep.com/api/v4/stock_peers"
    response = requests.get(uri,params={'symbol':symbol,'apikey':FINANCE_API_KEY})
    return response

def get_current_stock_financial_scores(symbol):
    '''
    Refer to the API page for details: https://site.financialmodelingprep.com/developer/docs/stock-financial-scores/
    '''
    uri = "https://financialmodelingprep.com/api/v4/score"
    response = requests.get(uri,params={'symbol':symbol,'apikey':FINANCE_API_KEY})
    return response

def get_MnA_data():
    flag = True
    page = 0
    while flag==True:
        uri = "https://financialmodelingprep.com/api/v4/mergers-acquisitions-rss-feed"
        raw_response = requests.get(uri,params={'page':page,'apikey':FINANCE_API_KEY})
        response = raw_response.json()
        if len(response)<1:
            flag = False
        page+=1
    return response

