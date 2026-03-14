#!/usr/bin/env python3

import sys
import datetime


def gen_fibo(n:int = 1):
    i:int = 3
    a:int = 0
    b:int = 1
    c:int = 0
    if n >= 1:
        yield a
    if n >= 2:
        yield b
    while i <= n:
        c = a + b
        yield c
        a = b
        b = c
        i += 1


def is_prime_number(num:int) -> bool:
    prime:bool = False
    d: int = 3
    if num >= 2:
        prime = True
        while d < num and prime:
            if num % d == 0:
                prime = False
            d += 1
    return (prime)


def gen_prime_number(n:int = 1):
    i:int = 2
    num:int = 3
    if n >= 1:
        yield 2
    while i <= n:
        while not is_prime_number(num):
            num += 2
        yield num
        num += 2
        i += 1


def data_stream(argv: list[str]) -> None:
    player: str = ""
    level: int = 0
    event: str = ""
    total_events:int = 0
    nb_events: int
    high_level:int = 0
    treaser_event: int = 0
    level_up_event:int = 0
    start_time:datetime
    end_time:datetime
    n:int = 0
    try:
        nb_events = int(argv[1])
    except Exception:
        nb_events = 1000
    print("=== Game Data Stream Processor ===\n")
    print("")
    print("Processing 1000 game events...")
    print("")
    start_time = datetime.datetime.now()
    for i in range(1, nb_events + 1):
        print(f"Event {i}: Player {player} (level {level}) {event}")
        total_events += 1
        if high_level < level:
            high_level = level
        if "treasure" in event:
            treaser_event += 1
        if event == "leveled up":
            level_up_event += 1
    end_time = datetime.datetime.now()
    print("")
    print("=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treaser_event}")
    print(f"Level-up events: {level_up_event}")
    print("")
    print(f"Memory usage: {nb_events}")
    print(f"Processing time: {(end_time - start_time)} seconds   {end_time}")
    print("")
    print("=== Generator Demonstration ===")
    n = 10
    print(f"Fibonacci sequence (first {n}):", end="")
    for fibo in gen_fibo(n):
        print(f"{fibo}", end=", ")
    print("")
    n = 5
    print(f"Prime numbers (first {n}):", end="")
    for prime in gen_prime_number(n):
        print(f"{prime}", end=", ")
    print("")


if __name__ == "__main__":
    data_stream(sys.argv)
