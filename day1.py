def part1():
    with open('input/day1.1.txt', 'r') as file:
        first = []
        second = []

        for line in file:
            n1, n2 = line.split()
            first.append(int(n1))
            second.append(int(n2))

        total_distance = 0
        while len(first) != 0:
            minimum1 = min(first)
            minimum2 = min(second)
            total_distance += abs(minimum1 - minimum2)
            first.remove(minimum1)
            second.remove(minimum2)

    return total_distance

def part2():
    with open('input/day1.2.txt', 'r') as file:
        first = []
        second = []
        for line in file:
            n1, n2 = line.split()
            first.append(int(n1))
            second.append(int(n2))

        total_distance = 0
        for n1 in first:
            total_distance += second.count(n1) * n1
    return total_distance

if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
