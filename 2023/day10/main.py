from functools import reduce
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path + "/input.txt") as f:
    pipes = {
        (i, j): val
        for (i, line) in enumerate(f)
        for (j, val) in enumerate(line.strip())
    }
    valids = {
        ("n", "F"): "e",
        ("w", "F"): "s",
        ("e", "J"): "n",
        ("s", "J"): "w",
        ("e", "7"): "s",
        ("n", "7"): "w",
        ("w", "L"): "n",
        ("s", "L"): "e",
        ("n", "|"): "n",
        ("s", "|"): "s",
        ("w", "-"): "w",
        ("e", "-"): "e",
    }

    def next_index(index, direction):
        row, col = index
        if direction == "n":
            return row - 1, col
        if direction == "s":
            return row + 1, col
        if direction == "w":
            return row, col - 1
        if direction == "e":
            return row, col + 1

    def get_from_direction(dir):
        return {"n": "s", "e": "w", "s": "n", "w": "e"}.get(dir, None)

    def is_valid_direction(pipes, current_index, direction):
        return (
            valids.get((direction, pipes.get(next_index(current_index, direction))))
            is not None
        )

    def valid_directions(pipes, index, current_direction):
        next_directions = []
        for direction in filter(
            lambda d: d != get_from_direction(current_direction),
            ("n", "s", "w", "e"),
        ):
            if is_valid_direction(pipes, index, direction):
                next_directions.append(direction)

        return next_directions

    def dfs(pipes, start_index):
        stack = [(start_index, None, 0)]
        visited = {}

        while stack:
            current_index, current_direction, current_path_length = stack.pop()

            if current_index in visited:
                visited[current_index] = min(
                    current_path_length, visited[current_index]
                )
            else:
                visited[current_index] = current_path_length

            for direction in valid_directions(pipes, current_index, current_direction):
                next_idx = next_index(current_index, direction)
                if next_idx not in visited or visited[next_idx] > current_path_length:
                    stack.append((next_idx, direction, current_path_length + 1))

        furthest_point = max(visited, key=lambda k: visited[k])
        furthest_distance = visited[furthest_point]

        return furthest_distance

    start_index = [k for k, v in pipes.items() if v == "S"][0]
    longest_path = dfs(pipes, start_index)

    print("Longest path length:", longest_path)
