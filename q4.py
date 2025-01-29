def stats_printer(func):
    def wrapper(numbers):
        print(f"Numbers: {numbers}")
        print(f"Count of Numbers: {len(numbers)}")
        print(f"Sum of Numbers: {sum(numbers)}")
        print(f"Average of Numbers: {sum(numbers) / len(numbers):.2f}")
        print(f"Maximum of Numbers: {max(numbers)}")
        return func(numbers)
    return wrapper

@stats_printer
def process_numbers(numbers):
    print("Processing the numbers...")

def read_file_and_process(filepath):
    with open(filepath, 'r') as file:
        for line in file:
            numbers = [float(num) for num in line.split()]
            process_numbers(numbers)

#
read_file_and_process('numbers.txt')




