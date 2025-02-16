from fastapi import FastAPI, Query
from typing import Optional
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

@app.get("/igpm/")
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

@app.get("/ipca/")
def read_dates(start_date: Optional[str] = Query(None), end_date: Optional[str] = Query(None)):
    try:
        ipca_base_endpoint = os.environ["ipca_base_endpoint"]
        ipca_base_endpoint = ipca_base_endpoint.replace('{data_inicio}',start_date)
        ipca_base_endpoint = ipca_base_endpoint.replace('{data_final}',end_date)
        payload = api_wrapper.get(endpoint=ipca_base_endpoint)
        return payload
    except ValueError:
        return {"error": "Invalid date format. Use dd/mm/yyyy."}

@app.get("/currencies/")
def read_filters(start_date: Optional[str] = Query(None), end_date: Optional[str] = Query(None), currency1: Optional[str] = Query(None), currency2: Optional[str] = Query(None)):
    try:
        cambio = os.environ["cambio"]
        start_date = start_date.replace("/","")
        end_date = end_date.replace("/","")
        cambio = cambio.replace('{data_inicio}',start_date)
        cambio = cambio.replace('{data_final}',end_date)
        cambio = cambio.replace('{currency_01}',currency1)
        cambio = cambio.replace('{currency_02}',currency2)
        payload = api_wrapper.get(endpoint=cambio)
        return payload, cambio
    except ValueError:
        return {"error": "Invalid date format. Use dd/mm/yyyy."}
    
@app.get("/geracao/")
def read_filters(start_date: Optional[str] = Query(None), end_date: Optional[str] = Query(None), currency1: Optional[str] = Query(None), currency2: Optional[str] = Query(None)):
    try:
        dados_geracao = os.environ["dados_geracao_energia"]
        start_date = start_date.replace("/","")
        end_date = end_date.replace("/","")
        dados_geracao = dados_geracao.replace('{data_inicio}',start_date)
        dados_geracao = dados_geracao.replace('{data_final}',end_date)
        dados_geracao = dados_geracao.replace('{currency_01}',currency1)
        dados_geracao = dados_geracao.replace('{currency_02}',currency2)
        payload = api_wrapper.get(endpoint=dados_geracao)
        return payload
    except ValueError:
        return {"error": "Invalid date format. Use dd/mm/yyyy."}