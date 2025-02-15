from fastapi import FastAPI
from datetime import datetime
from configs.configs_loader import load_json_and_set_env
from api_infraestructure.get_wrapper import RequestWrapper
import os
import logging
api_wrapper = RequestWrapper
load_json_and_set_env("/workspaces/grid_vision_api/src/configs/endpoints.json")

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI mock template!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

@app.get("/dates/data_inicio={data_inicio}&data_fim={data_fim}")
def read_dates(data_inicio: str, data_fim: str):
    try:
        date_obj1 = datetime.strptime(data_inicio, "%d/%m/%Y")
        date_obj2 = datetime.strptime(data_fim, "%d/%m/%Y")
        igpm_base_url = os.environ["igpm_base_endpoint"]
        igpm_base_url.replace('{data_inicio}',date_obj1)
        igpm_base_url.replace('{data_final}',date_obj2)
        logger.error(igpm_base_url)
        api_wrapper.get(igpm_base_url)
        return {
            "formatted_data_inicio": date_obj1.strftime("%Y-%m-%d"),
            "formatted_data_fim": date_obj2.strftime("%Y-%m-%d")
        }
    except ValueError:
        return {"error": "Invalid date format. Use dd/mm/yyyy."}
