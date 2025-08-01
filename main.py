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


def main():
    '''
    Read the text file "frankenstein" and print the full contents to the console

    INPUTS : None
    OUTPUTS : None
    '''

    frankenstein_contents = get_book_text("books/frankenstein.txt")

    print(frankenstein_contents)

main()