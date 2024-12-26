from itertools import cycle


def main():

    directions = {
        'U': (-1, 0),  # up
        'R': (0, 1),   # right
        'D': (1, 0),   # down
        'L': (0, -1)   # left
    }
    directions_cycle = cycle(directions)
    starting_dir = '^'

    x_dir, y_dir = 0, 0
    lab_map = read_input()
    x, y = (0, 0)

    for r, row in enumerate(lab_map):
        for c, char in enumerate(row):
            if char == '^':
                x, y = (r, c)
    traversed_coordinates = []

    # move
    iterator = iter(directions)
    if starting_dir == '^':
        x_dir, y_dir = directions['U']

    # See if we can traverse in this direction without going off-grid
    # or hitting an obstacle denoted by '#'
    while (0 <= x + x_dir < len(lab_map)) and (0 <= y + y_dir < len(lab_map[0])):
        if not can_traverse(x, y, x_dir, y_dir, lab_map, traversed_coordinates):
            # the guard turns 90 degrees to the right
            x_dir, y_dir = directions[next(directions_cycle)]
            can_traverse(x, y, x_dir, y_dir, lab_map, traversed_coordinates)
        else:
            # the guard moves in the given direction specified by x_dir, y_dir
            traversed_coordinates.append((x, y))
            x, y = (x + x_dir, y + y_dir)

    print(f'DEBUG: The guard traversed the following coordinates: {traversed_coordinates}')
    print(f'DEBUG: The guard ended up at coordinates: {x, y}')
    print(f'Uniquely traversed spaces subtracting duplicates: {len(set(traversed_coordinates)) + 1}')


def can_traverse(x, y, x_dir, y_dir, lab_map, traversed_coordinates):
    if lab_map[x + x_dir][y + y_dir] != '#':
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
    main()
