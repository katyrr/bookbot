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


def get_num_words(text):
    '''
    INPUTS
    ======
    - text : string
        A single string to be analysed.

    OUTPUTS
    =======
    - num_words : int
        The number of words contained in <text>, where words are distinguished by delimeter " ".
    '''

    split_string = text.split()
    num_words = len(split_string)

    return num_words

def main():
    '''
    Read the text file "frankenstein" and print the full contents to the console

    INPUTS : None
    OUTPUTS : None
    '''

    frankenstein_contents = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(frankenstein_contents)
    
    print(f"{num_words} words found in the document")

main()