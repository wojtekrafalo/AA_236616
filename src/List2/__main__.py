import math
import random

from src.List2.algorithms import min_count, get_multi_set, \
    default_hash, sha224_hash, sha3_256_hash, sha_256_hash, md5_hash, simple_hash

max_n = 10_000
def_k = 400


def ex5_a():
    diff_avg = 0

    for i in range(1, max_n + 1):
        est_rep = min_count(def_k, sha3_256_hash, get_multi_set(i, True))
        est_not = min_count(def_k, sha3_256_hash, get_multi_set(i, False))

        diff_rel = abs(est_rep - est_not) / est_not
        diff_avg += diff_rel

    diff_avg /= max_n

    file_ex5_a = open("ex5_a.txt", "w")
    file_ex5_a.write("Raport zostal wygenerowany poprzez projekt dolaczony do rozwiazania. Plik zawiera rozwiazanie zadania 1_a.\
    \nUruchomiono min_count dla kazdego n z przedzialu [1, " + str(max_n) + "] dla k=100,\
    \ndla zbiorow bez powtorzen oraz dla multizbiorow, o takim samym odpowiadajacym zbiorze podstawowym.\
    \nDla kazdych dwoch uruchomien wyliczono roznice wzgledna. Jej srednia wartosc wynosi: " + str(diff_avg) + "\
    \nOznacza to, ze powtorzenia w multizbiorze nie maja zadnego wplywu na dzialanie algorytmu min_count.")
    file_ex5_a.close()


def ex5_b():
    ks = [2, 3, 10, 100, 400]
    file_ex5_b = open("ex5_b.txt", "w")
    file_ex5_b.write("Raport zostal wygenerowany poprzez projekt dolaczony do rozwiazania. Plik zawiera rozwiazanie zadania 1_b.\
        \nUruchomiono min_count dla kazdego n z przedzialu [1, " + str(max_n) + "] dla multizbiorow bez powtorzen.\
        \nDla kazdego n uruchomiono algorytm dla kazdego k ze zbioru" + str(ks) + ".\
        \nDane zostaly uzyte do wygenerowania wykresu w programie Excel. Wykres przedstawia plik 'ex5_b_charts.xlsx'.\
        \nPonizej przedstawiono wyniki uruchomienia algorytmu:\n\n")

    for n in range(1, max_n + 1):
        file_ex5_b.write(str(n))
        for k in ks:
            _n = min_count(k, sha3_256_hash, get_multi_set(n, False))
            file_ex5_b.write("," + str(_n / n))
        file_ex5_b.write("\n")
    file_ex5_b.close()


def ex5_c():
    min_k = 10
    max_k = 1_000
    step = int(max_n / 100)
    max_diff = 0.1
    min_prob = 0.95
    found_k = -1

    for k in range(min_k, max_k):
        no_correct = 0
        complete_tests = 0
        for i in range(1, max_n, step):
            complete_tests += 1
            n = random.randint(1, max_n)
            _n = min_count(k, sha3_256_hash, get_multi_set(n, False))
            res = abs(_n / n - 1)
            if res < max_diff:
                no_correct += 1
        if no_correct / complete_tests >= min_prob:
            found_k = k
            break
    file_ex5_c = open("ex5_c.txt", "w")
    file_ex5_c.write("Raport zostal wygenerowany poprzez projekt dolaczony do rozwiazania. Plik zawiera rozwiazanie zadania 5_c.\
        \nUruchomiono min_count dla kolejnych k z przedzialu [" + str(min_k) + ", " + str(max_k) + "] \
        \ndla kolejnych n: {1, 101, 201, 301, 401, 501, 601} dla multizbiorow bez powtorzen.\
        \nDla kazdego n i k policzono, jak wiele uruchomien algorytmu spelnia warunek oraz zwrocono pierwsze k, dla ktorego jest spelniony.\
        \nWynioslo: " + str(found_k))
    file_ex5_c.close()
    return found_k


def ex_6():
    no_func = 6
    functions = [default_hash, sha224_hash, sha3_256_hash, sha_256_hash, md5_hash, simple_hash]
    func_err = [0.0] * 6
    step = 1

    for i in range(0, no_func):
        err = 0.0
        idx = 0
        for n in range(1, max_n, step):
            idx += 1
            _n = min_count(def_k, functions[i], get_multi_set(n, False))
            err += (abs(_n - n) / n)
        err /= idx
        func_err[i] = err

    file_ex6 = open("ex6.txt", "w")
    file_ex6.write("Raport zostal wygenerowany poprzez projekt dolaczony do rozwiazania. Plik zawiera rozwiazanie zadania 6.\
        \nUruchomiono min_count dla k=" + str(def_k) + ", dla kolejnych n: {1, 101, 201, 301, 401, 501, 601} dla multizbiorow bez powtorzen.\
        \nZastosowano " + str(no_func) + " roznych funkcji hashujacych: {default_hash, sha224_hash, sha3_256_hash, sha_256_hash, md5_hash, simple_hash}.\
        \nIch implementacje znajdują się w pliku mutual_exclusion_alg.py. Opisy funkcji znajduja sie w sprawozdaniu. \
        \nBlad wzgledny wyliczony przez min_count z wtykorzystaniem powyzszych funkcji wyniosl odpowiednio:\
        \n" + str(func_err))
    file_ex6.close()


def ex7():
    file_ex7_data = open("ex7_data.txt", "w")
    file_ex7_data.write("Raport zostal wygenerowany poprzez projekt dolaczony do rozwiazania. Plik zawiera rozwiazanie zadania 7.\
            \nUruchomiono min_count dla k=" + str(def_k) + ", dla kolejnych n: [1, " + str(max_n) + "] dla multizbiorow bez powtorzen.\
            \nZastosowano funkcje hashujaca: sha3_256_hash.\
            \nWypisano ponizej wartosc _n/n, gdzie _n jest wartoscia wyznaczona przez algorytm min_count.\
            \nWartosci te zostaly uzyte w celu wyznaczenia estymacji wedlug nierownosci Czebyszewa oraz Chernoffa.\
            \nWyniki te zapisano w pliku 'ex7_estimate.txt'.")
    results = []
    for n in range(1, max_n + 1):
        file_ex7_data.write(str(n))
        _n = min_count(def_k, sha3_256_hash, get_multi_set(n, False))
        results.append(_n / n)
        file_ex7_data.write("," + str(_n / n) + "\n")
    file_ex7_data.close()

    results.sort()
    file_ex7_estimate = open("ex7_estimate.txt", "w")
    alphas = [0.05, 0.01, 0.005]
    for alpha in alphas:
        delta = results[math.ceil((1 - alpha) * (len(results) - 1))] + 0.00000000001
        file_ex7_estimate.write("\n\nAlpha: " + str(alpha) + ",\n    delta=" + str(delta) + "\n    1-delta=" + str(
            1 - delta) + "\n    1+delta=" + str(1 + delta) + "\n")
        no_success = 0
        for r in results:
            if r < delta:
                no_success += 1
        file_ex7_estimate.write("    Prawdopodobienstwo= " + str(no_success / len(results)))


def main():
    print("Uruchomienie rozwiązania zajmie około godziny.\nZad 1.a) trwa praca...")
    ex5_a()
    print("Zad 5 b) Trwa praca...")
    ex5_b()
    print("Zad 5 c) Trwa praca...")
    found_k = ex5_c()
    print("Zad 5 c) zakończono. Znalezione k:" + str(found_k))
    print("Zad 6. Trwa praca...")
    ex_6()
    print("Zad 7. Trwa praca...")
    ex7()


if __name__ == '__main__':
    main()
