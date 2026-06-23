import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")

client = MongoClient(MONGODB_URL)

db = client["eco_visionars"]

reports_collection = db["reports"]

print("✅ MongoDB Connected Successfully")


