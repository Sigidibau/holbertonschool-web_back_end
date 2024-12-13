#!/usr/bin/env python3
"""inserting a doc in the db with python"""


import pymongo


def instert_school(mongo_colletcion, **keywargs):
    """fuction to instert docs in the db"""
    new_Doc = mongo_colletcion.insert_one({**keywargs})
    return new_Doc.inserted_id
