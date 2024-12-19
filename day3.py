import re
from gc import enable


def part1():
    result = 0

    with open("input/day3.1.txt") as file:
        instructions = re.finditer(r'mul\(\d{1,3},\d{1,3}\)', file.read())

        for instruction in instructions:
            n1, n2 = re.search(r'(\d{1,3}),(\d{1,3})', instruction.group()).groups()
            result += int(n1) * int(n2)
    return result


def part2():
    result = 0

    with open("input/day3.2.txt") as file:
        do_regex = r'do\(\)'
        dont_regex = r'don\'t\(\)'
        mul_regex = r'mul\(\d{1,3},\d{1,3}\)'

        actual = file.read()

        while True:
            res = re.search(dont_regex, actual)
            if res:
                current = actual[:res.start()]
            else:
                current = actual

            for instruction in re.finditer(mul_regex, current):
                n1, n2 = re.search(r'(\d{1,3}),(\d{1,3})', instruction.group()).groups()
                result += int(n1) * int(n2)

            if res:
                current = actual[res.end():]
            else:
                break
            res2 = re.search(do_regex, current)
            if res2:
                actual = current[res2.start():]
            else:
                break
    return result


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
