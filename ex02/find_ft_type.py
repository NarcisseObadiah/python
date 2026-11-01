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


def main() -> None:
    """
    Running this file alone must do nothing.
    """
    return


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass

# ---------------- TEST ----------------
# python3.10 find_ft_type.py
# (should print nothing)

# python3.10 -c "from find_ft_type import all_thing_is_obj as f; \
# ft_list=['Hello','tata!']; ft_tuple=('Hello','toto!'); \
# ft_set={'Hello','tutu!'}; ft_dict={'Hello':'titi!'}; \
# f(ft_list); f(ft_tuple); f(ft_set); f(ft_dict); \
# f('Brian'); f('Toto'); print(f(10))"

# Expected:
# List : <class 'list'>
# Tuple : <class 'tuple'>
# Set : <class 'set'>
# Dict : <class 'dict'>
# Brian is in the kitchen : <class 'str'>
# Toto is in the kitchen : <class 'str'>
# Type not found
# 42
# # --------------------------------------
