from test_framework import generic_test


def evaluate(expression: str) -> int:
    val = 0
    results = []
    for seq in expression.split(","):
        if seq == "-":
            results.append(-results.pop() + results.pop())
        elif seq == "+":
            results.append(results.pop() + results.pop())
        elif seq == "*":
            results.append(results.pop() * results.pop())
        elif seq == "/":
            results.append(int(1 / results.pop() * results.pop()))
        else:
            results.append(int(seq))
    return results.pop()


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", "evaluate_rpn.tsv", evaluate)
    )
