#!/usr/bin/env python3


import random


def disp_players_achievements(players: dict[str, set[str]]) -> None:
    for player, achievements in players.items():
        print(f"Player {player} achievements: {achievements}")


def all_unique_achievements(players: dict[str, set[str]]) -> set[str]:
    union: set[str] = set()
    for achievements in players.values():
        union = union.union(achievements)  # union & achievements
    return (union)


def common_to_all_players(players: dict[str, set[str]]) -> set[str]:
    inter: set[str] = next(iter(players.values()), set())
    for achievements in players.values():
        inter = inter.intersection(achievements)  # inter | achievements
    return (inter)


def unique_achievments_by_players(player: str, players: dict[str, set[str]]) -> set[str]:
    achievements: set[str] = players[player]
    for p, a in players.items():
        if p != player:
            achievements = achievements.difference(a)
    return (achievements)


def missing_achievements_by_player(player: str, players: dict[str, set[str]], achievements: set[str]) -> set[str]:
    return (achievements.difference(players[player]))


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


def gen_player_achievements(players: list[str], achievements: set[str]) -> dict[str, set[str]]:
    players_achievements: dict[str, set[str]] = {}
    for p in players:
        players_achievements[p] = set()
        nb_achievements = random.randint(1, 20)
        for i in range(nb_achievements):
            players_achievements[p].add(random.choice(list(achievements)))
    return (players_achievements)


def achievement_tracker() -> None:
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
    print("=== Achievement Tracker System ===\n")
    players_achievments: dict[str, set[str]] = gen_player_achievements(players, achievements)
    player1: str = ""
    player2: str = ""
    disp_players_achievements(players_achievments)
    print("")
    print(f"All distinct achievements: {all_unique_achievements(players_achievments)}")
    print("Total unique achievements:", end=" ")
    print(f"{len(all_unique_achievements(players_achievments))}")
    print("")
    print(f"Common to all players: {common_to_all_players(players_achievments)}")
    print("")
    for p in players_achievments:
        print(f"Only {p} has: {unique_achievments_by_players(p, players_achievments)}")
    print("")
    for p in players_achievments:
        print(f"{p} is missing: {missing_achievements_by_player(p, players_achievments, achievements)}")
    print("")
    print("\n=== OLD EXERCICE ===\n")
    print(f"Rare achievements (1 player): {rare_achievements(players_achievments)}")
    print("")
    player1 = "Alice"
    player2 = "Bob"
    print(f"{player1} vs {player2} common:", end=" ")
    print(f"{p1_inter_p2(player1, player2, players_achievments)}")
    print(f"{player1} unique: {p1_diff_p2(player1, player2, players_achievments)}")
    print(f"{player2} unique: {p1_diff_p2(player2, player1, players_achievments)}")


if __name__ == "__main__":
    achievement_tracker()
