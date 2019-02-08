"""
    Playing with NLP tasks.
    Implementing one_hot_encoding.
    ograndoptimist, 08.02.2019.
    http://github.com/ograndoptimist, gabrieliprj@gmail.com
    mentored by Karla Figueiredo, karla.figueiredo@gmail.com
"""

from numpy import array

print(__doc__)


def eliminatePontuaction(text: str):
    """
        Eliminate pontuactions, single and double quoted symbols from the current string.
        ::params:
                text: a string containg all the suplemented text.
        ::return:
                returns a list containing all of the words from the original string.                
    """

    preprocessed_text = ''

    text = list(text.lower().split())
        
    for word in text:
        new_word = ''
        for character in word:
            if character in {'.', ',', "'", "’", '"'}:
                pass
            else:
                new_word += character
        preprocessed_text +=  ' ' + new_word        

    return preprocessed_text.split()              
            

def tokenization(text: str):
    """
        Build the tokenization.
        ::params:
                text: the raw text to be processed.
        ::return:
                returns a list of tokens.
    """

    raw_words = eliminatePontuaction(text)

    token = []

    for word in raw_words:
        if word not in token:
            token.append(word)

    return token


def wordToIndex(tokens: list):
    """
        Gives an integer index to each tokens's word.
        ::params:
            tokens: a list of unique words.
        ::return:
            dicio: returns a dictionary containing all the vocabulary composed of
            the following content: {'word': integer_index}.
    """

    dicio = dict()

    for index, word in enumerate(tokens):
        dicio[word] = index

    return dicio


def vectorization(vocabulary_dict: dict):
    """
        Vectorization of the tokens.
        ::params:
            vocabulary_dict: a dict containing all of the text's vocabulary.
        ::return:
            returns a list of index correspondent to each text's word.
    """

    vectorize = []

    for word in vocabulary_dict.keys():
        vectorize.append(vocabulary_dict[word])

    return vectorize    
    

def one_hot_encoding(text: str):
    """
       Return the one-hot-encoding preprocessement of raw texts.
        ::params:
            text: a string  containing the raw text the have to be preprocessed.
        ::returns:
            returns a list composed of 0's and 1's, where 1 is assigned to the local where the integer index is. 
    """
    
    assert text != str, "Please, enter a text!"
    
    tokens = tokenization(text)
    vocabulary_dict = wordToIndex(tokens)
    vector_of_index = vectorization(vocabulary_dict)

    length_dict = len(vocabulary_dict)

    one_hot_vector = []

    for index in vector_of_index:
        vector_aux = [0] * length_dict
        vector_aux[index] = 1
        one_hot_vector.append(vector_aux)

    return array(one_hot_vector)     


if __name__ == '__main__':

    text = "The Teams page contains a listing of the various Community Teams,\
             their responsibilities, links to their Wiki Home Pages and leaders, communication tools,\
             and a quick reference to let you know whether and when they hold meetings.\
             Most Teams’ Wiki Home Pages provide information about who they are, what they do, when\
             their meetings are, and how to contact them. Using these pages, teammates are able to communicate and coordinate projects."
    
    print(one_hot_encoding(text))
