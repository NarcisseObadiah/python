def NULL_not_found(object: any) -> int:
    """Print the type of a "Null" like object.

    Return 0 if the object is one of the NULL types, 1 otherwise.
    """
    kind = type(object)
    if object is None:
        print("Nothing:", object, kind)
    elif kind is float and object != object:
        print("Cheese:", object, kind)
    elif kind is int and object == 0:
        print("Zero:", object, kind)
    elif kind is str and object == "":
        print("Empty:", kind)
    elif kind is bool and object is False:
        print("Fake:", object, kind)
    else:
        print("Type not Found")
        return 1
    return 0