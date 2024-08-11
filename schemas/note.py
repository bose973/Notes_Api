def noteEntity(item):
    return {
        "id" : str(item["_id"]),
        "title" : item["title"],
        "description" : item["desc"],
        "important" : item["imp"]
    }

def notesEntity(items:list):
    return [noteEntity(item) for item in items]