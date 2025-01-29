def wordCount(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    word_lines = {}
    for line_number, line in enumerate(lines, start=1):
        words = line.split()
        for word in words:
            word = word.strip().lower()
            if word not in word_lines:
                word_lines[word] = []
            word_lines[word].append(line_number)

    return word_lines

result = wordCount('words.txt')
print(result)
