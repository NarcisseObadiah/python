ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list[1] = "World!"
ft_tuple = ft_tuple[:1] + ("Germany!",)
ft_set.remove("tutu!")
ft_set.add("Heilbronn!")
ft_dict["Hello"] = "42 Heilbronn!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)


# ---------------- TEST ----------------
# python3.10 hello.py
# Expected:
# ['Hello', 'World!']
# ('Hello', 'France!')
# {'Hello', 'Paris!'}  # order may vary
# {'Hello': '42Paris!'}
# --------------------------------------
