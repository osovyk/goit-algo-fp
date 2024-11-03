import matplotlib.pyplot as plt
import numpy as np

# Функція для малювання одного гілля дерева
def draw_pythagoras_tree(ax, x, y, angle, length, level, max_level):
    if level > max_level:
        return

    # Обчислюємо нові координати кінця гілки
    x_new = x + length * np.cos(np.radians(angle))
    y_new = y + length * np.sin(np.radians(angle))

    # Малюємо гілку
    ax.plot([x, x_new], [y, y_new], color='green', lw=2 * (max_level - level + 1))

    # Малюємо дві нові гілки з новими кутами та меншими довжинами
    new_length = length * 0.8
    draw_pythagoras_tree(ax, x_new, y_new, angle - 45, new_length, level + 1, max_level)
    draw_pythagoras_tree(ax, x_new, y_new, angle + 45, new_length, level + 1, max_level)

# Головна функція для побудови дерева
def pythagoras_tree(levels):
    fig, ax = plt.subplots()

    # Налаштування візуалізації
    ax.set_aspect('equal')
    ax.axis('off')

    # Стартова точка та довжина першої гілки
    x_start, y_start = 0, 0
    initial_length = 1
    initial_angle = 90

    # Малюємо дерево Піфагора
    draw_pythagoras_tree(ax, x_start, y_start, initial_angle, initial_length, 0, levels)
    plt.show()

# Введення рівня рекурсії від користувача
if __name__ == "__main__":
    pythagoras_tree(levels=7)
