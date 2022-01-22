from typing import List

from test_framework import generic_test


def get_valid_ip_address(s: str) -> List[str]:
    valid = []

    def valid_qd(qd: str) -> bool:
        return qd and (not qd.startswith("0") or qd == "0") and int(qd) < 256

    for qd1_size in range(1, 4):
        qd1 = s[:qd1_size]
        if not valid_qd(qd1):
            continue

        for qd2_size in range(1, 4):
            qd2 = s[qd1_size : qd1_size + qd2_size]
            if not valid_qd(qd2):
                continue

            for qd3_size in range(1, 4):
                qd3 = s[qd1_size + qd2_size : qd1_size + qd2_size + qd3_size]
                if not valid_qd(qd3):
                    continue

                qd4 = s[qd1_size + qd2_size + qd3_size :]
                if not valid_qd(qd4):
                    continue

                valid.append(f"{qd1}.{qd2}.{qd3}.{qd4}")
    return valid


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "valid_ip_addresses.py",
            "valid_ip_addresses.tsv",
            get_valid_ip_address,
            comparator=comp,
        )
    )
