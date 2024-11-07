def cakes(recipe, available):
    keys_recipe = list(recipe.keys())
    generator = [available[keys_recipe[i]] // recipe[keys_recipe[i]] if keys_recipe[i] in list(available.keys()) else None for i in range(len(keys_recipe))]
    if None in generator:
        return 0
    return min(generator)



dt = cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200})
print(dt)