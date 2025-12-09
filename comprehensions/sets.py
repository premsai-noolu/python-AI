favourite_chais = ['masala chai', "Green tea", "masala chai","Green tea","Iced peach tea", "Ginger chai"]

unique_chais = {chai for chai in favourite_chais}

print(unique_chais)

recipes = {
    "masala chai" : ["ginger", "clove","cardmom"],
    "Elaichi chai": ["cardmom","milk"],
    "Spicy_chai": ["ginger","black_pepper"]
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
print(unique_spices)