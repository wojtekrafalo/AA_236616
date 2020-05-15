import csv
import math
import random

from src.List3.algorithms import unique_sum, get_multi_set, Scenario, \
    default_hash, sha224_hash, sha3_256_hash, sha_256_hash, md5_hash, simple_hash, print_multiset, simple_sum, \
    unique_real_sum, unique_avg, unique_real_avg

max_n = 1_000
def_m = 200


def ex9():
    m_arr = [2, 3, 5, 10, 100, 200, 300, 500]
    for m in m_arr:
        file_name = "ex9_data_" + str(m) + ".csv"
        file_ex9_data_m = open(file_name, "w")
        file_ex9_data_m.write("n,ratio" + "\n")

        for i in range(1, max_n + 1):
            multiset = get_multi_set(i, False)
            sum_est = unique_sum(multiset, sha3_256_hash, m)
            sum_exa = unique_real_sum(multiset)

            ratio = sum_est / sum_exa
            file_ex9_data_m.write(str(i) + "," + str(ratio) + "\n")
        file_ex9_data_m.close()
        print(file_name + ": zakonczono zapis.")

    file_ex9 = open("data/ex9.txt", "w")
    file_ex9.write("Raport zostal wygenerowany poprzez projekt dolaczony do rozwiazania. Plik zawiera rozwiazanie zadania 9.\
    \nZostaly tu wykonane eksperymenty analogiczne do tych z listy zadan dotyczacej minCount.\
    \nUruchomiono unique_sum dla kazdego n z przedzialu [1, " + str(max_n) + "] dla roznych m ze zbioru: " + str(
        m_arr) + "\
    \nDla kazdych dwoch roznych n multizbiory sa rozlaczne.\
    \nDla kazdego m wyniki przedstawiono na osobnym wykresie.\
    \nNa osi poziomej znajduje sie n, zas na osi pionowej stosunek (_sum/sum).\
    \nWyniki uruchomienia algorytmu znajduja sie w plikach o nazwie 'ex9_data_{m}.csv', gdzie w miejsce {m} umieszczono wartosc m.\
    \nZas wykresy znajduja sie w plikach o tych samych nazwach, lecz z rozszerzeniem '.xlsx'.\
    \nW tym oraz pozostalyc plikach zastosowano podstawienie:\
    \n  _sum - estymowana przez algorytm unique_sum wartosc sumy unikalnych elementow multizbioru.\
    \n  sum  - dokladna wartosc ow sumy.")
    file_ex9.close()


def ex9_a():
    fun_hash = [default_hash, sha224_hash, sha3_256_hash, sha_256_hash, md5_hash, simple_hash]
    fun_err = []
    step = int(max_n / 100)
    for fun in fun_hash:
        diff_ratio = 0
        inc = 0
        for i in range(1, max_n + 1, step):
            multiset = get_multi_set(i, False, Scenario.LINEAR, 1, 10)
            sum_est = unique_sum(multiset, fun, def_m)
            sum_exa = unique_real_sum(multiset)

            ratio = sum_est / sum_exa
            diff_ratio += ratio
            inc += 1
        diff_ratio /= inc
        fun_err.append(diff_ratio)

    file_ex9_a = open("data/ex9_a.txt", "w")
    file_ex9_a.write("Raport zostal wygenerowany poprzez projekt dolaczony do rozwiazania. Plik zawiera rozwiazanie zadania 9_a.\
    \nZastosowano 6 funkcji hashujacych ze zbioru: {default_hash, sha224_hash, sha3_256_hash, sha_256_hash, md5_hash, simple_hash}\
    \nOpisy kolejnych funkcji znajduja sie w sprawozdaniu dolaczonym do rozwiazania.\
    \nUruchomiono unique_sum z uzyciem kazdej z nich dla kolejnych n z przedzialu [1, 11, 21, 31, ..." + str(
        max_n) + "] dla m=" + str(def_m) + ",\
    \ndla multizbiorow bez powtorzen. Dla danego n zastosowano ten sam multizbiorj jednak dla dwoch roznych n multizbiory sa rozlaczne.\
    \nDla kazdego uruchomienia algorytmu wyznaczono stosunek (_sumy/sum). Nastepnie wyznaczono jego wartosc srednia dla kazdej funkcji hashujacej.\
    \nWyniki wynosza odpowiednio:" + str(fun_err))
    file_ex9_a.close()


def ex9_b():
    sc_err = []
    step = int(max_n / 100)
    def_a = 50
    def_b = max_n
    reps = [True, False]
    for rep in reps:
        for scenario in Scenario:
            diff_ratio = 0
            inc = 0
            for i in range(1, max_n + 1, step):
                multiset = get_multi_set(i, rep, scenario, def_a, def_b)
                sum_est = unique_sum(multiset, sha3_256_hash, def_m)
                sum_exa = unique_real_sum(multiset)

                ratio = sum_est / sum_exa
                diff_ratio += ratio
                inc += 1
            diff_ratio /= inc
            sc_err.append(diff_ratio)

    file_ex9_b = open("data/ex9_b.txt", "w")
    file_ex9_b.write("Raport zostal wygenerowany poprzez projekt dolaczony do rozwiazania. Plik zawiera rozwiazanie zadania 9_b.\
    \nAlgorytm unique_sum uruchomiono dla roznych scenariuszy:\
    \n- w przypadku, gdy wartosci lambda elementow multizbioru sa sobie rowne (EQUAL),\
    \n- sa losowo wybrane z rozkladu jednostajnego z przedzialu: [1, " + str(def_b) + " ] (LINEAR) \
    \n- oraz kiedy wiekszosc elementow jest z przedzialu: [" + str(def_b - def_a) + ", " + str(def_b + def_a) + " ], ale okolo 5% z wartosci sa odstajace (SIMILAR).\
    \nKazdy z tych scenariuszy zostal uruchomiony dla multizbiorow z powtorzeniami oraz bez powtorzen. Lacznie wzieto pod uwage szesc scenariuszy.\
    \nDla kazdego z nich uruchomiono unique_sum dla kolejnych n z przedzialu [1, 11, 21, 31, ..." + str(
        max_n) + "] dla m=" + str(def_m) + ",\
    \nDla kazdego uruchomienia algorytmu zmierzono stosunek (_sum/sum). Dla kazdego scenariusza wyliczono srednia arytmetyczna tych wartosci.\
    \nWyniki przedstawia ponizsza tabela:\
    \n                  EQUAL           LINEAR          SIMILAR\
    \nPowtorzenia:      " + str(sc_err[0]) + " " + str(sc_err[1]) + " " + str(sc_err[2]) + "\
    \nBez powtorzen:    " + str(sc_err[3]) + " " + str(sc_err[4]) + " " + str(sc_err[5]))

    file_ex9_b.close()


def find_binary_search_delta(results, alpha, dokl):
    size = len(results)
    corr = int((1 - alpha) * size)
    delta = 5
    min_d = 0
    max_d = 10
    step = 2

    while abs(delta - min_d) > dokl:
        idx = 0
        while idx <= corr:
            if 1 - delta < results[idx] < 1 + delta:
                idx += 1
            else:
                break
        if idx <= corr:
            temp = delta
            delta = (max_d + temp) / step
            min_d = temp
        else:
            temp = delta
            delta = (min_d + temp) / step
            max_d = temp
    return delta


def ex9_c():
    alphas = [0.05, 0.01, 0.005]
    m_arr = [2, 3, 5, 10, 100, 200, 300, 500]
    file_base = "ex9_data_"
    file_ext = ".csv"
    deltas = []
    deltas_sub = []
    deltas_add = []
    dokl = 0.000000000000001

    for m in m_arr:
        results = list()
        with open(file_base + str(m) + file_ext, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                results.append(abs(float(row["ratio"])))
        results.sort()

        for alpha in alphas:
            deltas.append(find_binary_search_delta(results, alpha, dokl))

    for d in deltas:
        deltas_sub.append(float(1 - d))
        deltas_add.append(float(1 + d))

    file_ex9_c = open("data/ex9_c.txt", "w")
    file_ex9_c.write("Raport zostal wygenerowany poprzez projekt dolaczony do rozwiazania. Plik zawiera rozwiazanie zadania 9_c.\
    \nWykorzystano wyniki otrzymane w zadaniu 9 (mianowicie te zapisane w pliku 'ex9_data_200.csv'), aby porownac je z ograniczeniami wynikajacymi z nierownosci Czebyszewa.\
    \nUruchomiono wyszukiwanie binarne maksymalnych wartosci delta (zgodnie z pewna dokladnoscia rowna " + str(dokl) + ") dla trzech wartosci alpha: 5%, 1% oraz 0.5%, aby osiagnac nierownosc:\
    \n          P[1-delta < _sum / sum < 1+delta]  >  1-alpha.\
    \n Powyzsze ograniczenia zostaly przedstawione razem z wartosciami (_sum/sum) jednym wykresie w pliku 'ex9_c_data_{m}.xlsx', gdzie w miejsce {m} wstawiono odpwiednie wartosci m.\
    \n Dla odpowiednich wartosci m oraz wartosci alpha osiagnieto ponizsze wyniki:")

    for i in range(0, len(m_arr)):
        file_ex9_c.write("\n\n\n\n\n\n" + str(m_arr[i]) + ":\n")
        file_ex9_c.write(" \
        \n      delta: " + str(deltas[3*i + 0]) + "   " + str(deltas[3*i + 1]) + "   " + str(deltas[3*i + 2]) + "\
        \n  1 - delta: " + str(deltas_sub[3*i + 0]) + "   " + str(deltas_sub[3*i + 1]) + "   " + str(deltas_sub[3*i + 2]) + "\
        \n  1 + delta: " + str(deltas_add[3*i + 0]) + "   " + str(deltas_add[3*i + 1]) + "   " + str(deltas_add[3*i + 2]))
    file_ex9_c.close()


def analyze_results(file_name, alpha):
    results = list()
    with open(file_name, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            results.append(abs(float(row["result"]) - 1))

    results.sort()
    i = math.ceil((1 - alpha) * (len(results) - 1))
    delta = results[i] + 0.00000000001
    print("For alpha: " + str(alpha) + ", the delta=" + str(delta) + "\n1-delta=" + str(1 - delta) + "\n1+delta=" + str(
        1 + delta))
    success_tries = 0
    for r in results:
        if r < delta:
            success_tries += 1
    print(success_tries / len(results))
    assert 1 - alpha < success_tries / len(results)


def ex10():
    avg_ratio = 0.0
    step = int(max_n / 100)
    def_a = 50
    def_b = max_n
    inc = 0

    file_ex10_data = open("data/ex10_data.csv", "w")
    file_ex10_data.write("n,ratio" + "\n")

    for i in range(1, max_n + 1, step):
        multiset = get_multi_set(i, False, Scenario.SIMILAR, def_a, def_b)
        avg_est = unique_avg(multiset, sha3_256_hash, def_m)
        avg_exa = unique_real_avg(multiset)

        ratio = avg_est / avg_exa
        file_ex10_data.write(str(i) + "," + str(ratio) + "\n")
        avg_ratio += ratio
        inc += 1

    avg_ratio /= inc
    file_ex10_data.close()
    print("ex10_data.csv: Zakonczono zapis.")

    file_ex10 = open("data/ex10.txt", "w")
    file_ex10.write("Raport zostal wygenerowany poprzez projekt dolaczony do rozwiazania. Plik zawiera rozwiazanie zadania 10.\
        \nAlgorytm unique_sum uruchomiono dla kolejnych n z przedzialu [1, 11, 21, 31, ..." + str(
        max_n) + "] dla m=" + str(def_m) + ",\
        \nDla kazdego uruchomienia _avg/avg). Na koniec wyznaczono srednia arytmetyczna tych wartosci.\
        \nWykorzystano sposob polegajacy na jednym przebiegu algorytmu unique_sum,\
        \njednak rownoczesnie z estymowaniem sumy watosci lambda unikalnych elementow multizbioru, estymowano rowniez osobna sume,\
        \nzakladajac, ze dla kazdego elementu wartosc lambda wynosi 1. W ten sposob z podobna dokladnoscia wyznaczono licznosc zbioru.\
        \n\nWyniki eksperymentu (stosunek dla kolejnych uruchomien algorytmu) znajduja sie w pliku ex10_data.csv.\
        \nSrednia wartosc wyliczonego stosunku sredniej do jej rzeczywistych wartosci wyniosla: " + str(
        avg_ratio) + ".")
    file_ex10.close()


def main():
    # print("Uruchomienie rozwiązania zajmie około godziny.")
    #
    # print("Zad 9) Trwa praca...")
    # ex9()
    #
    # print("Zad 9 a) Trwa praca...")
    # ex9_a()
    #
    # print("Zad 9 b) Trwa praca...")
    # ex9_b()
    #
    print("Zad 9 c) Trwa praca...")
    ex9_c()
    #
    # print("Zad 10) Trwa praca...")
    # ex10()


if __name__ == '__main__':
    main()
