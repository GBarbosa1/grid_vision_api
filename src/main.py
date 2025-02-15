from fastapi import FastAPI, Query
from datetime import date
from typing import Optional
from datetime import datetime
from configs.configs_loader import load_json_and_set_env
from api_infraestructure.get_wrapper import RequestWrapper
import os
import logging
api_wrapper = RequestWrapper()
load_json_and_set_env("configs\endpoints.json")
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI mock template!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

@app.get("/dates/")
def read_dates(start_date: Optional[str] = Query(None), end_date: Optional[str] = Query(None)):
    try:
        igpm_base_url = os.environ["igpm_base_endpoint"]
        igpm_base_url = igpm_base_url.replace('{data_inicio}',start_date)
        igpm_base_url = igpm_base_url.replace('{data_final}',end_date)
        payload = api_wrapper.get(endpoint=igpm_base_url)
        return payload
    except ValueError:
        print(igpm_base_url)
        return {"error": "Invalid date format. Use dd/mm/yyyy."}
