from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.responses import RedirectResponse
import pandas as pd
import json


pelis= pd.read_csv('https://objectstorage.sa-saopaulo-1.oraclecloud.com/n/gr4oj5h2hdd0/b/documentos/o/pelis.csv')

app = FastAPI()

@app.get('/')
async def root():
    return RedirectResponse(url='/docs/')


# @app.get('/plataform/{pelis}')
# async def get_count_platform(pelis:list):
#     select = pelis[pelis['show_id'].isin(pelis)]
#     return JSONResponse(content=json.loads(select.to_json()))


@app.get('/peli_ml')
async def get_data_ml():
    return JSONResponse(content=json.loads(pelis.to_json())) 
