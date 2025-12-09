menu = ['masala chai', "Iced lemon tea", "Green tea","Iced peach tea", "Ginger chai"]

iced_tea = [tea for tea in menu if "Iced" in tea]

print(iced_tea)

iced_tea_len=[my_tea for my_tea in menu if len(my_tea) > 12]
print(iced_tea_len)