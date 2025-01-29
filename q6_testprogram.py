import random
import time
import matplotlib.pyplot as plt
from q6_sort import Vehicle, selection_sort, bubble_sort, merge_sort


def generate_vehicles(num=5):
    manufacturers = ["Nissan", "Chevrolet", "Kia", "Mazda", "Hyundai"]
    models = ["X100", "CivicPro", "RangerX", "Storm", "Speedster"]
    types = ["Hatchback", "Convertible", "Pickup", "Minivan", "Coupe"]
    vehicles = []

    for _ in range(num):
        manufacturer = random.choice(manufacturers)
        model = random.choice(models)
        vehicle_type = random.choice(types)
        cost = random.randint(15000, 60000)
        mileage = random.randint(5000, 250000)
        vehicles.append(Vehicle(manufacturer, model, vehicle_type, cost, mileage))

    return vehicles


def measure_time_and_print(vehicles, key, sort_function):
    vehicles_copy = vehicles[:]  # Copy to avoid modifying the original list
    start_time = time.time()
    sorted_vehicles = sort_function(vehicles_copy, key)
    end_time = time.time()

    print(f"\nSorted by {key} using {sort_function.__name__}:")
    for v in sorted_vehicles:
        print(v)

    return end_time - start_time


def plot_results(sorting_algorithms, execution_times):
    plt.figure(figsize=(8, 5))

    for sort_name, times in execution_times.items():
        plt.bar(sort_name, times, color='skyblue', edgecolor='black')

    plt.xlabel("Sorting Algorithm")
    plt.ylabel("Time Taken (seconds)")
    plt.title("Sorting Performance")
    plt.show()


def main():
    sorting_field = "cost"  # Fixed sorting field
    vehicles = generate_vehicles(5)  # Generate only 5 vehicles

    execution_times = {
        "Selection Sort": measure_time_and_print(vehicles, sorting_field, selection_sort),
        "Bubble Sort": measure_time_and_print(vehicles, sorting_field, bubble_sort),
        "Merge Sort": measure_time_and_print(vehicles, sorting_field, merge_sort),
    }

    plot_results(execution_times.keys(), execution_times)


if __name__ == "__main__":
    main()
