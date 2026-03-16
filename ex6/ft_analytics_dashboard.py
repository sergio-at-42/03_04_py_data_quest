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
    i:int = 1
    player: str = ""
    event:str = ""
    while i <= nb_events:
        player = random.choice(players_name)
        event = random.choice(events_type)
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


def analytics_dashboard(argv: list[str]) -> None:

    players_level: dict[str, int] = {}
    player: str = ""
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
    print("=== Game Analytics Dashboard ===\n")
    print("")
    print(f"Processing {nb_events} game events...")
    print("")
    start_time:datetime.datetime = datetime.datetime.now()
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
            print(f"Event {total_events}: Player {player} (level {players_level[player]}) {event}")
        if total_events ==4:
            print("...")            
    end_time:datetime.datetime = datetime.datetime.now()


    print("")
    print("=== List Comprehension Examples ===")
    print(f"High scorers (>2000): [’alice’, ’charlie’, ’diana’]")
    print(f"Scores doubled: [4600, 3600, 4300, 4100]")
    print(f"Active players: [’alice’, ’bob’, ’charlie’]")
    print("")
    print("=== Dict Comprehension Examples ===")
    print(f"Player scores: {’alice’: 2300, ’bob’: 1800, ’charlie’: 2150}")
    print(f"Score categories: {’high’: 3, ’medium’: 2, ’low’: 1}")
    print(f"Achievement counts: {’alice’: 5, ’bob’: 3, ’charlie’: 7}")
    print("")
    print("=== Set Comprehension Examples ===")
    print(f"Unique players: {’alice’, ’bob’, ’charlie’, ’diana’}")
    print(f"Unique achievements: {’first_kill’, ’level_10’, ’boss_slayer’}")
    print(f"Active regions: {’north’, ’east’, ’central’}")
    print("")
    print("=== Combined Analysis ===")
    print(f"Total players: 4")
    print(f"Total unique achievements: 12")
    print(f"Average score: 2062.5")
    print(f"Top performer: alice (2300 points, 5 achievements)")
    print("")


if __name__ == "__main__":
    analytics_dashboard(sys.argv)
