#!/usr/bin/env python3
""" pythoncode thar List all docs in a collection """
import pymongo


def list_all(mongo_collection) -> list:
    """ Listing all docs in a collection
        Args:
            mongo_collection: Collection of object

        Return:
            List with documents, otherwise []
    """
    documents: list = []

    for document in mongo_collection.find():
        documents.append(document)

    return documents
