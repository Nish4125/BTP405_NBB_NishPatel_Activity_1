import matplotlib.pyplot as plt

def graphSnowfall(filename):
    with open(filename, 'r') as file:
        data = []
        for line in file:
            data.append(int(line.strip()))

    max_value = max(data)

    range_step = 10
    ranges = []
    for i in range(0, max_value + 1, range_step):
        ranges.append((i, i + range_step - 1))

    counts = []
    for _ in ranges:
        counts.append(0)

    for snowfall in data:
        for i in range(len(ranges)):
            low, high = ranges[i]
            if low <= snowfall <= high:
                counts[i] += 1
                break

    labels = []
    for low, high in ranges:
        labels.append(f"{low + 1}-{high + 1}")

    plt.bar(labels, counts)
    plt.title('Snowfall Accumulation')
    plt.xlabel('Snowfall Ranges (cm)')
    plt.ylabel('Occurrences')
    plt.tight_layout()
    plt.show()

graphSnowfall('snowfall.txt')
