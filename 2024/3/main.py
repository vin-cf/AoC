import re


def main():
    input="xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

    sequence_regex = re.compile(r'mul\(\d+,\d+\)')
    result = sequence_regex.findall(input)

    total_mul = 0
    for item in result:
        to_multiply = re.compile(r'\d+').findall(item)
        total_mul += int(to_multiply[0]) * int(to_multiply[1])

    print(r'Sum for day 1: {sum}')

    total_mul = 0
    
    # This regex handles the scenario where there may not be a do() after a don't()
    # This is not handled correctly by re.compile('don\'t\(\).*?do\(\)'
    # (?:do\(\)|$) is a non-capturing group that matches either do() or the end of the input.
    # This ensures that if there's no do() following a don't(), the regex will consume until the end of the input.
    corrupted_regex = re.compile(r"don't\(\).*?(?:do\(\)|$)", flags=re.DOTALL)
    uncorrupted_input = re.sub(corrupted_regex, "foo", input)

    sequence_regex = re.compile(r'mul\(\d+,\d+\)')
    result = sequence_regex.findall(uncorrupted_input)
    for item in result:
        i, j = map(int, re.compile(r'\d+').findall(item))
        total_mul += i * j

    print(f"Sum for day 2: {total_mul}")


if __name__ == '__main__':
    main()
