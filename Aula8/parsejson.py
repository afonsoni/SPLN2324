# import json

# f = open("2024-04-07-DRE_dump.json", "r", encoding="utf-8")
# data = json.load(f)
# f.close()

# data_small = data[0:10000]


# notes = [ entry["notes"].replace("\n"," ").replace("\r"," ") for entry in data_small if "notes" in entry]
# f_out = open("small.json", "w", encoding="utf-8")

# #json.dump(data_small, f_out, indent=4, ensure_ascii=False)
# for note in notes:
# 	f_out.write(note + "\n")
# f_out.close()

import ijson
filename = "2024-04-07-DRE_dump.json"
with open(filename, "r", encoding="utf-8") as f:
	objects = ijson.items(f, "item")
	data_small = []
	for idx, object in enumerate(objects):
		if idx >= 10000:
			break
		data_small.append(object)

notes = [ entry["notes"].replace("\n"," ").replace("\r"," ") for entry in data_small if "notes" in entry]
f_out = open("small.txt", "w", encoding="utf-8")

#json.dump(data_small, f_out, indent=4, ensure_ascii=False)
for note in notes:
	f_out.write(note + "\n")
f_out.close()