from pymongo import MongoClient
client = MongoClient('localhost', 27017)

corrThreshold=0.5

db = client.test_database

correlationCollection = db.correlation

def insert(x, y, corr):
    l=sorted([x, y])
    entry={"keyword1": l[0],
        "keyword2": l[1],
        "correlation": corr}
    correlationCollection.insert_one(entry)

def get(x, y):
    l=sorted([x, y])
    entry= correlationCollection.find_one(
        {"keyword1": l[0],"keyword2": l[1]})
    if(entry==None):
        return None
    return entry["correlation"]

def getDOI(keyword):
    print("a")

keywords={}

keys=keywords.keys()

for i in range(len(keys)):
    for j in range(i+1,len(keys)):
        corr=get(keys[i], keys[j])
        if(corr==None):
            document_list1=getDOI(keys[i])
            corr=len(set(document_list1).intersection(getDOI(keys[j])))/len(document_list1)
            insert(keys[i], keys[j], corr)
        if(corr>=corrThreshold):
            keywords[keys[i] + " " + keys[j]]=(keywords[keys[i]]+keywords[keys[j]])/2
            del keywords[keys[i]]
            del keywords[keys[j]]
        



