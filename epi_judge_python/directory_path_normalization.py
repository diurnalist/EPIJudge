from test_framework import generic_test


def shortest_equivalent_path(path: str) -> str:
    shortest = []
    if path.startswith("/"):
        shortest.append("")
    for part in path.split("/"):
        if part == "..":
            if not shortest or shortest[-1] == "..":
                shortest.append(part)
            else:
                shortest.pop()
        elif part and part != ".":
            shortest.append(part)
    return "/".join(shortest).rstrip("/") or "/"


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "directory_path_normalization.py",
            "directory_path_normalization.tsv",
            shortest_equivalent_path,
        )
    )
