#!/usr/bin/env python3

import sys
import math


class DetailsError(Exception):
    """Base class for details-related errors."""
    def __init__(self, e: Exception) -> None:
        super().__init__(f"Error details - Type: {type(e).__name__}, " +
                         f"Args: {e.args}")


class CoordError(Exception):
    """Base class for coordinates-related errors."""
    def __init__(self, msg: str = "coordinates must be 3 integers") -> None:
        super().__init__(msg)


class ParseError(CoordError):
    """Base class for parsing-related errors."""
    def __init__(self, e: Exception) -> None:
        super().__init__(f"Error parsing coordinates: {e.__str__()}")


def dist_3d(
        p1: tuple[float, float, float],
        p2: tuple[float, float, float]
        ) -> float:
    d = math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 + (p2[2]-p1[2])**2)
    return (d)


def disp_dist(
        p1: tuple[float, float, float],
        p2: tuple[float, float, float]
        ) -> None:
    print(f"Distance between {p1} and {p2}: {round(dist_3d(p1, p2), 2)}")


def list_argv(argv: list[str]) -> str:
    la: str = ""
    for i in range(1, argv.__len__()):
        la += argv[i] + " "
    la = la.rstrip(" ")
    if argv.__len__() == 2:
        la = "\"" + la + "\""
    return (la)


def parse_coordinate(argv: list[str]) -> tuple[float, float, float]:
    p: tuple[float, float, float]
    if argv.__len__() == 4:
        p = (float(argv[1]), float(argv[2]), float(argv[3]))
    elif argv.__len__() == 2:
        p = (float(argv[1].split(",")[0]),
             float(argv[1].split(",")[1]),
             float(argv[1].split(",")[2]))
    else:
        raise CoordError()
    return (p)


def create_3d_pos(
        o: tuple[float, float, float],
        p: tuple[float, float, float]
        ) -> None:
    print(f"Position created: {p}")
    disp_dist(o, p)
    print("")


def parse_3d_position(o: tuple[float, float, float], argv: list[str]) -> None:
    try:
        p: tuple[float, float, float]
        p = parse_coordinate(argv)
    except ValueError as e:
        print(f"Parsing invalid coordinates: {list_argv(argv)}")
        print(ParseError(e))
        print(DetailsError(e))
    except CoordError as e:
        print(e)
    else:
        print(f"Parsing coordinates: {list_argv(argv)}")
        disp_dist(o, p)
    finally:
        print("")


def get_player_pos() -> tuple[float, float, float]:
    coord_float: list[float] = []
    coord_str: list[str] = []
    c: str = ""
    while not coord_float:
        try:
            coord_str = (input(
                "Enter new coordinates as floats in format ’x,y,z’:"
                )).split(sep=",", maxsplit=2)
            if len(coord_str) != 3:
                raise CoordError()
            for c in coord_str:
                coord_float.append(float(c))
        except CoordError:
            print("Invalid syntax")
            coord_float.clear()
        except ValueError:
            print(f"Error on parameter '{c}':", end=" ")
            print(f"could not convert string to float: '{c}'")
            coord_float.clear()
    return (coord_float[0], coord_float[1], coord_float[2])


def coordinate_system(argv: list[str]) -> None:
    coord_start: tuple[float, float, float]
    coord_end: tuple[float, float, float]
    print("=== Game Coordinate System ===")
    print("")
    print("Get a first set of coordinates")
    coord_start = get_player_pos()
    print(f"Got a first tuple: {coord_start}")
    x, y, z = coord_start
    print(f"Coordinates: X={x}, Y={y}, Z={z}")
    print(f"Distance to center: {round(dist_3d((0, 0, 0), coord_start), 4)}")
    print("")
    print("Get a second set of coordinates")
    coord_end = get_player_pos()
    print("Distance between the 2 sets of coordinates:", end=" ")
    print(round(dist_3d(coord_start, coord_end), 4))
    print("")
    print("\n=== OLD EXERCICE ===\n")
    create_3d_pos((0, 0, 0), (10, 20, 5))
    parse_3d_position((0, 0, 0), argv)
    parse_3d_position((0, 0, 0), ["test", "123", "456", "789"])
    parse_3d_position((0, 0, 0), ["test", "abc,def,ghi"])
    print("Unpacking demonstration:")
    print("Player at x=3, y=4, z=0")
    x, y, z = (3, 4, 0)
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    coordinate_system(sys.argv)
