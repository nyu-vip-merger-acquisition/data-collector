from financial_apis import get_eligible_entities
from models import Entity
from tqdm import tqdm

def collect_data_from_financialprep():
    entities = get_eligible_entities()
    for i in tqdm(range(len(entities))):
        symbol = entities[i]
        entity = Entity(symbol)
        print("*"*89)
        # print(entity)
        entity.write_to_file()


if __name__=="__main__":
    collect_data_from_financialprep()