from financial_apis import get_eligible_entities
from models import Entity

def collect_data_from_financialprep():
    entities = get_eligible_entities()
    for symbol in entities:
        entity = Entity(symbol)
        print(entity)
        entity.write_to_file()


if __name__=="__main__":
    collect_data_from_financialprep()