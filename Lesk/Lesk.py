from nltk.corpus import wordnet as wn
from nltk.stem import SnowballStemmer
import nltk
import re


#synset for each word

def ret_synsets(var):
    return wn.synsets(var)

# synset definiton

def ret_definition(var):
    return wn.synset(str(var)).definition

# regular expression to find words between ''

def ret_extract(var):
    return re.findall("\'(.*?)\'", str(var))

# wrapper for synsets

def wrapper_ret_synsets(string):
    list_ = []
    for var in string:
         list_.append(ret_extract(ret_synsets(var)))
    return list_


# wrapper for definitions

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

# This function shoudl be updated and Test_* should be brought in

def Lesk(list_):

    count_list = list_
    count = 0
    row = 0
    col = 0
    columns = []
    for i in list_:
        col = 0
        for j in i:   
            count_list[row][col] = count
            count = count + 1
            col = col + 1
        row = row + 1

    return count_list

# for each word, find the number of definitions

def Test(list_):
     rows = -1 # Because of python's terribly confusing delimitors, starting row with -1 instead of 1
     cols = 0
     columns = []
     for row in list_:
         rows = rows + 1
         cols = 0
         for col in row:
             cols = cols + 1
         columns.append(cols)
     return (columns, rows + 1)


# remove stopwords

def StopWords(str1):
     words = str1.split()
     for word in words:
         if word in nltk.corpus.stopwords.words('english'):
             words.remove(word)
     return set(words)

# compare the definition here by splitting each word's definitions and then working on them individually

def Test_2(str1, list_):
     
     scores = []
     for l in list_:
          scores.append(len(StopWords(str1).intersection(StopWords(l))))
 #         print str1
 #         print l
 #         print '\n'
     return scores

# wrapper function to compare the first word definition with each word

def Test_1(list_):
    [columns, rows] = Test(list_)
    scores = []
    for k in range(0, 1):
        for i in range(0, columns[k]):
            scores.append(Test_2(str(list_[k][i]), list_[k + 1]))
    
    return scores    

def main():
    var = 'pine cone' #Input to Lesk
    tokens = var.split(' ') #Split the words

    # retrieve synsets of each word, and then definition of each word
    print Test_1(wrapper_ret_definition(wrapper_ret_synsets(tokens))) 
    



if __name__ == "__main__":
    main()


