import json
import os
import orjson
from config import MAX_CALLS_PER_MINUTE,ONE_MINUTE
from ratelimit import limits, RateLimitException, sleep_and_retry
import requests


def write_to_json_file(file_path,data_obj):
    # Serializing json
    json_object = orjson.dumps(data_obj)
    
    # Writing to sample.json
    with open(file_path, "w") as outfile:
        outfile.write(json_object)

@sleep_and_retry
@limits(calls=MAX_CALLS_PER_MINUTE, period=ONE_MINUTE)
def throttled_api_request(uri,params):
    raw_response = requests.get(uri,params=params)
    response = orjson.loads(raw_response.text)
    return response