import os
import json
import dataclasses

from financial_apis import get_company_info,get_company_financial,get_company_financial_ratios,get_key_metrics,get_company_enterprise_value,get_financial_growth
from config import FINANCE_API_KEY
from config import RAW_FILE_DATA_PATH


@dataclasses.dataclass
class Entity:
    def __init__(self,symbol) -> None:
        self.symbol = symbol

    @property
    def profile(self):
        return get_company_info(self.symbol)
    
    @property
    def income_statement(self):
        return get_company_financial(self.symbol,"income_statement")
    
    @property
    def reported_financial_statement(self):
        return get_company_financial(self.symbol,"reported_financial_statement")
    
    @property
    def balance_sheet_statement(self):
        return get_company_financial(self.symbol,"balance_sheet_statement")
    
    @property
    def cash_flow_statement(self):
        return get_company_financial(self.symbol,"cash_flow_statement")
    
    @property
    def company_financial_ratios(self):
        return get_company_financial_ratios(self.symbol)

    @property
    def key_metrics(self):
        return get_key_metrics(self.symbol)

    @property
    def enterprise_value(self):
        return get_company_enterprise_value(self.symbol)

    @property
    def financial_growth(self):
        return get_financial_growth(self.symbol)

    def __str__(self) -> str:
        fields = ['profile','income_statement','balance_sheet_statement', 'cash_flow_statement', 'reported_financial_statement', 'company_financial_ratios', 'enterprise_value', 'financial_growth', 'key_metrics' ]
        data_dict = {}
        for field in fields:
            data_dict[field] = getattr(self,field)

        return json.dumps(data_dict, indent=4)

    def write_to_file(self):
        json_string = str(self)
        file_path = os.path.join(RAW_FILE_DATA_PATH,"{}.json".format(self.symbol))
        with open(file_path, "w") as outfile:
            outfile.write(json_string)