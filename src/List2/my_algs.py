
#
# def ex8():
#     hll_test_registers()
#     hll_analyse_hash_func()
#     hll_test_estimate()
#     hll_compare_hyper_and_min_count()
#
#
# def hll_test_registers():
#     step = int(max_n / 100)
#     file_ex8_test_registers = open("ex8_test_registers.txt", "w")
#     file_ex8_test_registers.write("Raport zostal wygenerowany poprzez projekt dolaczony do rozwiazania. \
#         \nPlik zawiera dane dotyczace rozwiazania zadania 8, a mianowicie dane dotyczace testu algorytmu hyper_log_log dla roznych wielkosci rejestrow.\
#         \nUruchomiono hyper_log_log dla kolejnych n: {1, 101, 201, 301, 401, 501, ...} dla multizbiorow bez powtorzen.\
#         \nKolejne kolumny wyniku dotycza kolejnych liczb rejestrow: 16, 32, 64, 128, 256, 512, 1024, 2048, 4096. Zastosowano funkcje hashujaca sha3_256_bin_hash.\
#         \nWykresy danych z tego pliku znajduja sie w pliku 'ex8_test_registers_charts.xlsx'. ")
#     for n in range(1, max_n + 1, step):
#         file_ex8_test_registers.write(str(n))
#         for b in range(4, 13):
#             result = hyper_log_log(b, sha3_256_bin_hash, get_multi_set(n, False))
#             file_ex8_test_registers.write(str(abs(result / n - 1)))
#         file_ex8_test_registers.write("\n")
#     file_ex8_test_registers.close()
#
#
# def hll_analyse_hash_func():
#     step = int(max_n / 100)
#     file_ex8_test_hash_functions = open("ex8_test_registers.txt", "w")
#     file_ex8_test_hash_functions.write("Raport zostal wygenerowany poprzez projekt dolaczony do rozwiazania. \
#         \nPlik zawiera dane dotyczace rozwiazania zadania 8, a mianowicie dane dotyczace testu algorytmu hyper_log_log dla roznych funkcji hashujacych.\
#         \nUruchomiono hyper_log_log dla kolejnych n: {1, 101, 201, 301, 401, 501, ...} dla multizbiorow bez powtorzen.\
#         \nKolejne kolumny wyniku dotycza kolejnych funkcji hahsujacych: {default_bin_hash, sha224_bin_hash, sha3_256_bin_hash, sha_256_bin_hash, md5_bin_hash, simple_bin_hash}.\
#         \nWykresy danych z tego pliku znajduja sie w pliku 'ex8_test_hash_functions.xlsx'. ")
#     for func in [default_bin_hash, sha224_bin_hash, sha3_256_bin_hash, sha_256_bin_hash, md5_bin_hash, simple_bin_hash]:
#         print(str(func) + "- Avg relative error:")
#         avg_err = 0
#         no_tries = 0
#         for n in range(1, max_n + 1, step):
#             no_tries += 1
#             result = hyper_log_log(10, func, get_multi_set(n, False))
#             avg_err += abs((result / n) - 1)
#         print(avg_err / no_tries)
#
#
# def hll_test_estimate():
#     def_b = 10
#     file_ex8_test_estimate = open("file_ex8_test_estimate.txt", "w")
#     file_ex8_test_estimate.write("Raport zostal wygenerowany poprzez projekt dolaczony do rozwiazania. \
#         \nPlik zawiera dane dotyczace rozwiazania zadania 8, a mianowicie dane dotyczace testu algorytmu hyper_log_log oraz porownania estymacji Czebyszewa i Chernoffa.\
#         \nUruchomiono hyper_log_log dla kolejnych n: {1, 101, 201, 301, 401, 501, ...} dla multizbiorow bez powtorzen.\
#         \nW kolejnych liniach zanotowano wynik (_n / n), gdzie _n jest wynikiem otrzymanym z algorytmu hyper_log_log.")
#     for n in range(1, max_n + 1):
#         file_ex8_test_estimate.write(str(n))
#         _n = hyper_log_log(def_b, sha3_256_bin_hash, get_multi_set(n, False))
#         file_ex8_test_estimate.write("," + str(_n / n) + "\n")
#     file_ex8_test_estimate.close()
#
#
# def hll_compare_hyper_and_min_count():
#     file = open("zad_4_alg_comp_results.csv", "w")
#     file.write("bytes,min_count,hyper_log_log\n")
#     for b in range(4, 13):
#         k = math.ceil((2 ** b) * 5 / 32)
#         out = str((2 ** b) * 5) + ","
#         out += str(comp_rel_err(min_count, sha3_256_hash, k)) + ","
#         out += str(comp_rel_err(hyper_log_log, sha3_256_bin_hash, b)) + "\n"
#         file.write(out)
#     file.close()
#
#
# def comp_rel_err(f, hash_function, k_b):
#     step = int(max_n / 100)
#     no_tries = 0
#     avg_err = 0
#     for n in range(1, max_n + 1, step):
#         _n = f(k_b, hash_function, get_multi_set(n, False))
#         avg_err += abs(_n / n - 1)
#         no_tries += 1
#     return avg_err / no_tries




# def default_bin_hash(x):
#     h = hash(x)
#     base = 2 ** 128
#     if h < 0:
#         h += base
#     return bin(h)[2:].zfill(128)
#
#
# def sha224_bin_hash(x):
#     return bin(int(sha224(x.encode("utf-8")).hexdigest(), 16))[2:].zfill(256)
#
#
# def sha3_256_bin_hash(x):
#     return bin(int(sha3_256(x.encode("utf-8")).hexdigest(), 16))[2:].zfill(256)
#
#
# def sha_256_bin_hash(x):
#     return bin(int(sha256(x.encode("utf-8")).hexdigest(), 16))[2:].zfill(256)
#
#
# def md5_bin_hash(x):
#     return bin(int(md5(x.encode("utf-8")).hexdigest(), 16))[2:].zfill(128)
#
#
# def simple_bin_hash(x):
#     base = 60
#     h = 0
#     idx = 0
#     for c in x:
#         h = h * base + ord(c)
#         idx += 1
#     return bin(h)[2:].zfill(64)
