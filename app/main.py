import os
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv

load_dotenv()

from llms import *
from workflow import generate_plan

app = FastAPI()
