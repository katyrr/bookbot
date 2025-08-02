from main import *
from stats import *

def test_func():

    test_contents = get_book_text("books/test_text.txt")
    num_words_in_test = get_num_words(test_contents)
    test_freqs = get_freqs(test_contents)

    print(f"num words = {num_words_in_test}")
    print(test_freqs)
    
test_func()