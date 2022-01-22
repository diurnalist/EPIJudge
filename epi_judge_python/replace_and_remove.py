import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    # Shift all the b's out
    wpos, num_a = 0, 0
    for i in range(size):
        if s[i] != "b":
            s[wpos] = s[i]
            wpos += 1
        if s[i] == "a":
            num_a += 1
    curpos = wpos - 1
    wpos += num_a - 1
    retsize = wpos + 1
    while curpos >= 0:
        if s[curpos] == "a":
            s[wpos - 1 : wpos + 1] = "dd"
            wpos -= 2
        else:
            s[wpos] = s[curpos]
            wpos -= 1
        curpos -= 1
    return retsize


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "replace_and_remove.py",
            "replace_and_remove.tsv",
            replace_and_remove_wrapper,
        )
    )
