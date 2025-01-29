class Vehicle:
    def __init__(self, manufacturer, model, vehicle_type, cost, mileage):
        self.manufacturer = manufacturer
        self.model = model
        self.vehicle_type = vehicle_type
        self.cost = cost
        self.mileage = mileage

    def __str__(self):
        return f"{self.manufacturer} {self.model} ({self.vehicle_type}) - Cost: ${self.cost}, Mileage: {self.mileage} km"


def selection_sort(vehicles, key):
    vehicles = vehicles[:]
    n = len(vehicles)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if key == "cost" and vehicles[j].cost < vehicles[min_index].cost:
                min_index = j
            elif key == "mileage" and vehicles[j].mileage < vehicles[min_index].mileage:
                min_index = j
            elif key == "manufacturer" and vehicles[j].manufacturer < vehicles[min_index].manufacturer:
                min_index = j
            elif key == "model" and vehicles[j].model < vehicles[min_index].model:
                min_index = j
            elif key == "vehicle_type" and vehicles[j].vehicle_type < vehicles[min_index].vehicle_type:
                min_index = j

        vehicles[i], vehicles[min_index] = vehicles[min_index], vehicles[i]

    return vehicles


def bubble_sort(vehicles, key):
    vehicles = vehicles[:]
    n = len(vehicles)

    for i in range(n - 1):
        for j in range(n - i - 1):
            swap = False
            if key == "cost" and vehicles[j].cost > vehicles[j + 1].cost:
                swap = True
            elif key == "mileage" and vehicles[j].mileage > vehicles[j + 1].mileage:
                swap = True
            elif key == "manufacturer" and vehicles[j].manufacturer > vehicles[j + 1].manufacturer:
                swap = True
            elif key == "model" and vehicles[j].model > vehicles[j + 1].model:
                swap = True
            elif key == "vehicle_type" and vehicles[j].vehicle_type > vehicles[j + 1].vehicle_type:
                swap = True

            if swap:
                vehicles[j], vehicles[j + 1] = vehicles[j + 1], vehicles[j]

    return vehicles


def merge_sort(vehicles, key):
    if len(vehicles) <= 1:
        return vehicles

    mid = len(vehicles) // 2
    left = merge_sort(vehicles[:mid], key)
    right = merge_sort(vehicles[mid:], key)

    return merge(left, right, key)


def merge(left, right, key):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if key == "cost":
            condition = left[i].cost <= right[j].cost
        elif key == "mileage":
            condition = left[i].mileage <= right[j].mileage
        elif key == "manufacturer":
            condition = left[i].manufacturer <= right[j].manufacturer
        elif key == "model":
            condition = left[i].model <= right[j].model
        elif key == "vehicle_type":
            condition = left[i].vehicle_type <= right[j].vehicle_type
        else:
            condition = False

        if condition:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

