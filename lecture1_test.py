from lecture1 import bruteforce, dict_find
from typing import List
import pytest

words = []
with open('file.txt', 'r', encoding='utf-8') as f:
    for l in f:
        if l[-1] == '\n':
            words.append(l[:-1])
        else:
            words.append(l)


@pytest.mark.parametrize("text, expected", [
    (["123", "2", "234"], [2, ("123", "234")]),
    (words, [6, ('JjA3python', 'pythonf')])
])
def test_bruteforce(text: List[str], expected: [int, (str, str)]):
    assert bruteforce(text)[0] == expected[0]
    assert bruteforce(text)[1] == expected[1]


@pytest.mark.parametrize("text, expected", [
    (["123", "2", "234"], [2, ("123", "234")]),
    (words, [6, ('JjA3python', 'pythonf')])
])
def test_dict(text: List[str], expected: [int, (str, str)]):
    assert dict_find(text)[0] == expected[0]
    assert dict_find(text)[1] == expected[1]
