import sys
import re
import json

sent_file = open(sys.argv[1])
tweet_file = open(sys.argv[2])

scores = {} # initialize an empty dictionary


def writeDictionary():
    for line in sent_file:
       term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
       scores[term] = int(score)  # Convert the score to an integer.


def main():
   writeDictionary()
   #print scores.items()

for tweetLine in tweet_file:   #read the file line by line
   #looping each tweet in the file   
   sentiment = 0.0
   tweet = json.loads(tweetLine)
   
   if tweet.has_key("text"):     # the text of the tweet
      #print tweet["text"]   
      for word in re.sub("[^\w]", " ", tweet["text"]).split():
      #looping each word of the tweet 
         print word
         #if word.encode('utf-8') in scores.keys():
         if scores.has_key(word.encode('utf-8')):
            sentiment += float(scores[word])
            print "ha entrado"
      #print sentiment 


if __name__ == '__main__':
    main()
