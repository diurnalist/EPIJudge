from test_framework import generic_test


def look_and_say(n: int) -> str:
    nxt = "1"
    for i in range(n - 1):
        cur = nxt
        chr = cur[0]
        nxt = ""
        count = 1
        for j in range(len(cur) - 1):
            if cur[j] != cur[j + 1]:
                nxt += f"{count}{cur[j]}"
                count = 1
                chr = cur[j + 1]
            else:
                count += 1
        nxt += f"{count}{chr[-1]}"
    return nxt


import itertools


def look_and_say_groupby(n: int) -> str:
    s = "1"
    for _ in range(n - 1):
        s = "".join(f"{len(list(grp))}{k}" for k, grp in itertools.groupby(s))
    return s


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "look_and_say_groupby.py", "look_and_say.tsv", look_and_say
        )
    )
