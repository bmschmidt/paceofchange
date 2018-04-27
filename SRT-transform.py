import glob
import sys
import os
import numpy as np

from SRP import SRP

hasher = SRP(6400)

def standardize_word(word):
    """
    They have some funny conventions involving brackets.
    """
    if word.find("|")==-1:
        return word
    if word=="|":
        return word

    word = word.strip("|")
    word.replace("arabic","1")
    word.replace("+digit","11")
    word.replace("digit","1")
    return word

try:
    os.makedirs("SRPs")
except:
    pass
try:
    os.makedirs("logSRPs")
except:
    pass

try:
    os.makedirs("littleLogSRPs")
    os.makedirs("littleSRPs")
except:
    pass


for file in glob.glob("poems/*"):
    words = []
    counts = []
    doc = open(file)
    for line in doc:
        (word,count) = line.split("\t")
        word = standardize_word(word)
        try:
            words.append(word.decode("utf-8"))
        except AttributeError:
            # Some 2/3 mucking
            words.append(word)
        counts.append(int(count))

    scores = hasher.stable_transform(words,counts)
    scores = scores.astype(np.float64)
    scores = np.divide(scores,np.linalg.norm(scores))

    newfile = file.replace("poems/","SRPs/")
    with open(newfile,"w") as f:
        for i in range(len(scores)):
            f.write("V%i\t%s\n" %(i,str(scores[i])))

    scores = hasher.stable_transform(words,counts,log=False)
    scores = scores.astype(np.float64)
    scores = np.divide(scores,np.linalg.norm(scores))

    newfile = file.replace("poems/","littleSRPs/")
    with open(newfile,"w") as f:
        for i in range(len(scores)):
            f.write("V%i\t%s\n" %(i,str(scores[i])))
            
    log_scores = hasher.stable_transform(words,counts,log=True)    
    newfile = file.replace("poems/","littleLogSRPs/")
    with open(newfile,"w") as f:
        for i in range(len(log_scores)):
            f.write("V%i\t%s\n" %(i,str(log_scores[i])))
    
