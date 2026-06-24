def filter_shop_inventory(shop_items, balance):
    return [item for (item, cost) in shop_items if balance >= cost]