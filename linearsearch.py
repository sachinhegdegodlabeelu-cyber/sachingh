from typing import Iterable, List, Sequence, TypeVar, Optional

"""
linearsearch.py

Simple, well-typed linear search utilities for lists/iterables.

Functions:
- linear_search(arr, target) -> int
    Return the index of the first occurrence of target in arr, or -1 if not found.
- linear_search_all(arr, target) -> list[int]
    Return a list of all indices where target occurs in arr (empty if none).
"""


T = TypeVar("T")


def linear_search(arr: Sequence[T], target: T) -> int:
    """Return the index of the first occurrence of target in arr, or -1 if not found.

    Args:
        arr: A sequence (e.g., list or tuple) to search.
        target: The value to search for.

    Returns:
        Index of the first match, or -1 if no match is found.
    """
    if arr is None:
        raise TypeError("arr must be a sequence, got None")
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1


def linear_search_all(arr: Sequence[T], target: T) -> List[int]:
    """Return a list of indices of all occurrences of target in arr.

    Args:
        arr: A sequence to search.
        target: The value to search for.

    Returns:
        List of matching indices (may be empty).
    """
    if arr is None:
        raise TypeError("arr must be a sequence, got None")
    return [i for i, v in enumerate(arr) if v == target]


if __name__ == "__main__":
    # Basic usage examples
    sample = [3, 5, 2, 5, 7]
    print("sample:", sample)
    print("linear_search(sample, 5) ->", linear_search(sample, 5))       # expected 1
    print("linear_search(sample, 4) ->", linear_search(sample, 4))       # expected -1
    print("linear_search_all(sample, 5) ->", linear_search_all(sample, 5))  # expected [1, 3]