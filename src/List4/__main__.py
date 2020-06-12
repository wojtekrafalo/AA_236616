from src.List4.algorithms import *


def generate_points_by_q_power(scale_q, prob_func, file_name):
    ns = [1, 3, 6, 12, 24, 48]
    n_len = len(ns)
    step_q = (1 / (scale_q + 1)) / 2
    result = [[]] * (n_len + 1)
    list_q = list()
    q = 1 / 2 - step_q

    while q > 0:
        list_q.append(q)
        q -= step_q
    result[0] = list_q

    for i in range(0, n_len):
        list_prob = list()
        for q in list_q:
            list_prob.append(prob_func(ns[i], q))
            # q -= step_q
        result[i + 1] = list_prob
    save_result_to_csv(result, file_name, ns, scale_q)


def generate_points_by_n_number(scale_n, prob_func, file_name):
    qs = [0.001, 0.01, 0.1]
    q_len = len(qs)
    result = [[]] * (q_len + 1)
    list_n = list()

    for n in range(1, scale_n + 1):
        list_n.append(n)
    result[0] = list_n

    for i in range(0, q_len):
        list_prob = list()
        for n in range(1, scale_n + 1):
            list_prob.append(prob_func(n, qs[i]))
        result[i + 1] = list_prob
    save_result_to_csv(result, file_name, qs, scale_n)


def save_result_to_csv(data_list, file_name, var_list, scale):
    output = file_name[len(file_name) - 1]

    file = open(file_name + ".csv", "w")

    for v in var_list:
        output += (',' + str(v))
    output += "\n"

    for i in range(0, scale):
        for j in range(0, len(data_list)):
            output += (str(data_list[j][i]) + ", ")
        output += "\n"

    file.write(output)
    file.close()
    print(file_name + ".csv:  zakonczono zapis.")


def ex11_a(scale_q, scale_n):
    generate_points_by_q_power(scale_q, nakamoto_prob, "ex11_nakamoto_q")
    generate_points_by_q_power(scale_q, grunspan_prob, "ex11_grunspan_q")
    generate_points_by_n_number(scale_n, nakamoto_prob, "ex11_nakamoto_n")
    generate_points_by_n_number(scale_n, grunspan_prob, "ex11_grunspan_n")


def ex11_b(scale_q, scale_n):
    generate_points_by_q_power(scale_q, experimental_prob, "ex11_simulation_q")
    generate_points_by_n_number(scale_n, experimental_prob, "ex11_simulation_n")


if __name__ == '__main__':
    scale_q = 200
    scale_n = 100
    print("Uruchomienie rozwiązania zajmie kilka minut.")
    print("Zad 11 a) Trwa praca...")
    ex11_a(scale_q, scale_n)

    print("Zad 11 b) Trwa praca...")
    ex11_b(scale_q, scale_n)

    file_ex11 = open("data/ex11.txt", "w")
    file_ex11.write("Raport zostal wygenerowany poprzez projekt dolaczony do rozwiazania. Plik zawiera rozwiazanie zadania 11.\
        \nZostaly tu wyliczone prawdopodobienstwa sukcesu adwersarza P(n, q) wedlug formul Nakamoto i Gunspana oraz w sposob eksperymentalny poprzez wykonanie symulacji.\
        \n  -W przypadku, gdy n (ilosc wydobytych blokow w celu potwierdzenia transakcji) jest z gory ustalone\
        \n   (przyjmuje wartosci: {1, 3, 6, 12, 24, 48}), moc adwersarza q zmienia sie o 1/" + str(scale_q) + ".\
        \n    Wyniki zostaly zapisane w plikach odpowiednio: 'exA_nakamoto_q.csv' oraz 'exA_grunspan_q.csv'.\
        \n  -W przypadku, gdy q jest z gory ustalone (przyjmuje wartosci: {0.001, 0.01, 0.1}), n zmienia sie o 1/" + str(scale_n) + ".\
        \n    Wyniki zostaly zapisane w plikach odpowiednio: 'exA_nakamoto_n.csv' oraz 'exA_grunspan_n.csv'.\
        \n\nDla kazdego z plikow '.csv' (lacznie szesciu) w plikach o tej samej nazwie, lecz z rozszerzeniem '.xlsx' zaimportowano zestawy danych oraz wygenerowano wykresy.")
    file_ex11.close()
