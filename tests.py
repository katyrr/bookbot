from main import *

def test_func():

    test_contents = get_book_text("books/test_text.txt")
    num_words_in_test = get_num_words(test_contents)

    print(num_words_in_test)
    

test_func()