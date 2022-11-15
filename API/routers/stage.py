from fastapi import APIRouter, Header
from databases.databases import db
from bson import json_util
from json import loads


router = APIRouter()
results=db.Results

@router.get("/stage")
def get_stages():
    res = list(results["stage"].find({}))
    return loads(json_util.dumps(res))
    