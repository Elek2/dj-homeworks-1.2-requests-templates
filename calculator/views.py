from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def ingredients(request, recipe):
    servings = request.GET.get('servings', 1)
    dish = {}
    if DATA.get(recipe):  # Если нет такого ключа - ничего не делаем
        dish.update(DATA.get(recipe))  # Чтобы избежать ссылку на словарь DATA
        for ingredient in dish:
            dish[ingredient] = round(dish[ingredient]*int(servings), 1)  # Умножаем грамовки блюд на пар-р servings
    context = {
        'recipe': dish,
    }
    return render(request, 'calculator/index.html', context)

