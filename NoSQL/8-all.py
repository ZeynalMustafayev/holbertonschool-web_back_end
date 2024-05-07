#!/usr/bin/env python3
"""List all documents in Python"""


def list_all(mongo_collection):
    if mongo_collection == "":
        return []
    return mongo_collection.find()