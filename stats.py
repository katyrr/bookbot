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