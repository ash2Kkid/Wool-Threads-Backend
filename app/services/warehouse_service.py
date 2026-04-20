from app.database.warehouse_db import get_all_warehouses, get_nearby_warehouses


def fetch_all_warehouses():
    return get_all_warehouses()


def fetch_nearby_warehouses(city: str):
    return get_nearby_warehouses(city)