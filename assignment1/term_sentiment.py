import sys
import re
import json

sent_file = open(sys.argv[1])
tweet_file = open(sys.argv[2])

scores = {} # initialize an empty dictionary


def writeDictionary():
    for line in sent_file:
  	term, score  = line.split("\t")  # The file is tab-delimited. 						"\t" means "tab character"
  	scores[term] = int(score)  # Convert the score to an integer.


def main():
	writeDictionary()

for fileLine in tweet_file:   #read the file line by line
   sentiment = 0.0
   tweet = json.loads(fileLine)

   if tweet.has_key("text"):
        for word in re.sub("[^\w]", " ", tweet["text"]).split(): 
             if word.encode('utf-8') in scores.keys():
		sentiment = sentiment + float(scores[word])
                print sentiment 


if __name__ == '__main__':
    main()
