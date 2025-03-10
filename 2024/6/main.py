from itertools import cycle
from concurrent.futures import ProcessPoolExecutor

import cProfile
import time

def main():
    lab_map = read_input()
    x, y = (0, 0)
    directions = {
        'U': (-1, 0),  # up
        'R': (0, 1),   # right
        'D': (1, 0),   # down
        'L': (0, -1)   # left
    }
    successful_blocks = set()
    for r, row in enumerate(lab_map):
        for c, char in enumerate(row):
            if char == '^':
                x, y = (r, c)
                break
    print(f'DEBUG: The size of the map is: {len(lab_map)} x {len(lab_map[0])}')
    size_x = len(lab_map)
    size_y = len(lab_map[0])

    with ProcessPoolExecutor() as executor:
        futures = [
            executor.submit(traverse, x, y, lab_map, r, c, size_x, size_y, directions)
            for r, row in enumerate(lab_map)
            for c, char in enumerate(row)
            if char not in {'^', '#'}
        ]
        for future in futures:
            future.result()  # Ensure all tasks are complete

    print(f'DEBUG: The number of successful blocks is: {len(successful_blocks)}')

def traverse(x, y, lab_map, obstacle_x, obstacle_y, size_x, size_y, directions):
    traversed_coordinates = set()
    directions_cycle = cycle(directions)
    x_dir, y_dir = directions['U']

    # See if we can traverse in this direction without going off-grid
    # or hitting an obstacle denoted by '#'
    while (0 <= x + x_dir < size_x) and (0 <= y + y_dir < size_y):
        if (x, y, x_dir, y_dir) in traversed_coordinates:
            print(f'The guard is in a loop with obstacle at coordinates: {obstacle_x, obstacle_y}')
            return obstacle_x, obstacle_y
        if not can_traverse(x, y, x_dir, y_dir, lab_map, obstacle_x, obstacle_y):
            # the guard turns 90 degrees to the right
            x_dir, y_dir = directions[next(directions_cycle)]
            can_traverse(x, y, x_dir, y_dir, lab_map, obstacle_x, obstacle_y)
        else:
            # the guard moves in the given direction specified by x_dir, y_dir
            traversed_coordinates.add((x, y, x_dir, y_dir))
            x, y = (x + x_dir, y + y_dir)
    print(f'Obstacle at coordinates: {obstacle_x, obstacle_y} did not block the guard')

    # print(f'DEBUG: The guard traversed the following coordinates: {traversed_coordinates}')
    # print(f'DEBUG: The guard ended up at coordinates: {x, y}')
    # print(f'Uniquely traversed spaces subtracting duplicates: {len(set(traversed_coordinates)) + 1}')


def _has_duplicates(lst):
    return len(lst) != len(set(lst))

def can_traverse(x, y, x_dir, y_dir, lab_map, obstacle_x, obstacle_y):
    if lab_map[x + x_dir][y + y_dir] != '#' and (x + x_dir, y + y_dir) != (obstacle_x, obstacle_y):
        return True
    else:
        return False

def read_input():
    input_grid = []
    try:
        with open('input.txt', 'r') as f:
            for line in f:
                line = line.rstrip('\n')  # remove trailing newline
                input_grid.append(list(line))

    except FileNotFoundError:
        print("Error: The file 'input-test.txt' was not found.")
        return None

    except Exception as e:
        print(f"An error occurred while reading the input file: {e}")
        return None
    return input_grid


if __name__ == '__main__':
    profiler = cProfile.Profile()
    profiler.enable()
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(f"Total runtime: {end_time - start_time:.4f} seconds")
    profiler.disable()
    profiler.print_stats(sort='time')  # Print profiling results