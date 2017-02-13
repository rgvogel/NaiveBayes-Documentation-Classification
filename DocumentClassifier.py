# Project: Naive Bayes: Document Classifier 
#
# Author: Roderick Vogel
# Purpose: Program trains a program ( using Naive Bayes method) to reconize text based on the text category and the number of words of each text that occur in this category. Then the training is tested based on the test documents. 

import copy 
import math 
import time
import heapq

def Training():
    
   
    trained = {}
    counter = {}
    CatDict = {}
    wordDict = {}
    wordDictT = {}
    train = "trainingStem.txt"
    
# create dictionary for each category holding all text in category  and dictionary of all unique words total text
    with open(train, 'r') as f:

        for line in f:
            splitline = line.split()
            words = splitline[1:]

            if splitline[0] not in CatDict:
                CatDict[splitline[0]] = []
                CatDict[splitline[0]].append(words)

            else:
                CatDict[splitline[0]].append(words)
            
            for i in words: 

                if i not in wordDict:
                    wordDict[i] = 0
                    
    #iterate through each category
    for c in CatDict:
        
            #print (c, w)
        # set word counter for each category to a word dictionary 
        counter[c] = copy.deepcopy(wordDict)
        # set the resulting trained values for each categorie to word dictionary also
        trained[c] = copy.deepcopy(wordDict)

    #iterate through each category
    for i in CatDict:
        #set count for total  number of words in category to 0
        count = 0
# iterate through each list in category
        for x in CatDict[i]:
# iterate through each word in each list
            for c in x:
      
                #count number of time word appears in category
                counter[i][c] = int(counter[i][c]) +1
                # count total number of words in category
                count = count +1
        
        # go through each word count in category and calculate how common it is in text
        for s in  counter[i]:
            q = counter[i][s] +1
            trained[i][s] = float(q)/(count+ len(wordDict))
           
        
    #for i in trained:
         #count = 0
         #for s in trained[i]:
          #   count = trained[i][s] + count
         #print(i,count)
    return trained

def test(trainDict):
   testDict = {}
   ratioDict = {}
   testCatDict = {}
   # stores all ratios of the text to number of docs
   docRatioList = [float(585)/11293,float(591)/11293,float(598)/11293,float(594)/11293,float(593)/11293,float(564)/11293,float(590)/11293,float(595)/11293,float(598)/11293,float(480)/11293,float(377)/11293,float(578)/11293,float(597)/11293,float(600)/11293,float(584)/11293,float(594)/11293,float(465)/11293,float(572)/11293,float(593)/11293,float(545)/11293]

   
   test = "testStem.txt"
   count = 0
   

   #store value ratio cj value in test dict
   for x in trainDict: 
        ratioDict[x] = docRatioList[count]
        count = count +1
       
   total = 7527
   Pass = 0
   count = 0
   with open(test, 'r') as f:
       for line in f:
            
            splitline = line.split()
            words = splitline[1:]
            # set the test dictionary to zero clear dictionary of previous test
            for x in trainDict:
                testDict[x] = 0
                
            # runs through each category
            for p in testDict:
                # runs through each word adds a log of the word probablity for the specific category
                for w in words:
                    
                    if w in trainDict[p]:
                        testDict[p] = math.log(trainDict[p][w]) +testDict[p]
                # add log of the ratio of the occurence of the text to the dictionary 
                testDict[p] = math.log(ratioDict[p]) + testDict[p]
                
            # finds the max value of the test dictionary (max = predicted category)
            maxCat = max(testDict, key=testDict.get)
            
            # adds one to Pass if the category was predicted correctly 
            if maxCat == splitline[0]:
                Pass = Pass +1
    # calculates the number of categories correctly predicted vs total number of values 
   passRatio = float(Pass)/total
   print passRatio

def maxInc (trainDict):
    x = copy.deepcopy(trainDict)
    for i in trainDict:
        keyMax = heapq.nlargest(100, trainDict[i], key= trainDict[i].get)
        for k in keyMax:
            x[i][k] = trainDict[i][k]*5

    return x
if __name__ == "__main__":

    start = time.time()
    trained = {}
    improved = {}
    trained = Training()
    improved = maxInc(trained)
    test(improved)
    end = time.time()
    #time in seconds for program to run
    print(end- start)
