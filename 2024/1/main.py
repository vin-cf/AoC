from typing import List


def main():
    puzzle_input = read_input()
    print(puzzle_input)
    p1_answer = process(puzzle_input)
    print(f'Part 1 answer: {p1_answer}')

    puzzle_input = read_input()
    p2_answer = similarity(puzzle_input)
    print(f'Part 2 answer: {p2_answer}')


def similarity(puzzle_input: (List, List)):
    similarity_list = []

    left_list, right_list = puzzle_input

    for base_number in left_list:
        multiplier = right_list.count(base_number)
        similarity_list.append(base_number * multiplier)

    return sum(similarity_list)


def read_input():
    # read input from input.txt in the same directory as this file
    # the inputs are listed as such:
    # list 1   list 2
    # 1   1
    # 4   5
    # 5   6
    # returns [left list], [right list] [1,4,5],[1,5,6]
    try:
        with open('input.txt', 'r') as f:
            lines = [line.strip().split() for line in f.readlines()]
            left_list = [int(line[0]) for line in lines]
            right_list = [int(line[1]) for line in lines]
            return left_list, right_list

    except FileNotFoundError:
        print("Error: The file 'input.txt' was not found.")
        return None

    except Exception as e:
        print(f"An error occurred while reading the input file: {e}")
        return None


def process(puzzle_input):
    left_list, right_list = puzzle_input

    distance = 0

    while left_list or right_list:
        left_smallest = min(left_list)
        right_smallest = min(right_list)
        distance += abs(left_smallest - right_smallest)
        left_list.remove(left_smallest)
        right_list.remove(right_smallest)

    return distance


if __name__ == '__main__':
    main()
