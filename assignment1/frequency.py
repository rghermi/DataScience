import json
import sys
import re

tweet_file = open(sys.argv[1])   


def main():
   frequency = {} # initialize an empty dictionary
   totWord = 0.0  # count the total number of words in tweets
   for tweetLine in tweet_file:
      #looping each tweet in the file
      tweet = json.loads(tweetLine)
      if tweet.has_key("text"):
       #  print tweet["text"]  # print the whole tweet 	
         string = tweet["text"]   
         for word in re.findall(r'[^\s!,.?@/":;0-9]+', string, re.UNICODE):
            #looping each word in the tweet
            #re.findall(r"\w+|[^\w\s]", string, re.UNICODE):
            #re.split("(\W+)", string):
            totWord = totWord +1
            if frequency.has_key(word):
               frequency[word] = int(frequency[word] + 1)
               
            else:
               frequency[word] = int(1)
   
   keys = frequency.keys()
   values = frequency.values() 

   #for keys,values in frequency.items():
      
   for w in sorted(frequency, key=frequency.get, reverse=True):
      print "%s %.6f" % (w.encode("utf-8"), frequency[w]/totWord)


if __name__ == '__main__':
    main()
