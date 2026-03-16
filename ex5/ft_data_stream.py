#!/usr/bin/env python3

import sys
import datetime
import random


def gen_event(nb_events: int = 1000):
    events_type: list[str] = ["killed monster",
                              "found treasure",
                              "leveled up"]
    players_name: list[str] = ["alice",
                               "bob",
                               "tatiana",
                               "charlie",
                               "sergio"]
    i: int = 1
    player: str = ""
    event: str = ""
    while i <= nb_events:
        player = random.choice(players_name)
        event = random.choice(events_type)
        yield (player, event)
        i += 1


def gen_fibo(n: int = 1):
    i: int = 3
    a: int = 0
    b: int = 1
    c: int = 0
    if n >= 1:
        yield (a, n == 1)
    if n >= 2:
        yield (b, n == 2)
    while i <= n:
        c = a + b
        yield (c, i == n)
        a = b
        b = c
        i += 1


def is_prime_number(num: int) -> bool:
    prime: bool = False
    d: int = 3
    if num >= 2:
        prime = True
        while d < num and prime:
            if num % d == 0:
                prime = False
            d += 1
    return (prime)


def gen_prime_number(n: int = 1):
    i: int = 2
    num: int = 3
    if n >= 1:
        yield (2, n == 1)
    while i <= n:
        while not is_prime_number(num):
            num += 2
        yield (num, n == i)
        num += 2
        i += 1


def data_stream(argv: list[str]) -> None:
    players_level: dict[str, int] = {}
    player: str = ""
    event: str = ""
    nb_events: int
    total_events: int = 0
    treaser_event: int = 0
    level_up_event: int = 0
    start_time: datetime.datetime
    end_time: datetime.datetime
    n: int = 0
    try:
        nb_events = int(argv[1])
    except Exception:
        nb_events = 1000
    print("=== Game Data Stream Processor ===\n")
    print("")
    print(f"Processing {nb_events} game events...")
    print("")
    start_time = datetime.datetime.now()
    for player, event in gen_event(nb_events):
        total_events += 1
        if player not in players_level.keys():
            players_level[player] = random.randint(1, 12)
        if "treasure" in event:
            treaser_event += 1
        if "level" in event:
            level_up_event += 1
            players_level[player] += 1
        if total_events <= 3:
            print(f"Event {total_events}:", end=" ")
            print(f"Player {player} (level {players_level[player]}) {event}")
        if total_events == 4:
            print("...")
    end_time = datetime.datetime.now()
    print("")
    print("=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print("High-level players (10+):", end=" ")
    print(f"{sum(1 for level in players_level.values() if level > 10)}")
    print(f"Treasure events: {treaser_event}")
    print(f"Level-up events: {level_up_event}")
    print("")
    print("Memory usage: Constant (streaming)")
    pt: datetime.timedelta = end_time - start_time
    print("Processing time: ", end=" ")
    print(f"{pt.seconds}.{pt.microseconds // 1000:03d} seconds", end=" ")
    print(f"({pt.microseconds} microseconds)")
    print("")
    print("=== Generator Demonstration ===")
    n = 10
    print(f"Fibonacci sequence (first {n}):", end=" ")
    for fibo, last in gen_fibo(n):
        print(f"{fibo}{"" if last else ", "}", end="")
    print("")
    n = 5
    print(f"Prime numbers (first {n}):", end=" ")
    for prime, last in gen_prime_number(n):
        print(f"{prime}{"" if last else ", "}", end="")
    print("")


if __name__ == "__main__":
    data_stream(sys.argv)
