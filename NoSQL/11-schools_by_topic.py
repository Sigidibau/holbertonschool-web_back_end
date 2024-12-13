#!/usr/bin/env python3
"""func to return a specific topic from db"""


import pymongo
from typing import List, Dict


def schools_by_topic(mongo_collection, topic: str) -> List[Dict]:
    """this func return a specific topic from the db"""
    return list(mongo_collection.find({"topics": topic}))
