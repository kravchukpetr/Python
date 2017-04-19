import string
import operator
file_obj = open('sentences.txt', 'r')
data_list = list(file_obj)
data_list = [line.lower() for line in data_list]
list_dict = []
all_words={}
j=0
for line in data_list:
    d={}
    data_row = [word.strip(string.punctuation) for word in line.split()]
    #print(data_row)
    #for word in data_row:
    #    print(word)
    udata = set(data_row)
    for i in udata:
        d[i] = data_row.count(i)
        if i not in all_words:
            all_words[i] = j
            j +=1
        #print(i, data_row.count(i))
    list_dict.append(d)
    #print d
print(list_dict)
sorted_all_words = sorted(all_words.items(), key=operator.itemgetter(1))
#for keys,values in all_words.items():
#    print(keys)
#    print(values)
print(len(all_words)-1)
print(len(data_list)-1)
matr=[[0 for y in xrange(len(all_words)-1)] for x in xrange(len(data_list)-1)]
# print(matr)
i=0
j=0
for sent in list_dict:
    for a_keys, a_values in all_words.items():
        for w_keys, w_values in sent.items():
            if w_keys == a_keys:
                print(i)
                print(j)
                print(w_values)
                matr[i][j] = w_values
        j +=1
    i +=1
    j = 0
print(matr)


