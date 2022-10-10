def the_recipe():
    cook_book = {}
    with open('recipes.txt', 'r', encoding='utf-8') as recipes_list:
        for line in recipes_list:
            dish_name = line.strip()
            cb = {dish_name: []}
            ingredient_quality = recipes_list.readline()
            for i in range(int(ingredient_quality)):
                dis = recipes_list.readline()
                ingredient_name, quantity, measure = dis.split(' | ')
                recipes = {'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure.strip()}
                cb[dish_name].append(recipes)
            recipes_list.readline()
            cook_book.update(cb)

    def get_shop_list_by_dishes(dishes, person_count):
        for recipe in cook_book.get(dishes[0]):
            recipe['quantity'] *= person_count
            print(recipe)
        for recipe in cook_book.get(dishes[1]):
            recipe['quantity'] *= person_count
            print(recipe)

    return get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 5)


the_recipe()
