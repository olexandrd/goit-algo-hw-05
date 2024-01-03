# -*- coding: utf-8 -*-
import timeit
import matplotlib.pyplot as plt
from search_methods import kmp_search, boyer_moore_search, rabin_karp_search


with open("data/1.txt") as fb:
    text_1 = f'"""{fb.read()}"""'

with open("data/2.txt") as fb:
    text_2 = f'"""{fb.read()}"""'


def collect_execution_time(method, text, substring):
    setup_code = f"from search_methods import {method.__name__}"
    execution_code = f"{method.__name__}({text}, '{substring}')"
    execution_time = timeit.timeit(
        execution_code, setup=setup_code, globals=globals(), number=5
    )
    return execution_time, eval(execution_code)


substrings = [
    "через",
    "структури даних ",
    "пошук часто використовується через швидкий час пошуку",
    "класифікацію структур даних, що були обрані для дослідження та",
    "ultra mega ultimate superior python search algorithm that search lorem ipsum ...",
]

substrings_legend = [
    "5 chars",
    "16 chars",
    "53 chars\nfrom 1st",
    "62 chars\nfrom 2nd",
    "random\nstring",
]

# Get execution time for each search algorithm on text 1
kmpSearch = [collect_execution_time(kmp_search, text_1, x)[0] for x in substrings]
boyerMooreSearch = [
    collect_execution_time(boyer_moore_search, text_1, x)[0] for x in substrings
]
rabinKarpSearch = [
    collect_execution_time(rabin_karp_search, text_1, x)[0] for x in substrings
]

# Show plot for text 1
plt.figure(figsize=(8, 6))
plt.plot(substrings_legend, kmpSearch, label="kmpSearch")
plt.plot(substrings_legend, boyerMooreSearch, label="boyerMooreSearch")
plt.plot(substrings_legend, rabinKarpSearch, label="rabinKarpSearch")
plt.ylabel("Time, s")
plt.title("Search algorithms comparison on text 1")
plt.legend()
plt.grid(True, which="both", ls="--", c="0.5")
plt.show()


# Get execution time for each search algorithm on text 2
kmpSearch = [collect_execution_time(kmp_search, text_2, x)[0] for x in substrings]
boyerMooreSearch = [
    collect_execution_time(boyer_moore_search, text_2, x)[0] for x in substrings
]
rabinKarpSearch = [
    collect_execution_time(rabin_karp_search, text_2, x)[0] for x in substrings
]

# Show plot for text 2
plot2 = plt
plot2.figure(figsize=(8, 6))
plot2.plot(substrings_legend, kmpSearch, label="kmpSearch")
plot2.plot(substrings_legend, boyerMooreSearch, label="boyerMooreSearch")
plot2.plot(substrings_legend, rabinKarpSearch, label="rabinKarpSearch")
plot2.ylabel("Time, s")
plot2.title("Search algorithms comparison on text 2")
plot2.legend()
plot2.grid(True, which="both", ls="--", c="0.5")
plot2.show()
