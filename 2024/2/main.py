from typing import List


def main():
    puzzle_input = read_input()
    safe_sum = process(puzzle_input)
    print(f'Day 1 answer: {safe_sum}')


def _to_int(string_list: List[str]):
    return list(map(int, string_list))


def _is_all_ascending(report: List[str]):
    comparison_list = list(zip(_to_int(report), _to_int(report[1:])))
    return all([((x[0] < x[1]) and (x[1] - x[0] <= 3)) for x in comparison_list])


def _is_all_descending(report: List[str]):
    comparison_list = list(zip(_to_int(report), _to_int(report[1:])))
    return all([((x[0] > x[1]) and (x[0] - x[1] <= 3)) for x in comparison_list])


def process(puzzle_input: List):
    safe_count: int = 0
    safe_lists = []  # debug
    for report in puzzle_input:
        if _is_all_ascending(report) or _is_all_descending(report):
            safe_count += 1
            safe_lists.append(report)

    return safe_count


def read_input():
    try:
        with open('input.txt', 'r') as f:
            lines = [line.strip().split() for line in f.readlines()]
            return lines

    except FileNotFoundError:
        print("Error: The file 'input.txt' was not found.")
        return None

    except Exception as e:
        print(f"An error occurred while reading the input file: {e}")
        return None


if __name__ == '__main__':
    main()
