#!/usr/bin/env python3

import sys


def disp_current_inventory(inventory: dict[str, int]) -> None:
    # item_max: str = ""
    # item_min: str = ""
    # for item, quantity in inventory.items():
    #     if item_min == "" or inventory[item_min] > quantity:
    #         item_min = item
    #     if item_max == "" or inventory[item_max] < quantity:
    #         item_max = item
 
    for item, quantity in inventory.items():
        print(f"{item}: {quantity} units", end=" ")
        print(f"({round(quantity/sum(inventory.values())*100, 1)}%)")


def disp_inventory_statistics(inventory: dict[str, int]) -> None:
    item_max: str = ""
    item_min: str = ""
    for item, quantity in inventory.items():
        if item_min == "" or inventory[item_min] > quantity:
            item_min = item
        if item_max == "" or inventory[item_max] < quantity:
            item_max = item
    print(f"Most abundant: {item_max} ({inventory[item_max]} units)")
    print(f"Least abundant: {item_min} ({inventory[item_min]} units)")


def disp_item_categories(inventory: dict[str, int]) -> None:
    item_max: str = ""
    item_min: str = ""
    for item, quantity in inventory.items():
        if item_min == "" or inventory[item_min] > quantity:
            item_min = item
        if item_max == "" or inventory[item_max] < quantity:
            item_max = item
    print(f"Moderate: {inventory}")
    print(f"Scarce: {inventory}")


def disp_management_suggestions(inventory: dict[str, int]) -> None:
    item_max: str = ""
    item_min: str = ""
    for item, quantity in inventory.items():
        if item_min == "" or inventory[item_min] > quantity:
            item_min = item
        if item_max == "" or inventory[item_max] < quantity:
            item_max = item
    print(f"Restock needed: {inventory.keys()}")


def disp_dictionary_properties(inventory: dict[str, int]) -> None:
    item_max: str = ""
    item_min: str = ""
    for item, quantity in inventory.items():
        if item_min == "" or inventory[item_min] > quantity:
            item_min = item
        if item_max == "" or inventory[item_max] < quantity:
            item_max = item
    print(f"Dictionary keys: {inventory.keys()}")
    print(f"Dictionary values: {inventory.values()}")
    item:str = "sword"
    print(f"Sample lookup - ’{item}’ in inventory: {True}")


def load_inventory(argv: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    name: str = ""
    quantity: int = 0
    for i in range(1, argv.__len__()):
        name = argv[i].split(":")[0]
        quantity = int(argv[i].split(":")[1])
        inventory[name] = quantity
    return (inventory)


def inventory_system(argv: list[str]) -> None:
    print("=== Inventory System Analysis ===\n")
    inventory: dict[str, int] = load_inventory(argv)
    total_items: int = sum(inventory.values())
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}")
    print("")
    print("=== Current Inventory ===")
    disp_current_inventory(inventory)
    print("")
    print("=== Inventory Statistics ===")
    disp_inventory_statistics(inventory)
    print("")
    print("=== Item Categories ===")
    disp_item_categories(inventory)
    print("")
    print("=== Management Suggestions ===")
    disp_management_suggestions(inventory)
    print("")
    print("=== Dictionary Properties Demo ===")
    disp_dictionary_properties(inventory)
    print("")


if __name__ == "__main__":
    inventory_system(sys.argv)
