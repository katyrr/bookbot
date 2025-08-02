from stats import *
import sys

def get_book_text(filepath):
    '''
    INPUTS
    ======
    - filepath : string
        The relative file path to the text file of the book to analyse.

    OUTPUTS
    =======
    - contents : string
        The contents of the text file of the book to analyse.

    '''

    with open(filepath, 'r') as f:
        contents = f.read() 

    return contents


# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def configure_sort_criterion(keyname):
    '''
    INPUTS
    ======
    
    - keyname : string
        The name of the dict key to use for sorting.
    
    OUTPUTS
    =======
    - sort_criterion(items)
        A function that can be passed to dict.sort(key=sort_criterion).
        In that function, it is called on each item before the sort is performed,
        resulting in the dict being sorted in order of <keyname>.

    '''

    def sort_criterion(items):
        '''
        INPUTS
        ======
        - items : dict
            The dictionary to be sorted.

        OUTPUTS
        =======
        - The value of the key which will be used to sort the dict.

        '''
        return items[keyname]
    
    return sort_criterion



def main():
    '''
    Read the text file "frankenstein" and print the full contents to the console

    INPUTS : None
    OUTPUTS : None
    '''

    if len(sys.argv) != 2:
        print("error: wrong number of arguments passed.")
        print("correct usage: python3 main.py <path_to_text>.")
    
        sys.exit(1)

    loc = sys.argv[1]

    text = get_book_text(loc)
    num_words = get_num_words(text)
    char_freqs = get_freqs(text)

    list_freqs = dict_to_list(char_freqs)
    sort_crit = configure_sort_criterion("val")
    list_freqs.sort(reverse=True, key=sort_crit)
    
    print(f"============ BOOKBOT ============\nAnalyzing book found at {loc}...")
    print(f"----------- Word Count ----------\nFound {num_words} total words")
    print(f"--------- Character Count -------")

    for i in list_freqs:
        if i["key"].isalpha():
            print(f"{i["key"]}: {i["val"]}")
    

main()