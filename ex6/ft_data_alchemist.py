#!/usr/bin/env python3

import random


def ft_data_alchemist() -> None:
    players_origin: list[str] = [
        "Lucas", "Emma", "Léo", "Chloé", "Louis", "Manon", "Gabriel",
        "Hugo", "Lina", "Arthur", "Jade", "Nathan", "Louise", "Jules", "Zoé",
        "Adam", "Alice", "Noah", "Lola", "Ethan", "Inès", "Paul", "Sarah",
        "Tom", "Eva", "Sacha", "Clara", "Maxime", "Anna", "Mathis", "Mia",
        "Antoine", "Léa", "Romain", "Julia", "Enzo", "Ambre", "Baptiste",
        "Nina", "Théo", "Rose", "Camille"
    ]
    print("=== Game Game Data Alchemist ===")
    print("")
    players_names: list[str] = []
    for p in players_origin:
        if random.randint(0, 1):
            players_names.append(p.capitalize())
        else:
            players_names.append(p.lower())
    print(f"Initial list of players: {players_names}")
    print("")
    players_names_capitalized: list[str] = []
    players_names_only_capitalized: list[str] = []
    for p in players_names:
        players_names_capitalized.append(p.capitalize())
        if p.istitle():
            players_names_only_capitalized.append(p)
    print(f"New list with all names capitalized: {players_names_capitalized}")
    print("")
    print("New list of capitalized names only:", end=" ")
    print(f"{players_names_only_capitalized}")
    print("")
    players_with_score: dict[str, int] = {}
    players_with_score = {p: random.randint(0, 1000)
                          for p in players_names_capitalized}
    print(f"Score dict: {players_with_score}")
    print("")
    score_average: float = 0
    score_average = round(sum(players_with_score.values())
                          / len(players_with_score), 2)
    print(f"Score average is {score_average}")
    print("")
    players_hight_score: dict[str, int] = {}
    players_hight_score = {p: s
                           for p, s in players_with_score.items()
                           if s > score_average}
    print(f"High scores: {players_hight_score}")


if __name__ == "__main__":
    ft_data_alchemist()
