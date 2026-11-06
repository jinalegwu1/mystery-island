def add_item(player, item):
    if item in player["inventory"]:
        return False
    else:
        item.append(item)
        return True
