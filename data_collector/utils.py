import json
import os
import orjson
from config import RAW_FILE_DATA_PATH

def write_to_json_file(file_path,data_obj):
    # Serializing json
    json_object = orjson.dumps(data_obj)
    
    # Writing to sample.json
    with open(file_path, "w") as outfile:
        outfile.write(json_object)
