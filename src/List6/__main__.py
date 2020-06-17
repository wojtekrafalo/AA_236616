from src.List6.algorithms import *

ex14_times = 10_000
ex15_times = 100_000
ex15_n = 11


def ex14(t):
    return compare_funs(count_lines_f_iterative, fun_2_n_minus, t)


def ex15(times, n):
    avgs = []
    for i in range(0, n + 1):
        avgs.append(test_avg_fun_arr(times, i))
        # return test_avg_fun_arr(times, n)
    return avgs


def print_calls(arr):
    s = "\n"
    for i in range(0, len(arr)):
        s += str(i) + ": " + str(arr[i]) + "\n"
    return s


if __name__ == '__main__':
    # print("Uruchomienie rozwiązania zajac nawet kilkanascie minut.")
    #
    # print("Zad 14. Ponizej zostanie " + str(ex14_times) + " razy wywolana funkcja, ktora dla kolejnych liczb naturalnych\
    #  \nporownuje wartosci dwu funkcji: \
    #  \n    ciagu: 2^n - 1 \
    #  \n    oraz funkcji zliczajacej rzeczywista ilosc wywolan linii 6. pseudokodu z tresci zadania w sposob iteracyjny.\
    #  \n\nTrwa praca...")
    # is_the_same = ex14(ex14_times)
    #
    # if is_the_same:
    #     print("Wspomniane wywolanie sprawdzilo, ze funkcje sa rowne dla zbioru [0," + str(ex14_times) + "]")
    # else:
    #     print("Wspomniane wywolanie sprawdzilo, ze funkcje roznia sie dla zbioru [0," + str(ex14_times) + "]")

    print("\n\n\nZad 15.Ponizej zostanie " + str(ex15_times) + " razy wywolany algorytm uruchamiajacy rekurencyjnie dla\
     \nlosowej tablicy dla n=" + str(ex15_n) + ". \
     \nPonizej zostanie wypisana srednia ilosc wywolan algorytmu. \nTrwa praca...\n")

    arr_of_calls = ex15(ex15_times, ex15_n)
    print("Algorytm dla kolejnych n wykonal sie srednio: " + print_calls(arr_of_calls))
