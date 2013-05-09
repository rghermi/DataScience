import json
import sys
import re

tweet_file = open(sys.argv[1])

frequency = {} # initialize an empty dictionary

def main():
    
   for tweetLine in tweet_file:
      tweet = json.loads(tweetLine)
      if tweet.has_key("text"):
       #  print tweet["text"]  # print the whole tweet 	
         string = tweet["text"]   
         for word in re.findall(r'[^\s!,.?@/":;0-9]+', string, re.UNICODE):
            #re.findall(r"\w+|[^\w\s]", string, re.UNICODE):
            #re.split("(\W+)", string):
             
            print word



if __name__ == '__main__':
    main()
