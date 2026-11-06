def add_item(player, item):
    if item in player["inventory"]:
        return False
    else:
        player["inventory"].append(item)
        return True
