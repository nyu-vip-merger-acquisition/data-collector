import requests
import json

API_KEYS = "dca8f57d95497ddf6eba505230eb3953"
payload = {
    'apikey':API_KEYS
}
APIS = {
    "income_statement":('https://financialmodelingprep.com/api/v3/income-statement/{}',{'limit'}),
    "reported_income_statement":('https://financialmodelingprep.com/api/v3/income-statement-as-reported/{}',{}),
    "balance_sheet":('https://financialmodelingprep.com/api/v3/balance-sheet-statement/{}',{}),
    "cash_flow":('https://financialmodelingprep.com/api/v3/cash-flow-statement/{}',{}),
    "revenue_by_region":("https://financialmodelingprep.com/api/v4/revenue-geographic-segmentation?symbol={}&structure=flat",{}),
    "full_financial_statement":('https://financialmodelingprep.com/api/v3/financial-statement-full-as-reported/{}',{}),
    "ratios_ttm":('https://financialmodelingprep.com/api/v3/ratios-ttm/{}',{}),
    "annual_enterprise_value":('https://financialmodelingprep.com/api/v3/enterprise-values/{}',{}),
    "annual_key_metrics":('https://financialmodelingprep.com/api/v3/key-metrics/{}',{}),
    "financial_growth":('https://financialmodelingprep.com/api/v3/financial-growth/{}',{}),
    "institutional_ownership":('https://financialmodelingprep.com/api/v4/institutional-ownership/institutional-holders/symbol-ownership-percent?date=2021-09-30&symbol={}&page=0',{}),
    "profile":('https://financialmodelingprep.com/api/v3/profile/{}',{}),
    "market_cap":('https://financialmodelingprep.com/api/v3/market-capitalization/{}',{})
}


def get_data(url):
    raw_response = requests.get(url)
    data = json.loads(raw_response.text)
    print(data)

def get_available_entities():
    url = "https://financialmodelingprep.com/api/v3/financial-statement-symbol-lists?apikey=dca8f57d95497ddf6eba505230eb3953"
    raw_response = requests.get(url)
    data = raw_response.json()
    return data

def write_to_json_file(symbol,data_obj):
    # Serializing json
    json_object = json.dumps(data_obj, indent=4)
    # Writing to sample.json
    with open(symbol+".json", "w") as outfile:
        outfile.write(json_object)

if __name__=="__main__":
    entities = ['AAPL']#get_available_entities()
    # print(entities)
    for symbol in entities[:1]:
        data_obj = {}
        for key in APIS:
            api_url = APIS[key]
            uri = api_url[0].format(symbol)
            raw_response = requests.get(uri,params=payload)
            data_obj[key] = raw_response.json()
        write_to_json_file(symbol,data_obj)

# merge and acquisitions
# earning calls 
# 10k 
# sec filings (Sentiment analysis)
# press releases
# social media sentiments from website like stockwits/twitter
        