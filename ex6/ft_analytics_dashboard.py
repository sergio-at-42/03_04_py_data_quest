#!/usr/bin/env python3

import random
from typing import Any


def analytics_dashboard() -> None:
    data: dict[str, Any] = {
        "players": {
            "alice": {
                "level": 41,
                "total_score": 2824,
                "sessions_played": 13,
                "favorite_mode": "ranked",
                "achievements_count": 5,
            },
            "bob": {
                "level": 16,
                "total_score": 4657,
                "sessions_played": 27,
                "favorite_mode": "ranked",
                "achievements_count": 2,
            },
            "charlie": {
                "level": 44,
                "total_score": 9935,
                "sessions_played": 21,
                "favorite_mode": "ranked",
                "achievements_count": 7,
            },
            "diana": {
                "level": 3,
                "total_score": 1488,
                "sessions_played": 21,
                "favorite_mode": "casual",
                "achievements_count": 4,
            },
            "eve": {
                "level": 33,
                "total_score": 1434,
                "sessions_played": 81,
                "favorite_mode": "casual",
                "achievements_count": 7,
            },
            "frank": {
                "level": 15,
                "total_score": 8359,
                "sessions_played": 85,
                "favorite_mode": "competitive",
                "achievements_count": 1,
            },
            "Sergio": {
                "level": 69,
                "total_score": 424242,
                "sessions_played": 1000000000,
                "favorite_mode": "competitive",
                "achievements_count": 1,
            },
        },
        "sessions": [
            {
                "player": "bob",
                "duration_minutes": 94,
                "score": 1831,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "bob",
                "duration_minutes": 32,
                "score": 1478,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "diana",
                "duration_minutes": 17,
                "score": 1570,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "alice",
                "duration_minutes": 98,
                "score": 1981,
                "mode": "ranked",
                "completed": True,
            },
            {
                "player": "diana",
                "duration_minutes": 15,
                "score": 2361,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "eve",
                "duration_minutes": 29,
                "score": 2985,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "frank",
                "duration_minutes": 34,
                "score": 1285,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "alice",
                "duration_minutes": 53,
                "score": 1238,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "bob",
                "duration_minutes": 52,
                "score": 1555,
                "mode": "casual",
                "completed": False,
            },
            {
                "player": "frank",
                "duration_minutes": 92,
                "score": 2754,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "eve",
                "duration_minutes": 98,
                "score": 1102,
                "mode": "casual",
                "completed": False,
            },
            {
                "player": "diana",
                "duration_minutes": 39,
                "score": 2721,
                "mode": "ranked",
                "completed": True,
            },
            {
                "player": "frank",
                "duration_minutes": 46,
                "score": 329,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "charlie",
                "duration_minutes": 56,
                "score": 1196,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "eve",
                "duration_minutes": 117,
                "score": 1388,
                "mode": "casual",
                "completed": False,
            },
            {
                "player": "diana",
                "duration_minutes": 118,
                "score": 2733,
                "mode": "competitive",
                "completed": True,
            },
            {
                "player": "charlie",
                "duration_minutes": 22,
                "score": 1110,
                "mode": "ranked",
                "completed": False,
            },
            {
                "player": "frank",
                "duration_minutes": 79,
                "score": 1854,
                "mode": "ranked",
                "completed": False,
            },
            {
                "player": "charlie",
                "duration_minutes": 33,
                "score": 666,
                "mode": "ranked",
                "completed": False,
            },
            {
                "player": "alice",
                "duration_minutes": 101,
                "score": 292,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "frank",
                "duration_minutes": 25,
                "score": 2887,
                "mode": "competitive",
                "completed": True,
            },
            {
                "player": "diana",
                "duration_minutes": 53,
                "score": 2540,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "eve",
                "duration_minutes": 115,
                "score": 147,
                "mode": "ranked",
                "completed": True,
            },
            {
                "player": "frank",
                "duration_minutes": 118,
                "score": 2299,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "alice",
                "duration_minutes": 42,
                "score": 1880,
                "mode": "casual",
                "completed": False,
            },
            {
                "player": "alice",
                "duration_minutes": 97,
                "score": 1178,
                "mode": "ranked",
                "completed": True,
            },
            {
                "player": "eve",
                "duration_minutes": 18,
                "score": 2661,
                "mode": "competitive",
                "completed": True,
            },
            {
                "player": "bob",
                "duration_minutes": 52,
                "score": 761,
                "mode": "ranked",
                "completed": True,
            },
            {
                "player": "eve",
                "duration_minutes": 46,
                "score": 2101,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "charlie",
                "duration_minutes": 117,
                "score": 1359,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "Sergio",
                "duration_minutes": 4269,
                "score": 6942,
                "mode": "competitive",
                "completed": True,
            },
        ],
        "game_modes": ["casual", "competitive", "ranked"],
        "achievements": [
            "first_blood",
            "level_master",
            "speed_runner",
            "treasure_seeker",
            "boss_hunter",
            "pixel_perfect",
            "combo_king",
            "explorer",
        ],
    }
    players: dict[str, dict[str, Any]] = data["players"]
    sessions: list[dict[str, Any]] = data["sessions"]
    game_modes = set(data["game_modes"])
    achievements = set(data["achievements"])
    '''
    For each players, update total score with the acore of each sessions.
    '''
    for session in sessions:
        session["achievement"] = random.choice(list(achievements))
        session["region"] = random.choice(
            ["north", "east", "south", "west", "central", "planet Mars"])
        players[session["player"]]["total_score"] += session["score"]
    print("=== Game Analytics Dashboard ===")
    print("")
    print("=== List Comprehension Examples ===")
    '''
    The high scorers are players with a 12000 more score.
    '''
    high_scorers: list[str] = [p for p, d in players.items()
                               if d["total_score"] > 12000]
    print(f"High scorers (>12000): {high_scorers}")
    '''
    The doubles scores concern only the scores of the high scorers
    '''
    scores_doubled: list[int] = [players[p]["total_score"] * 2
                                 for p in high_scorers]
    print(f"Scores doubled: {scores_doubled}")
    '''Actives players are players with more than 300 minutes of duration play.
    '''
    active_players = [p for p in players
                      if sum(s["duration_minutes"]
                             for s in sessions
                             if s["player"] == p) > 300]
    print(f"Active players: {active_players}")
    print("")
    print("=== Dict Comprehension Examples ===")
    player_scores: dict[str, int] = {p: players[p]["total_score"]
                                     for p in players.keys()}
    print(f"Player scores: {player_scores}")
    '''
    Score categories : high >= 24000, medium >= 12000, low < 12000
    '''
    score_cat: dict[str, int] = {
        "hight": len([p for p in players
                      if players[p]["total_score"] >= 24000]),
        "medium": len([p for p in players
                       if 12000 >= players[p]["total_score"] < 24000]),
        "low": len([p for p in players
                    if players[p]["total_score"] < 12000])
    }
    print(f"Score categories: {score_cat}")
    achiev_count: dict[str, int] = {p: players[p]["achievements_count"]
                                    for p in players.keys()}
    print(f"Achievement counts: {achiev_count}")
    print("")
    print("=== Set Comprehension Examples ===")
    unique_players = {s["player"] for s in sessions}
    print(f"Unique players: {unique_players}")
    unique_achievements = {s["achievement"] for s in sessions}
    print(f"Unique achievements: {unique_achievements}")
    active_regions = {s["region"]
                      for s in sessions
                      if s["duration_minutes"] > 100}
    print(f"Active regions: {active_regions}")
    print(f"Game modes : {game_modes}")
    print("")
    print("=== Combined Analysis ===")
    print(f"Total players: {len(players)}")
    print(f"Total unique achievements: {len({s["achievement"]
                                             for s in sessions})}")
    average_score = round(sum(s["score"]
                              for s in sessions) / len(sessions), 1)
    print(f"Average score: {average_score}")
    player, data = max(players.items(), key=lambda p: p[1]["total_score"])
    print(f"Top performer: {player}", end=" ")
    print(f"({data["total_score"]} points,", end=" ")
    print(f"{data["achievements_count"]} achievements)")
    print("")


if __name__ == "__main__":
    analytics_dashboard()
