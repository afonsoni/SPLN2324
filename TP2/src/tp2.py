import ijson
filename = "2024-04-07-DRE_dump.json"
with open(filename, "r", encoding="utf-8") as f:
	objects = ijson.items(f, "item")
	data_small = []
	for idx, object in enumerate(objects):
		if idx >= 10000:
			break
		data_small.append(object)

id = [ entry["id"] for entry in data_small]
notes = [ entry["notes"].replace("\n"," ").replace("\r"," ") for entry in data_small if "notes" in entry]

def preprocess(line):
    line = line.lower()
    tokens = tokenize(line)
    tokens = [token for token in tokens if token not in stopwords]
    return list(tokens)

sentences = []
dic = {id: notes}
for line in notes:
    tokens = preprocess(line)
    sentences.append(tokens)

doc_index = WmdSimilarity(sentences, model_w2v, num_best= 10)

query = "leis para emigração e politicas estrangeiras"

query_tokens = preprocess(query)

sims = doc_index[query_tokens]

for index, sim in sims:
    print('sim = %.4f' % sim)
    print(notes[index])