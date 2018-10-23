import pickle

my_data = {'a': [1, 2.0, 3, 4+6j],
           'b': ('string', u'Unicode string'),
           'c': None}
output = open('data.pkl', 'wb')
pickle.dump(data1, output)
output.close()
