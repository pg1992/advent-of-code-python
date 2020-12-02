import requests


def naive_policy(policy, password):
    letter_range, letter = policy.split(' ')
    min_letter, max_letter = letter_range.split('-')

    min_letter = int(min_letter)
    max_letter = int(max_letter)

    before = len(password)
    after = len(password.replace(letter, ''))

    return min_letter <= before - after <= max_letter


def real_policy(policy, password):
    letter_range, letter = policy.split(' ')
    min_letter, max_letter = letter_range.split('-')

    min_letter = int(min_letter)
    max_letter = int(max_letter)

    first = password[min_letter - 1] == letter
    second = password[max_letter - 1] == letter

    return first + second == 1


def total_of_valid_passwords(password_db):
    count_naive = 0
    count_real = 0

    for entry in password_db.split('\n'):
        policy, password = entry.split(': ')

        count_naive += naive_policy(policy, password)
        count_real += real_policy(policy, password)

    return count_naive, count_real


def get_password_db(url, session):
    cookies = {
        'session': session
    }

    response = requests.get(url, cookies=cookies)
    password_db = response.text.rstrip()

    return password_db


def main():
    url = 'https://adventofcode.com/2020/day/2/input'
    session = '53616c7465645f5fa6389f760f7d7bb9c79be4bae659382e852e600d6d1b0c39596a75f140b50dcf05bd47ab664d8cf3'
    password_db = get_password_db(url, session)

    print(total_of_valid_passwords(password_db))


if __name__ == "__main__":
    main()
