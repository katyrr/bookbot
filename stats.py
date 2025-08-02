def get_num_words(text):
    '''
    INPUTS
    ======
    - text : string
        A single string (of any length) to be analysed.

    OUTPUTS
    =======
    - num_words : int
        The number of words contained in <text>, where words are distinguished by delimeter " ".
    '''

    split_string = text.split()
    num_words = len(split_string)

    return num_words

def get_freqs(text):
    '''
    INPUTS
    ======
    - text : string
        A single string (of any length) to be analysed.

    OUTPUTS
    =======
    - char_freqs : dict
        A dictionary containing every character that appears in <text>, and the frequency of its occurance.
        Treats upper case and lower case letters as the same.
    
    '''

    text = text.lower()
    char_freqs = {}
    
    for c in text:
        
        if c in char_freqs:
            char_freqs[c] += 1
        else:
            char_freqs[c] = 1

    return char_freqs