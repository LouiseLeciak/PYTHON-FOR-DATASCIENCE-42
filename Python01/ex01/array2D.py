def slice_me(family: list, start: int, end: int) -> list:
    if not isinstance(family, list):
        raise TypeError("wrong type argument")
    for i in family:
        if not isinstance(i, list):
            raise TypeError("require a 2D list")
        if len(i) != len(family[0]):
            raise TypeError("require equal size list")
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("require an int as slicing index")
    
    print(f"My shape is : ({len(family)}, {len(family[0])})")
    family_sliced = family[start:end]
    print(f"My new shape is : ({len(family_sliced)}, {len(family_sliced[0])})")
    return family_sliced
