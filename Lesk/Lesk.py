from nltk.corpus import wordnet as wn
import re

def ret_synsets(var):
    return wn.synsets(var)

def ret_definition(var):
    return wn.synset(str(var)).definition

def ret_extract(var):
    return re.findall("\'(.*?)\'", str(var))

def wrapper_ret_synsets(string):
    list_ = []
    for var in string:
         list_.append(ret_extract(ret_synsets(var)))
    return list_

def wrapper_ret_definition(list_):
    row = -1
    col = 0

    for l in list_:
        row = row + 1
        col = 0;
        for i in l:
           list_[row][col] = ret_definition(i)
           col = col + 1

    return list_

def main():
    var = 'pine cone'
    tokens = var.split(' ')
    list_ = wrapper_ret_synsets(tokens)
    print wrapper_ret_definition(wrapper_ret_synsets(tokens))
    

if __name__ == "__main__":
    main()


