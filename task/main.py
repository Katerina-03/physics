import numpy as np
import math
import cmath
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#===Task 1===
def bloch_sphere_plot_initial():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Расчет сферических координат
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = np.outer(np.sin(u), np.cos(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.cos(u), np.ones_like(v))

    # Построение сферы Блоха
    ax.plot_surface(x, y, z, color='grey', alpha=0.5, linewidth=0)

    # Построение точки состояния
    # Коэффициенты состояния |psi>
    x_state, y_state, z_state = 0, -1/np.sqrt(2), 0
    ax.scatter(x_state, y_state, z_state, color='blue')

    # Построение вектора состояния
    psi = ax.quiver(0, 0, 0, x_state, y_state, z_state, color='blue')
    x = ax.quiver(0,0,0, 1,0,0, color='green')
    y = ax.quiver(0, 0, 0, 0, 1, 0, color='yellow')
    z = ax.quiver(0,0,0, 0,0,1, color='red')

    # Настройка осей
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    ax.set_aspect("equal")

    # Подписи осей
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.legend([psi, x, y, z],['|psi>', 'x', 'y','z'], loc='best')

    plt.title('Сфера Блоха')
    plt.show()

bloch_sphere_plot_initial()

psi_initial = 1/np.sqrt(2) * np.array([1, -1j])

#=================Task 2===============

n = np.array([1/np.sqrt(2), 1/np.sqrt(2), 0])
a = np.pi / 2

cos_a = np.cos(a)
sin_a = np.sin(a)
I = np.eye(3)
cross_product_matrix = np.array([[0, -n[2], n[1]], [n[2], 0, -n[0]], [-n[1], n[0], 0]])
rotation_matrix = cos_a * I + (1 - cos_a) * np.outer(n, n) + sin_a * cross_product_matrix


print("Матрица оператора поворота")
print(rotation_matrix)
#===Task 3===
x_state, y_state, z_state = 0, -1/np.sqrt(2), 0
psi_A = np.array([[x_state], [y_state], [z_state]])
# Подействовать матрицей поворота на состояние |psi>
final_state = rotation_matrix.dot(psi_A)

print("Вектор конечного состояния:", final_state)

# Вектор конечного состояния
v = np.array(final_state)

# Ось Z
z = np.array([[1], [1], [0]])

# Вычисление угла между вектором и осью Z
angle = np.arccos(np.dot(v.T, z) / (np.linalg.norm(v) * np.linalg.norm(z)))

print('Угол между вектором конечного состояния и осью z',angle)
def bloch_sphere_plot_final():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Расчет сферических координат
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = np.outer(np.sin(u), np.cos(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.cos(u), np.ones_like(v))

    # Построение сферы Блоха
    ax.plot_surface(x, y, z, color='grey', alpha=0.5, linewidth=0)

    # Построение точки состояния
    # Коэффициенты состояния |psi>
    x_state_final, y_state_final, z_state_final = np.array(final_state)
    ax.scatter(x_state_final, y_state_final, z_state_final, color='blue')

    # Построение вектора конечного состояния
    psi_final_state = ax.quiver(0, 0, 0, x_state_final, y_state_final, z_state_final, color='blue')
    x = ax.quiver(0,0,0, 1,0,0, color='green')
    y = ax.quiver(0, 0, 0, 0, 1, 0, color='yellow')
    z = ax.quiver(0,0,0, 0,0,1, color='red')

    # Настройка осей
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    ax.set_aspect("equal")

    # Подписи осей
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.legend([psi_final_state, x, y, z],['Вектор конечного состояния', 'x', 'y','z'], loc='best')

    plt.title('Сфера Блоха')
    plt.show()
bloch_sphere_plot_final()