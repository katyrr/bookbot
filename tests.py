from main import *
from stats import *

def test_dict_sort():

    vehicles = [
        {"name": "car", "num": 7, "sort":100},
        {"name": "plane", "num": 10, "sort": 300},
        {"name": "boat", "num": 2, "sort": 200}
    ]

    original_vehicles = {"car":7, "plane":10, "boat":2}
    list_vehicles = dict_to_list(original_vehicles)
    print(list_vehicles)

    sort_criterion = configure_sort_criterion('num')
    vehicles.sort(reverse=True, key=sort_criterion)
    print(vehicles)
    


def test_func():

    test_contents = get_book_text("books/test_text.txt")
    num_words_in_test = get_num_words(test_contents)
    test_freqs = get_freqs(test_contents)

    print(f"num words = {num_words_in_test}")
    print(test_freqs)
    
test_dict_sort()
test_func()