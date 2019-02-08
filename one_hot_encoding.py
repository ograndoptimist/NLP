"""
    Playing with NLP tasks.
    Implementing one_hot_encoding preprocessing method.
    ograndoptimist, 08.02.2019.
    http://github.com/ograndoptimist, gabrieliprj@gmail.com
    mentored by Karla Figueiredo, karla.figueiredo@gmail.com
"""

from numpy import array

print(__doc__)


def preprocessText(text: str):
    """
        Eliminate pontuactions, single and double quoted symbols from the current string.
        ::params:
                text: a string containg all the suplemented text.
        ::return:
                returns a string containing all of the words from the original string but without
                especial symbols and capital letters.
        Example:
            >>> eliminatePontuaction("Some random text.")
            'some random text here'
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

    return preprocessed_text.lower()              
            

def tokenization(text_preprocessed: str):
    """
        Build the tokenization.
        ::params:
                text_preprocessed: the preprocessed text to be tokenized.
        ::return:
                returns a list of tokens.
        Example:
            >>> tokenization("some random text here")
            ['some', 'random', 'text', 'here']
    """

    raw_words = text_preprocessed.split()

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
         Example:
            >>> wordToIndex(['some', 'random', 'text', 'here'])
            {'some': 0, 'random': 1, 'text': 2, 'here': 3}
    """

    dicio = dict()

    for index, word in enumerate(tokens):
        dicio[word] = index

    return dicio


def vectorization(list_of_words: list, vocabulary_dict: dict):
    """
        Vectorization of the tokens.
        ::params:
            list_of_words: a list of preprocessed words from the rax text
            vocabulary_dict: a dict containing all of the text's vocabulary.
        ::return:
            returns a list of index correspondent to each text's word.
        Example:
            >>> vectorization(['some', 'random', 'text', 'here'], {'some': 0, 'random': 1, 'text': 2, 'here': 3})
            [0, 1, 2, 3]
    """

    vectorize = []

    for word in list_of_words:
        vectorize.append(vocabulary_dict[word])

    return vectorize    
    

def one_hot_encoding(text: str):
    """
       Return the one-hot-encoding preprocessement of raw texts.
        ::params:
            text: a string  containing the raw text that have to be preprocessed.
        ::returns:
            returns a list composed of 0's and 1's, where 1 is assigned to the local where the integer index is.
        Example:
            >>> text = "Some random text here"
            >>> one_hot_encoding(text)
            [[1 0 0 0]
             [0 1 0 0]
             [0 0 1 0]
             [0 0 0 1]]
    """
    
    assert text != str, "Please, enter a text!"
    
    text_preprocessed = preprocessText(text)
    tokens = tokenization(text_preprocessed)
    vocabulary_dict = wordToIndex(tokens)
    vector_of_index = vectorization(text_preprocessed.split(), vocabulary_dict)

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
             their meetings are, and how to contact them. Using these pages, teammates are able to\
             communicate and coordinate projects."
    
    save = one_hot_encoding(text)
    
    save_array = ''
    for k in save:
        save_array += str(k) + '\n'

    with open('array.txt', 'w') as file:
            file.write(save_array)
