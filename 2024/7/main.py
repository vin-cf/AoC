import cProfile
import time


def evaluate_with_recursion(numbers, target, index=0, current_value=0, memo=None):
    if index == len(numbers):
        return current_value == target

    # Initialize first number
    if index == 0:
        result = evaluate_with_recursion(numbers, target, index + 1, numbers[index], memo)
        return result

    if evaluate_with_recursion(numbers, target, index + 1, current_value + numbers[index], memo):
        return target

    # Try multiplying the current number
    if evaluate_with_recursion(numbers, target, index + 1, current_value * numbers[index], memo):
        return target

    concatenated_number = int(str(current_value) + str(numbers[index]))
    if evaluate_with_recursion(numbers, target, index + 1, concatenated_number, memo):
        return target

    return 0  # No valid combination found


# Example usage
def read_input():
    input_equations = []

    with open('input.txt', 'r') as f:
        for line in f:
            line = line.rstrip('\n')
            result = int(line.split(':')[0]) # Extract the key (before the colon)
            numbers = [int(x) for x in line.split(' ')[1:]]
            input_equations.append((result, numbers))

    return input_equations

if __name__ == '__main__':
    input_data = read_input()
    result = 0

    profiler = cProfile.Profile()
    profiler.enable()
    start_time = time.perf_counter()

    for target, numbers in input_data:
        result += evaluate_with_recursion(numbers=numbers, target=target)
    print("Total Calibration Result:", result)

    end_time = time.perf_counter()
    print(f"Total runtime: {end_time - start_time:.4f} seconds")
    profiler.disable()
    profiler.print_stats(sort='time')  # Print profiling results