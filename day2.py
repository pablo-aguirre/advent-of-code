def part1():
    with open("input/day2.1.txt", "r") as file:
        safe_counter = 0

        for line in file:
            numbers = [int(n) for n in line.split()]
            if is_safe(numbers):
                safe_counter += 1
    return safe_counter


def part2():
    with open("input/day2.2.txt", "r") as file:
        safe_counter = 0

        for line in file:
            numbers = [int(n) for n in line.split()]
            safe = is_safe(numbers)
            if safe:
                safe_counter += 1
            else:
                for i in range(len(numbers)):
                    if is_safe(numbers[:i] + numbers[i + 1:]):
                        safe_counter += 1
                        break
    return safe_counter


def is_safe(numbers):
    prev = 0
    levels = 0
    for i in range(1, len(numbers)):
        actual = numbers[i] - numbers[i - 1]
        if not actual * prev >= 0 or abs(numbers[i] - numbers[i - 1]) not in range(1, 4):
            break

        prev = actual
        levels += 1

    return levels == len(numbers) - 1


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
