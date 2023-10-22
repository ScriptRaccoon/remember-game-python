import os
import random
import time


def clear_console() -> None:
    clear_command = "cls" if os.name == "nt" else "clear"
    os.system(clear_command)


def get_amount() -> int:
    while True:
        amount_input = input("\nHow many numbers do you want to remember?\n")
        if amount_input.isnumeric() and amount_input != "0":
            return int(amount_input)
        print("A positive number is required for the amount.")


def get_random_numbers(amount: int) -> list[int]:
    return random.choices(range(0, 10), k=amount)


def print_numbers(numbers: list[int], duration: int = 1) -> None:
    clear_console()
    print("Get ready ...")
    time.sleep(2.5)
    clear_console()
    for n in numbers:
        print(n)
        time.sleep(duration)
        clear_console()


def get_answer() -> str:
    answer = input("Input the numbers that you just saw:\n")
    if " " in answer or "," in answer:
        print("\nHint: You don't have to use spaces or commas next time.")
    return answer.replace(" ", "").replace(",", "")


def evaluate(answer: str, random_numbers: list[int]) -> None:
    random_numbers_string = "".join(map(str, random_numbers))
    if random_numbers_string == answer:
        print("\nCorrect!")
    else:
        print("\nSorry, this is not correct. The correct numbers are:")
        print(random_numbers_string)


def main():
    clear_console()
    print("### Remember Game ###")
    while True:
        amount = get_amount()
        random_numbers = get_random_numbers(amount)
        print_numbers(random_numbers)
        answer = get_answer()
        evaluate(answer, random_numbers)


if __name__ == "__main__":
    main()
