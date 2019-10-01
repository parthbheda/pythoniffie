# assumes Python 3


def get_yn(prompt, yes_values=("y", "yes"), no_values=("n", "no")):
    """
    Prompt for a yes or no response;
    return True for yes or False for no
    """
    while True:
        response = input(prompt).strip().lower()
        if response in yes_values:
            return True
        elif response in no_values:
            return False


def get_int(prompt, lo=None, hi=None):
    """
    Prompt for a number,
    return as int
    """
    while True:
        try:
            value = int(input(prompt))
            if (lo is None or lo <= value) and (hi is None or value <= hi):
                return value
        except ValueError:
            pass


def get_one_of(prompt, values):
    """
    Prompt for a response in values,
    return response string
    """
    while True:
        value = input(prompt).strip().lower()
        if value in values:
            return value


def main():
    global attempt
    print(
        "Guessing Game\n"
        "\n"
        "Think of a number in [1..100],\n"
        "and I will try to guess it in no more than 7 tries.\n"
    )

    if get_yn("Are you ready? (y/n): "):
        lo, hi = 1, 100
        got_it = False
        for attempt in range(1, 8):
            guess = (lo + hi) // 2
            print("I guess {}!".format(guess))
            res = get_one_of("Was this [L]ow, [H]igh, or [C]orrect? ", 
            				{"l", "h", "c"})
            if res == "l":
                lo = guess + 1
            elif res == "h":
                hi = guess - 1
            else:  # correct!
                got_it = True
                break
            if lo > hi:
                break
        if got_it:
            print(f"Ha! Got it in {attempt} guesses!")
        else:
            print("Something smells in the state of Denmark...")
    else:
        print("Bye!")


if __name__ == "__main__":
    main()
