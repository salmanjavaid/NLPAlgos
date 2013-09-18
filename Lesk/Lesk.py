from nltk.corpus import wordnet as wn
from nltk.stem import SnowballStemmer
import nltk
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


def Test(list_):
     rows = -1
     cols = 0
     columns = []
     for row in list_:
         rows = rows + 1
         cols = 0
         for col in row:
             cols = cols + 1
         columns.append(cols)
     return (columns, rows + 1)

def StopWords(str1):
     words = str1.split()
     for word in words:
         if word in nltk.corpus.stopwords.words('english'):
             words.remove(word)
     return set(words)


def Test_2(str1, list_):
     
     scores = []
     for l in list_:
          scores.append(len(StopWords(str1).intersection(StopWords(l))))
 #         print str1
 #         print l
#          print '\n'
     return scores

def Test_1(list_):
    [columns, rows] = Test(list_)
    scores = []
    for k in range(0, 1):
        for i in range(0, columns[k]):
            scores.append(Test_2(str(list_[k][i]), list_[k + 1]))
 #           print '\n'
    return scores    

def main():
    var = 'pine cone'
    tokens = var.split(' ')
#    list_ = wrapper_ret_synsets(tokens)
    print Test_1(wrapper_ret_definition(wrapper_ret_synsets(tokens)))
    
#    stemmer = SnowballStemmer("english")
#    print stemmer.stem('saying')

if __name__ == "__main__":
    main()


