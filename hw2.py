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
        needed_ingr1 = {}
        needed_ingr2 = {}
        for recipe1 in cook_book.get(dishes[0]):
            n, q, m = recipe1.values()
            res = {n: {'quantity': int(q * person_count), 'measure': m}}
            needed_ingr1.update(res)
        for recipe2 in cook_book.get(dishes[1]):
            r, t, y = recipe2.values()
            ser = {r: {'quantity': int(t * person_count), 'measure': y}}
            needed_ingr2.update(ser)
        a = (needed_ingr1 | needed_ingr2)
        print(a)

    return get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)


the_recipe()
