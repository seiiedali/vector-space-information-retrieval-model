import os
import math
import operator
from typing import Dict, List, Any


def remove_punctuation(s):
    punctuation = "0123456789!()-[]{};:'\"\,<>./?@#$%^&*_~"
    no_punct = ""
    for c in s:
        if c not in punctuation:
            no_punct += c
    return no_punct


indexTable = dict()
for root, dirs, files in os.walk("./Docs/"):
    for filename in files:
        path = "./Docs/" + filename
        with open(path, "r") as content:
            content = content.read().replace('\n', ' ')
            cleanData = remove_punctuation(content).lower()
            tokens = cleanData.split()
            allFiles[filename] = dict()
            for term in tokens:
                if term in allFiles[filename]:
                    allFiles[filename][term] += 1
                else:
                    allFiles[filename][term] = 1
            uniqeTokens = list(dict.fromkeys(tokens))
            for word in uniqeTokens:
                if word in indexTable:
                    indexTable[word] += 1
                else:
                    indexTable[word] = 1
tfIdf = dict()
for filename in :
    # print(filename)
    tfIdf[filename] = dict()
    for word in allFiles[filename]:
        tfIdf[filename][word] = allFiles[filename][word] * \
            math.log10(allFiles.__len__()/indexTable[word])

for item in tfIdf:
    print("in a file name " + str(item) + " --> " + str(tfIdf[item]))
for item in indexTable:
    print("\"" + str(item) + "\"" +
          " wtih the weight of: " + str(indexTable[item]))

print("dictionary is made, data is loaded ...")


query = input("enter your query").lower()
queryTokens = query.split()

queryVector = {i: queryTokens.count(i) for i in queryTokens}

for item in queryVector:
    if item in indexTable:
        queryVector[item] = queryVector[item] * \
            math.log10(allFiles.__len__()+1/indexTable[item]+1)
    else:
        queryVector[item] = queryVector[item] * \
            math.log10(allFiles.__len__() + 1)

print(queryVector)

finalTable = dict()
finalQuery = dict()
for filename in allFiles:
    finalTable[filename] = dict()
    for word in indexTable:
        if word in allFiles[filename]:
            finalTable[filename][word] = tfIdf[filename][word]
        else:
            finalTable[filename][word] = 0
        if word in queryVector:
            finalQuery[word] = queryVector[word]
        else:
            finalQuery[word] = 0
for item in finalTable:
    print(finalTable[item])

rank = dict()
print("the ranked list due to query would be:")
for filename in finalTable:
    innerProduct = 0
    docValue = 0
    queryValue = 0
    for word in finalTable[filename]:
        innerProduct += finalTable[filename][word] * finalQuery[word]
        docValue += math.sqrt(finalTable[filename][word] ** 2)
        queryValue += math.sqrt(finalQuery[word] ** 2)
    rank[filename] = innerProduct / (docValue * queryValue)

ranklist = sorted(rank.items(), key=operator.itemgetter(1), reverse=True)
counter = 1
for value in ranklist:
    print(str(counter) + ". " + str(value))
    counter += 1
