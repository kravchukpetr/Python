import string
import operator
import numpy as np
import scipy.spatial as scipy
file_obj = open('sentences.txt', 'r')
data_list = list(file_obj)
data_list = [line.lower() for line in data_list]
list_dict = []
all_words={}
j=0
for line in data_list:
    d={}
    data_row = [((word.strip(string.punctuation)).strip(string.digits)).strip(string.whitespace) for word in line.split()]
    #print(data_row)
    #for word in data_row:
    #    print(word)
    udata = set(data_row)
    for i in udata:
        d[i] = data_row.count(i)
        if i not in all_words:
            if i != '':
                all_words[i] = j
                j += 1
        #print(i, data_row.count(i))
    list_dict.append(d)
    #print d
#print(list_dict)
#sorted_all_words = sorted(all_words.items(), key=operator.itemgetter(1))
#for keys,values in all_words.items():
    #print(keys)
    #print(values)
print(len(all_words))
print(len(data_list))
matr=[[0 for y in range(len(all_words))] for x in range(len(data_list))]
# print(matr)
i = 0
for sent in list_dict:
    j = 0
    for a_keys, a_values in all_words.items():
        for w_keys, w_values in sent.items():
            if w_keys == a_keys:
                #print(w_values)
                matr[i][j] = w_values
        #print('i = ' + str(i))
        #print('j = ' + str(j))
        j += 1
    i += 1
#print(matr)
a = np.array(matr)
#print(a)
koef = [[x for y in range(2)] for x in range(len(data_list))]
print(koef)
for j in range(len(data_list)):
    if j > 0:
        dist = scipy.distance.cosine(a[0, :], a[j, :])
        koef[j][1] = dist
print(koef)
koef = sorted(koef, key=lambda koef_entry: koef_entry[1])
print(koef)
string = str(koef[1][0]) + ' ' + str(koef[2][0])
file_obj = open('submission-1.txt', 'w')
file_obj.write(string)
file_obj.close()
print(string)