def main():
    input_grid = read_input()
    string_to_find = "XMAS"
    xmas_count = 0

    all_directions = [
            (0, 1),  # horizontal right
            (0, -1),  # horizontal left
            (1, 0),  # vertical down
            (-1, 0),  # vertical up
            (1, 1),  # diagonal down-right
            (1, -1),  # diagonal down-left
            (-1, 1),  # diagonal up-right
            (-1, -1)  # diagonal up-left
        ]

    for x in range(len(input_grid)):
        for y in range(len(input_grid[0])):
            letter = input_grid[x][y]

            # search in the same direction
            for direction in all_directions:
                x_dir, y_dir = direction
                # See if we can traverse 4 letters in this direection without going off-grid
                if (0 <= x + 3 * x_dir < len(input_grid)) and (0 <= y + 3 * y_dir < len(input_grid[0])):
                    # we can traverse without going off-grid
                    iterator = iter(string_to_find)
                    if letter == next(iterator):
                        if input_grid[x + x_dir][y + y_dir] == next(iterator):
                            if input_grid[x + 2*x_dir][y + 2*y_dir] == next(iterator):
                                if input_grid[x + 3*x_dir][y + 3*y_dir] == next(iterator):
                                    print(f'DEBUG: {string_to_find} was found in letter (row={x}, col={y}) going in direction {direction}')
                                    xmas_count += 1
    print(f'Day 1: Number of {string_to_find} found in grid = {xmas_count}')


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
