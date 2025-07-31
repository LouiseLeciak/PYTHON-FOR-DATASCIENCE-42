ft_list     = ["Hello", "tata!"]
ft_tuple    = ("Hello", "toto!")
ft_set      = {"Hello", "tutu!"}
ft_dict     = {"Hello" : "titi!"}

#We modify the tata in world
ft_list[1] = "World"
#Since you cant modify a value inside a tuple we make a new one
ft_tuple = ("Hello", "France!")
#There's no real order in a set, so we just modify tutu
ft_set = {"Hello", "Paris!"}
#We just need to change the value of the Hello key
ft_dict["Hello"] = "42Paris!"



print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)