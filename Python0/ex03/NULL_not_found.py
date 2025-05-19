def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: {object} <class '{type(object).__name__}'>")
        return 0
    elif isinstance(object, float) and object != object:
        print(f"Cheese: {object} <class '{type(object).__name__}'>")
        return 0
    elif object is False:
        print(f"Fake: {object} <class '{type(object).__name__}'>")
        return 0
    elif object == 0:
        print(f"Zero: {object} <class '{type(object).__name__}'>")
        return 0
    elif object == '': #oblige == pour une chaine vide
        print(f"Empty: {object} <class '{type(object).__name__}'>")
        return 0
    print("Type not Found")
    return 1