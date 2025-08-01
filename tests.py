from main import get_book_text

def test_func():

    test_contents = get_book_text("books/test_text.txt")

    print(test_contents)

test_func()