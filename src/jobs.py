from logging_config import with_logging, logging
import requests
import json
from datetime import datetime


@with_logging
def generate_auto_review():
    urlbase = ""
    # first get coders
    response = requests.get(url=urlbase + "/coder/all")
    coderIds = [coder['coder_id'] for coder in json.loads(response.content)]

    # get all problem for each coder and select n problems for auto review
    # based on timestamps, update their status as in_auto_review
    for id in coderIds:
        response = requests.get(url=urlbase + "/problem/all",
                                params={'coder_id': id})
        if response.status_code < 300:
            problems = json.loads(response.content)
            problems.sort(key=lambda p: datetime.strptime(p['date_last_solved'], "%m/%d/%Y"))
            # sort the problems with timestamps
            for p in problems[:5]:
                logging.info(p)
