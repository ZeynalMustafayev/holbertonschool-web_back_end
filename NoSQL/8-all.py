#!/usr/bin/env python3
"""List all documents in Python"""


def list_all(mongo_collection):
    """list_all"""
    if mongo_collection == "":
        return []
    return list(mongo_collection.find())