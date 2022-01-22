import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s):
    def _rev(_s, i, j):
        while i < j:
            _s[i], _s[j] = _s[j], _s[i]
            i, j = i + 1, j - 1

    _rev(s, 0, len(s) - 1)

    i = 0
    while True:
        # Find next word boundary
        j = i
        while j < len(s) and s[j] != " ":
            j += 1

        _rev(s, i, j - 1)
        i = j + 1
        if j == len(s):
            break


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return "".join(s_copy)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "reverse_words.py", "reverse_words.tsv", reverse_words_wrapper
        )
    )
