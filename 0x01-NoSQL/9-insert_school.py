#!/usr/bin/env python3
""" pythonfuncs that Insert docs in the collections """
import pymongo


def insert_school(mongo_collection, **kwargs):
    """ Inserting new docs features

        Args:
            mongo_collection: Collection to pass
            kwargs: Dictionary with elements to put

        Return:
            Id of the new element
    """
    new_school = mongo_collection.insert_one(kwargs)

    return (new_school.inserted_id)
