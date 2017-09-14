import json
import re

def read_json(filename):
    """Returns a dictionary from the provided filename.
    
    Inputs:
    @filename: The name of the file
    """
    try:
        with open(filename) as data_file:
            new_dict = json.load(data_file)
    except:
        return {}
    return new_dict

def words(dictionary, min_word_length = 3, corpus = []):
    """Returns a list of the words contained into the provided dictionary.
    
    Inputs:
        @dictionary: the dictionary to analyze
        @min_word_lentgh: the minimum number of chars the word contains
        @corpus: a list of words to be added to the result (default empty)
    """
    if bool(dictionary):
        for key in dictionary.keys():
            if isinstance(dictionary[key], dict):
                corpus = corpus + words(dictionary[key])
            else:
                filter_lamba = lambda x: len(x) > min_word_length +1
                corpus = corpus + list(filter(filter_lamba, re.sub("[^\w]", " ",  dictionary[key]).split()))
        return corpus
    else:
        return corpus