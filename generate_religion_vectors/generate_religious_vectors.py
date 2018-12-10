import gensim


# Load Google's pre-trained Word2Vec model.
model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)  

print(model.wv["Allah"])

words = ['Christian', 'Muslim', 'christian', 'muslim', 
         'Christ', 'Allah', 'Jesus', 'Muhammad', 'Christmas', 'Eid',
         'Abraham', 'Ibrahim', 'Maryam', 'Mary', 
         'Bible', 'Quran', 'church', 'mosque', 'Christianity', 'Islam']

largeVector = []
for w in words:
	embedding = [w]
	embedding.extend(model.wv[w])
	largeVector.extend(embedding)

with open('religious_vectors.txt', 'w') as f:
    for item in largeVector:
        if (type(item) == str):
        	f.write("\n")
        	f.write("%s " % item)
        else:
        	f.write("%s " % item)