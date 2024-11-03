import random
import matplotlib.pyplot as plt


def get_analytical_probabilities():
    """Обчислює аналітичні ймовірності для сум на двох шестигранних кубиках у відсотках."""
    sum_counts = {i: 0 for i in range(2, 13)}

    # Рахуємо кількість способів для кожної можливої суми
    for dice1 in range(1, 7):
        for dice2 in range(1, 7):
            dice_sum = dice1 + dice2
            sum_counts[dice_sum] += 1

    total_outcomes = 6 * 6
    probabilities = {sum_value: (count / total_outcomes) * 100 for sum_value, count in sum_counts.items()}

    return probabilities


def simulate_dice_throws(num_throws):
    """Симулює кидки двох кубиків та обчислює ймовірності кожної можливої суми у відсотках."""
    sum_counts = {i: 0 for i in range(2, 13)}

    for _ in range(num_throws):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice_sum = dice1 + dice2
        sum_counts[dice_sum] += 1

    probabilities = {sum_value: (count / num_throws) * 100 for sum_value, count in sum_counts.items()}
    return probabilities


# Запуск симуляції
num_throws = 1000000
monte_carlo_probabilities = simulate_dice_throws(num_throws)
analytical_probabilities = get_analytical_probabilities()

# Виведення таблиці для порівняння
print("Сума | Монте-Карло ймовірність (%) | Аналітична ймовірність (%)")
print("------------------------------------------------------------")
for sum_value in range(2, 13):
    print(
        f"{sum_value:>4} | {monte_carlo_probabilities[sum_value]:>23.2f} | {analytical_probabilities[sum_value]:>22.2f}")

# Побудова графіка
sums = list(range(2, 13))
monte_carlo_values = [monte_carlo_probabilities[sum_val] for sum_val in sums]
analytical_values = [analytical_probabilities[sum_val] for sum_val in sums]

plt.plot(sums, monte_carlo_values, marker='o', label='Монте-Карло ймовірність (%)')
plt.plot(sums, analytical_values, marker='x', label='Аналітична ймовірність (%)', linestyle='--')
plt.xlabel("Сума на двох кубиках")
plt.ylabel("Ймовірність (%)")
plt.title("Ймовірності сум на двох кубиках: Монте-Карло vs Аналітичні")
plt.legend()
plt.show()
