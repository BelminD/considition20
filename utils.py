from collections import defaultdict


def best_residence_location(state):
    scores = defaultdict(int)
    available = available_map_slots(state)
    for x1, y1 in available:
        scores[(x1, y1)] = 0
        for x2 in range(len(state.map)):
            for y2 in range(len(state.map)):
                if manhattan_distance(x1, y1, x2, y2) > 0 and state.map[x2][y2] in [
                    0,
                    3,
                ]:
                    scores[(x1, y1)] += 1 / manhattan_distance(x1, y1, x2, y2)
    if not scores:
        return (-1, -1)
    return max(scores, key=lambda x: scores[x])  # Key with max value


def best_utility_location(state):
    scores = defaultdict(int)
    available = available_map_slots(state)
    for x1, y1 in available:
        scores[(x1, y1)] = 0
        for x2 in range(len(state.map)):
            for y2 in range(len(state.map)):
                if manhattan_distance(x1, y1, x2, y2) > 0 and state.map[x2][y2] in [
                    0,
                    2,
                ]:
                    scores[(x1, y1)] += 1 / manhattan_distance(x1, y1, x2, y2)
                if manhattan_distance(x1, y1, x2, y2) <= 3 and state.map[x2][y2] == 3:
                    scores[(x1, y1)] = -1e5
    if not scores:
        return (-1, -1)
    return max(scores, key=lambda x: scores[x])  # Key with max value


def available_map_slots(state):
    # Go through the map and find available slots
    return [
        (i, j)
        for i in range(len(state.map))
        for j in range(len(state.map))
        if state.map[i][j] == 0
    ]


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)
