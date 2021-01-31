import itertools

from search import _all_bytestrings


def test_all_bytestrings():
    for secret in _all_bytestrings():
        print(secret)


if __name__ == "__main__":
    i = 0
    for length in itertools.count():
        print(length)
        i += 1
        if i > 20:
            break
