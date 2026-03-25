#!/usr/bin/env python3

import sys


def score_analytics(argv: list[str]) -> None:
    scores: list[int] = []
    print("=== Player Score Analytics ===")
    no_score: bool = True
    i: int = 0
    for i in range(1, argv.__len__()):
        try:
            scores.append(int(argv[i]))
            no_score = False
        except ValueError:
            print(f"Invalid parameter: ’{argv[i]}’")
    if no_score:
        print("No scores provided.", end=" ")
        print("Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        print(f"Scores processed: {scores}")
        print(f"Total players: {scores.__len__()}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    score_analytics(sys.argv)
