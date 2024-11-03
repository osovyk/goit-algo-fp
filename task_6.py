items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Жадібний алгоритм
def greedy_algorithm(items, budget):
    # Сортуємо страви за співвідношенням калорійності до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    selected_items = []
    total_cost = 0
    total_calories = 0

    for name, data in sorted_items:
        if total_cost + data["cost"] <= budget:
            selected_items.append(name)
            total_cost += data["cost"]
            total_calories += data["calories"]

    return selected_items, total_cost, total_calories


# Динамічне програмування
def dynamic_programming(items, budget):
    n = len(items)
    item_names = list(items.keys())
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    # Заповнення таблиці dp для оптимального рішення
    for i in range(1, n + 1):
        name = item_names[i - 1]
        cost = items[name]["cost"]
        calories = items[name]["calories"]
        for b in range(budget + 1):
            if cost <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - cost] + calories)
            else:
                dp[i][b] = dp[i - 1][b]

    # Вибір оптимальних страв
    selected_items = []
    total_calories = dp[n][budget]
    total_cost = 0
    b = budget

    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            name = item_names[i - 1]
            selected_items.append(name)
            b -= items[name]["cost"]
            total_cost += items[name]["cost"]

    selected_items.reverse()  # Повертаємо в порядку додавання
    return selected_items, total_cost, total_calories


# Функція для виведення звіту
def print_report(selected_items, total_cost, total_calories):
    print("Вибрані страви:")
    for item in selected_items:
        print(f"- {item}: вартість {items[item]['cost']}, калорійність {items[item]['calories']}")
    print(f"Загальна вартість: {total_cost}")
    print(f"Загальна калорійність: {total_calories}")


# Приклад використання
budget = 100

# Використання жадібного алгоритму
print("-------------------\nЖадібний алгоритм:")
selected_items, total_cost, total_calories = greedy_algorithm(items, budget)
print_report(selected_items, total_cost, total_calories)

# Використання динамічного програмування
print("-------------------\nДинамічне програмування:")
selected_items, total_cost, total_calories = dynamic_programming(items, budget)
print_report(selected_items, total_cost, total_calories)
