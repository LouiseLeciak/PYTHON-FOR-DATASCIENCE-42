def all_thing_is_obj(object: any) -> int:
    # to avoid doing if elif elif elif i'm using a dict
    types = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict"
    }

    #checking if the input is a string, if so then add is in the kitchen
    if type(object) is str:
        print(object + " is in the kitchen")
    else:
        # recuperer le nom de mon objet dans le dict
        obj_type_name = types.get(type(object))
        if obj_type_name:
            print(f"{obj_type_name} : {type(object)}")
        else:
            print("Type not found")

    return 42
