#!/usr/bin/env python3
""" 12-log_stats.py """

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx

    # Total documents in collection
    total_logs = nginx_collection.count_documents({}) if nginx_collection else 0
    print(f"{total_logs} logs")

    # Count per method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({"method": method}) if nginx_collection else 0
        print(f"\tmethod {method}: {count}")

    # Count GET /status
    status_check = nginx_collection.count_documents({"method": "GET", "path": "/status"}) if nginx_collection else 0
    print(f"{status_check} status check")
