def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    """
    Take the weight and the height and return the bmi value
    """
    if (len(height) != len(weight)):
        raise ValueError("AssertionError: different size of lists")

    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise TypeError("AssertionError: should be int or float")

    result = []
    for h, w in zip(height, weight):
        result.append(w / (h*h))
    return result


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    if not isinstance(limit, int):
        raise TypeError("AssertionError: limit must be an integer")

    result = []
    for b in bmi:
        if not isinstance(b, (int, float)):
            raise TypeError("AssertionError: should be int or float")
        if b > limit:
            result.append(True)
        else:
            result.append(False)
    return result
