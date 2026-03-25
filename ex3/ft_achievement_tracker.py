#!/usr/bin/env python3


import random


def disp_players_achievements(players: dict[str, set[str]]) -> None:
    for player, achievements in players.items():
        print(f"Player {player} achievements: {achievements}")


def all_unique_achievements(players: dict[str, set[str]]) -> set[str]:
    union: set[str] = {""}
    for achievements in players.values():
        if union == {""}:
            union = achievements
        else:
            union = union.union(achievements)  # union & achievements
    return (union)


def common_to_all_players(players: dict[str, set[str]]) -> set[str]:
    inter: set[str] = {""}
    for achievements in players.values():
        if inter == {""}:
            inter = achievements
        else:
            inter = inter.intersection(achievements)  # inter | achievements
    return (inter)


def rare_achievements(players: dict[str, set[str]]) -> set[str]:
    sym_diff: set[str] = {""}
    not_unique: set[str] = {""}
    for achievements in players.values():
        if sym_diff == {""}:
            sym_diff = achievements
        else:
            not_unique = not_unique.union(sym_diff.intersection(achievements))
            sym_diff = (sym_diff.union(achievements)).difference(not_unique)
            # sym_diff = sym_diff.symmetric_difference(achievements)
            # sym_diff = sym_diff.difference(not_unique)
    return (sym_diff)


def p1_inter_p2(p1: str, p2: str, players: dict[str, set[str]]) -> set[str]:
    p1_ach: set[str] = players[p1]
    p2_ach: set[str] = players[p2]
    p1_inter_p2: set[str] = p1_ach.intersection(p2_ach)
    return (p1_inter_p2)


def p1_diff_p2(p1: str, p2: str, players: dict[str, set[str]]) -> set[str]:
    p1_ach: set[str] = players[p1]
    p2_ach: set[str] = players[p2]
    p1_diff_p2: set[str] = p1_ach.difference(p2_ach)
    return (p1_diff_p2)


def gen_player_achievements() -> dict[str, set[str]]:
    achievements: set[str] = {
        "Speed Demon",
        "Level 10",
        "Perfectionist",
        "First Kill",
        "Crafting Genius",
        "Strategist",
        "World Savior",
        "Speed Runner",
        "Survivor",
        "Master Explorer",
        "Treasure Hunter",
        "Unstoppable",
        "First Steps",
        "Collector Supreme",
        "Untouchable",
        "Sharp Mind",
        "Boss Slayer"
    }
    players: list[str] = [
        "Alice",
        "Bob",
        "Charlie",
        "Dylan"
    ]
    players_achievements: dict[str, set[str]] = {}
    achievements_done: set[str] = set()
    for p in players:
        nb_achievements = random.randint(10, 30)
        for i in range(nb_achievements):
            achievements_done.add(random.choice(list(achievements)))
        players_achievements[p] = achievements_done
    return (players_achievements)


def achievement_tracker() -> None:
    print("=== Achievement Tracker System ===\n")
    players: dict[str, set[str]] = gen_player_achievements()
    player1: str = ""
    player2: str = ""
    disp_players_achievements(players)
    print("")
    print("=== Achievement Analytics ===")
    print(f"All unique achievements: {all_unique_achievements(players)}")
    print("Total unique achievements:", end=" ")
    print(f"{all_unique_achievements(players).__len__()}")
    print("")
    print(f"Common to all players: {common_to_all_players(players)}")
    print(f"Rare achievements (1 player): {rare_achievements(players)}")
    print("")
    player1 = "Alice"
    player2 = "Bob"
    print(f"{player1} vs {player2} common:", end=" ")
    print(f"{p1_inter_p2(player1, player2, players)}")
    print(f"{player1} unique: {p1_diff_p2(player1, player2, players)}")
    print(f"{player2} unique: {p1_diff_p2(player2, player1, players)}")


if __name__ == "__main__":
    achievement_tracker()
