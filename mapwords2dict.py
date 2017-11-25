import pickle

selectItems=50

with open ('dict', 'rb') as fp:
    nameSet = pickle.load(fp)

medicalDict=dict.fromkeys(nameSet, 0)

text="abduction ablation abduction"

text=text.split(" ");

for word in text:
    if(word in nameSet):
        medicalDict[word]+=1


k=sorted(medicalDict, key=medicalDict.__getitem__)
k=list(reversed(k[len(k)-selectItems:]))
print(k)

