#!/usr/bin/env python3

import sys
import datetime


class Player:

    def __init__(self, name: str, level: int = 0) -> None:
        self.name: str = name
        self.level: int = level


class TypeEvents:

    events_type: list[str] = ["killed monster",
                               "found treasure",
                               "leveled up,"]

    def __init__(self, event_num: int = 0) -> None:
        if event_num >= len(TypeEvents.events_type):
            event_num = 0
        self.event: str = TypeEvents.events_type[event_num]


class Event:

    def __init__(self, player: Player, event: TypeEvents) -> None:
        self.player: Player = player
        self.event: TypeEvents = event


class GameEvents:
    
    events: list[Event] = []
    total_events:int = 0
    high_level:int = 0
    treaser_event: int = 0
    level_up_event:int = 0


    @classmethod
    def get_events(cls) -> list[Event]:
        return (cls.events)

    @classmethod
    def set_events(cls, events: list[Event]) -> list[Event]:
        cls.events = events
        return (cls.events)

    @classmethod
    def add_event(cls, event: Event) -> Event:
        cls.events.append() = event
        cls.total_events += 1
        if cls.high_level < event.player.level:
            cls.high_level = event.player.level
        if "treasure" in event.event.event:
            cls.treaser_event += 1
        if event.event.event == "leveled up":
            cls.level_up_event += 1
        return (cls.events[len(cls.events) - 1])


def gen_event(nb_events: int = 1000):
    events_type: list[str] = ["killed monster",
                               "found treasure",
                               "leveled up,"]
    players_name: list[str] = ["alice",
                               "bob",
                               "tatiana",
                               "charlie",
                               "sergio"]
    i:int = 1
    player: str = ""
    event:str = ""
    while i <= nb_events:
        while not is_prime_number(num):
            num += 2
        yield (player, event)
        i += 1


def gen_fibo(n:int = 1):
    i:int = 3
    a:int = 0
    b:int = 1
    c:int = 0
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
    level: int = 0
    event: str = ""
    nb_events: int
    total_events:int = 0
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
    print(f"Processing {nb_events} game events...")
    print("")
    start_time:datetime.datetime = datetime.datetime.now()
    for player, event in gen_event(nb_events):
    # for i in range(1, nb_events + 1):
        total_events += 1
        if high_level < players_level[player]:
            high_level = level
        if "treasure" in event:
            treaser_event += 1
        if event == "leveled up":
            level_up_event += 1
            players_level[player] += 1
        if total_events <= 3:
            print(f"Event {total_events}: Player {player} (level {level}) {event}")
        if total_events ==4:
            print("...")            
    end_time:datetime.datetime = datetime.datetime.now()
    print("")
    print("=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treaser_event}")
    print(f"Level-up events: {level_up_event}")
    print("")
    print("Memory usage: Constant (streaming)")
    pt:datetime.timedelta = end_time - start_time
    print(f"Processing time: {pt.seconds}.{pt.microseconds // 1000:03d} seconds ({pt.microseconds} microseconds)")
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
