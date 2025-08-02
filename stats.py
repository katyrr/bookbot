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

def dict_to_list(dict):
    '''
    INPUTS
    ======
    - dict : dict
        The dictionary to convert.
        
    OUTPUTS
    =======
    - list : list of dicts
        The list version of <dict>.
        Each item in the list is an individual dictionary with two key/value pairs:
        The key of this element in the original <dict>, and the value of that key.
    
    '''

    list = []

    for i in dict:
        sub_dict = {}
        sub_dict["key"] = i
        sub_dict["val"] = dict[i]
        list.append(sub_dict)

    return list
