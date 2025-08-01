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



