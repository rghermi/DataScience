import sys
import json
import re
from collections import OrderedDict
import collections


tweet_file = open(sys.argv[1])

hashtag = {} # initialize an empty dictionary 


def main():

   for tweetLine in tweet_file:   #read the file line by line
      #looping each tweet in the file   
      tweet = json.loads(tweetLine)
   
      if tweet.has_key("text"):     # the text of the tweet
         for word in re.findall(r'[^\s!,.?@/":;0-9]+', tweet["text"], re.UNICODE):
            #looping each word of the tweet 
            if word[:1] == "#" and len(word)>1 :
               word = word[1:]
               if word in hashtag:
                  hashtag[word] += 1.0  
               else: 
                  count = 1.0
                  hashtag[word] = count 
   
   #sortedHashTag = sorted(hashtag, key=hashtag.get, reverse=True)
   orderedHash = OrderedDict (collections.Counter(hashtag).most_common(10))
   for w in orderedHash:
      print "%s %.1f" % (w, orderedHash[w])

if __name__ == '__main__':
    main()
