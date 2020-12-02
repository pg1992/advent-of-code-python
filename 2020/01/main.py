import requests


def find_pair(numbers, target=2020):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return numbers[i], numbers[j]
    return -1, -1


def find_trio(numbers, target=2020):
    for i in range(len(numbers)):
        a, b = find_pair(numbers[i + 1:], target - numbers[i])
        if a == -1:
            continue
        else:
            return numbers[i], a, b
    return -1, -1, -1


def main():
    url = 'https://adventofcode.com/2020/day/1/input'
    cookies = {
        'session': '53616c7465645f5fa6389f760f7d7bb9c79be4bae659382e852e600d6d1b0c39596a75f140b50dcf05bd47ab664d8cf3'
    }
    response = requests.get(url, cookies=cookies)
    numbers = [int(n) for n in response.text[:-1].split('\n')]

    a, b = find_pair(numbers)
    print(a * b)

    a, b, c = find_trio(numbers)
    print(a * b * c)


if __name__ == '__main__':
    main()
