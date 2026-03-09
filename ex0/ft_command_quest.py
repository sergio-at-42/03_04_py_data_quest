#!/usr/bin/env python3

import sys


def command_quest(argv: list[str]) -> None:
    print("=== Command Quest ===")
    if argv.__len__() == 1:
        print("No arguments provided!")
    print(f"Program name: {argv[0]}")
    if argv.__len__() > 1:
        print(f"Arguments received: {argv.__len__() - 1}")
        for i in range(1, argv.__len__()):
            print(f"Arguments {i}: {argv[i]}")
    print(f"Total arguments: {argv.__len__()}")


if __name__ == "__main__":
    command_quest(sys.argv)
