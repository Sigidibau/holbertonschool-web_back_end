#!/usr/bin/env python3
"""changing the db"""


import pymongo


def update_topics(mongo_collection, name, topics):
    """
    Updates the "topics" field of all documents in a MongoDB collection
    where the "name" field matches the given name.

    Args:
        mongo_collection (pymongo.collection.Collection):
        The MongoDB collection to update.
        name (str): The value of the "name" field to match.
        topics (list): A list of topics to set in the "topics" field.

    Returns:
        pymongo.results.UpdateResult:
        The result of the update operation.
        This contains information such as the number
        of documents matched and modified.
    """
    return mongo_collection.update_Many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
