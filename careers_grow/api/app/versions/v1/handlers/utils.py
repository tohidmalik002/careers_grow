def get_one(payload):
    print(payload)
    item_id = payload.get("id")
    # Simulate fetching an item by ID
    return {"id": item_id, "name": "Sample Item"}