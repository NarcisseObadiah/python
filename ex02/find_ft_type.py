def all_thing_is_obj(object: any) -> int:
    """Print the type of the given object and return 42."""
    kind = type(object)
    if kind is list:
        print("List :", kind)
    elif kind is tuple:
        print("Tuple :", kind)
    elif kind is set:
        print("Set :", kind)
    elif kind is dict:
        print("Dict :", kind)
    elif kind is str and object in ("Brian", "Toto"):
        print(f"{object} is in the kitchen :", kind)
    else:
        print("Type not found")
    return 42