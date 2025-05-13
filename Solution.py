import numpy as np
from scipy.optimize import linprog

def solve_game():
    A = np.array([
        [16/3, 13/3, 10/3],
        [5/3, 4, -5/3],
        [6, 13/3, 14/3]
    ])

    row_mins = np.min(A, axis=1)
    col_maxs = np.max(A, axis=0)

    minimax = np.max(row_mins)
    maximin = np.min(col_maxs)

    if minimax == maximin:
        print("Седлова точка съществува.")
        print(f"Решението е в чисти стратегии с цена на играта: {minimax}")
        return
    else:
        print("Няма седлова точка. Решението е в смесени стратегии.")

    c = [-1, -1, -1]
    A_ub = -A.T
    b_ub = [-1] * 3

    result_1 = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=(0, None), method="highs")
    
    if result_1.success:
        probs_1 = result_1.x / sum(result_1.x)  # Вероятности за Играч 1
        print("Оптимални вероятности за Играч 1:", probs_1)
    else:
        print("Грешка при решаване на стратегията за Играч 1.")

    c = [1, 1, 1]
    A_ub = A
    b_ub = [1] * 3

    result_2 = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=(0, None), method="highs")

    if result_2.success:
        probs_2 = result_2.x / sum(result_2.x)
        print("Оптимални вероятности за Играч 2:", probs_2)
    else:
        print("Грешка при решаване на стратегията за Играч 2.")

if __name__ == "__main__":
    solve_game()