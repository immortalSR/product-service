import random

def ProductFactory():
    return {
        "id": random.randint(1, 1000),
        "name": "Product" + str(random.randint(1, 100)),
        "category": "General",
        "available": True
    }
