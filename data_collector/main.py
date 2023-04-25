from financial_apis import get_eligible_entities
from models import Entity
from tqdm import tqdm
import os

def collect_data_from_financialprep():
    ignore_entities = [os.path.splitext(filename)[0] for filename in os.listdir('./data/raw_files/')]
    entities = get_eligible_entities()
    entities = list(set(entities)-set(ignore_entities))
    for i in tqdm(range(len(entities))):
        symbol = entities[i]
        entity = Entity(symbol)
        print("*"*89)
        # print(entity)
        entity.write_to_file()


if __name__=="__main__":
    collect_data_from_financialprep()


    
    