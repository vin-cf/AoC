from typing import List
import itertools


def main():
    puzzle_input = read_input()
    # puzzle_input = [['1', '6', '2', '3', '4'],
    #                 ['7', '6', '4', '2', '1'],
    #                 ['1', '2', '7', '8', '9'],
    #                 ['9', '7', '6', '2', '1'],
    #                 ['1', '3', '2', '4', '5'],
    #                 ['8', '6', '4', '4', '1'],
    #                 ['1', '3', '6', '7', '9']]
    safe_sum = process(puzzle_input)
    print(f'Day 1 answer: {safe_sum}')
    pd_safe_sum = process_pd(puzzle_input)
    print(f'Day 2 answer: {pd_safe_sum}')


def _to_int(string_list: List[str]):
    return list(map(int, string_list))


def _is_all_ascending(report: List[str]):
    comparison_list = list(zip(_to_int(report), _to_int(report[1:])))
    result = all([((x[0] < x[1]) and (x[1] - x[0] <= 3)) for x in comparison_list])
    return result


def _is_all_ascending_pd(report: List[str]):  # problem dampener
    if _is_all_ascending(report):
        return True
    combinations = itertools.combinations(report, len(report)-1)
    for combination in combinations:
        if _is_all_ascending(combination):
            return True
    return False


def _is_all_descending(report: List[str]):
    comparison_list = list(zip(_to_int(report), _to_int(report[1:])))
    result = all([((x[0] > x[1]) and (x[0] - x[1] <= 3)) for x in comparison_list])
    return result


def _is_all_descending_pd(report: List[str]):
    if _is_all_descending(report):
        return True
    combinations = itertools.combinations(report, len(report) - 1)
    for combination in combinations:
        if _is_all_descending(combination):
            return True
    return False


def process(puzzle_input: List):
    safe_count: int = 0
    safe_lists = []  # debug
    for report in puzzle_input:
        if _is_all_ascending(report) or _is_all_descending(report):
            safe_count += 1
            safe_lists.append(report)

    return safe_count


def process_pd(puzzle_input: List):
    safe_count: int = 0
    safe_lists = []  # debug
    for report in puzzle_input:
        if (_is_all_ascending_pd(report)
                or _is_all_descending_pd(report)):
            safe_count += 1
            # safe_lists.append(report)

    return safe_count


def read_input():
    with open('input.txt', 'r') as f:
        lines = [line.strip().split() for line in f.readlines()]
        return lines


if __name__ == '__main__':
    main()
