def NULL_not_found(object: any) -> int:
    try:
        if object is None:
            print("Nothing: None <class 'NoneType'>")
        elif type(object) == float and object != object:  # on verifie nan avec object != object parce que nan != nan
            print("Cheese: nan <class 'float'>")
        elif object == 0 and type(object) == int:
            print("Zero: 0 <class 'int'>")
        elif object == "" and type(object) == str:
            print("Empty: <class 'str'>")
        elif object is False:
            print("Fake: False <class 'bool'>")
        else:
            print("Type not Found")
            return 1
        return 0
    except Exception:
        return 1
