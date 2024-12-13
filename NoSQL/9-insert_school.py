#!/usr/bin/env python3
"""inserting a doc in the db with python"""


import pymongo


def insert_school(mongo_collection, **keywargs):
    """fuction to instert docs in the db"""
    new_Doc = mongo_collection.insert_one({**keywargs})
    return new_Doc.inserted_id
