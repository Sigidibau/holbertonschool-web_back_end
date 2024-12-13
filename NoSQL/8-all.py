#!/usr/bin/env python3
"""code to list all the docs in the db"""


import pymongo


def list_all(mongo_collection):
    """fucn to list all the docs of the db"""
    return [] if mongo_collection is None else mongo_collection.find()
