#!/usr/bin/env python3
""" 11-schools_by_topic.py """

def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools having a specific topic

    Args:
        mongo_collection: pymongo collection object
        topic (str): topic to search for

    Returns:
        list of documents (empty list if none)
    """
    if mongo_collection is None or not topic:
        return []

    return list(mongo_collection.find({"topics": topic}))
