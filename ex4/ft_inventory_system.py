#!/usr/bin/env python3

import sys


class RedundantItemError(Exception):
    """Base class for Inventory-related errors."""


def disp_current_inventory(inventory: dict[str, int]) -> None:
    total_quantities = sum(inventory.values())
    if total_quantities == 0:
        total_quantities = 1
    if inventory == {}:
        print("Inventory is empty.")
    else:
        for item, quantity in inventory.items():
            print(f"{item}: {quantity} units", end=" ")
            print(f"({round((quantity/total_quantities)*100, 1)}%)")


def disp_inventory_statistics(inventory: dict[str, int]) -> None:
    if inventory == {}:
        print("Inventory is empty.")
    else:
        max_item, max_qty = max(inventory.items(), key=lambda item: item[1])
        min_item, min_qty = min(inventory.items(), key=lambda item: item[1])
        print(f"Most abundant: {max_item} ({max_qty} units)")
        print(f"Least abundant: {min_item} ({min_qty} units)")


def disp_item_categories(inventory: dict[str, int]) -> None:
    if inventory == {}:
        print("Inventory is empty.")
    else:
        moderate_item = {i: q for i, q in inventory.items() if q > 3}
        scarce_item = {i: q for i, q in inventory.items() if q <= 3}
        print(f"Moderate: {moderate_item}")
        print(f"Scarce: {scarce_item}")


def disp_management_suggestions(inventory: dict[str, int]) -> None:
    if inventory == {}:
        print("Inventory is empty.")
    else:
        print(f"Restock needed: {[i for i, q in inventory.items() if q < 3]}")


def disp_dictionary_properties(inventory: dict[str, int]) -> None:
    print(f"Dictionary keys: {inventory.keys()}")
    print(f"Dictionary values: {inventory.values()}")
    item: str = "sword"
    print(f"Sample lookup - ’{item}’ in inventory:", end=" ")
    print(f"{bool(inventory.get(item))}")


def load_inventory(argv: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    name: str = ""
    quantity: int = 0
    if len(argv) > 1:
        for i in range(1, len(argv)):
            try:
                name = argv[i].split(":")[0]
                if name in inventory:
                    raise RedundantItemError()
                quantity = int(argv[i].split(":")[1])
                inventory[name] = quantity
            except RedundantItemError:
                print(f"Redundant item ’{name}’ - discarding")
            except IndexError:
                print(f"Error - invalid parameter ’{name}’")
            except ValueError:
                print(f"Quantity error for ’{name}':", end=" ")
                print(f"invalid literal for int() with base 10:", end=" ")
                print(f"’{argv[i].split(":")[1]}’")
    return (inventory)


def inventory_system(argv: list[str]) -> None:
    print("=== Inventory System Analysis ===\n")
    inventory: dict[str, int] = load_inventory(argv)
    if inventory == {}:
        print("Inventory is empty.")
    else:
        print(f"Got inventory: {inventory}")
        print(f"Item list: {list(inventory.keys())}")
        total_items: int = sum(inventory.values())
        print(f"Total quantity of the {len(inventory)} items: {total_items}")
        for item, quantity in inventory.items():
                print(f"Item {item}: represents", end=" ")
                print(f"{round((quantity/total_items)*100, 1)}%")
        max_item, max_qty = max(inventory.items(), key=lambda item: item[1])
        print(f"Item most abundant: {max_item} with quantity {max_qty}")
        min_item, min_qty = min(inventory.items(), key=lambda item: item[1])
        print(f"Item least abundant: {min_item} with quantity {min_qty}")
        inventory["magic_item"] = 1
        print(f"Updated inventory: {inventory}")
        print("")
        # print("\n=== OLD EXERCICE ===\n")
        # print(f"Unique item types: {len(inventory)}")
        # print("")
        # print("=== Current Inventory ===")
        # disp_current_inventory(inventory)
        # print("")
        # print("=== Inventory Statistics ===")
        # disp_inventory_statistics(inventory)
        # print("")
        # print("=== Item Categories ===")
        # disp_item_categories(inventory)
        # print("")
        # print("=== Management Suggestions ===")
        # disp_management_suggestions(inventory)
        # print("")
        # print("=== Dictionary Properties Demo ===")
        # disp_dictionary_properties(inventory)
        # print("")


if __name__ == "__main__":
    inventory_system(sys.argv)
