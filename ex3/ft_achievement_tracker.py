#!/usr/bin/env python3


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


def load_achievements() -> dict[str, set[str]]:
    players_achievements: dict[str, set[str]] = {
        "Alice": {"first_kill", "level_10", "treasure_hunter", "speed_demon"},
        "Bob": {"first_kill", "level_10", "boss_slayer", "collector"},
        "Charlie": {"level_10", "treasure_hunter", "boss_slayer",
                    "speed_demon", "perfectionist"}}
    return (players_achievements)


def achievement_tracker() -> None:
    print("=== Achievement Tracker System ===\n")
    players: dict[str, set[str]] = load_achievements()
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
