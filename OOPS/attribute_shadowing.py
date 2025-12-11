class chai:
    temperature="hot"
    strength="strong"

cutting = chai()
print(cutting.temperature)

cutting.temperature = "Mild"
cutting.cup = "small"

print("after changing",cutting.temperature)
print("cutting cup size",cutting.cup)
print("Direct look into the class", chai.temperature)

del cutting.temperature
del cutting.cup

print(cutting.temperature)
print(cutting.cup)

