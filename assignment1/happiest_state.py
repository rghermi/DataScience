import sys
import re
import json

sent_file = open(sys.argv[1])
tweet_file = open(sys.argv[2])

scores = {} # initialize an empty dictionary 
states = {}

def writeDictionary():
   for line in sent_file:
       term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
       scores[term] = int(score)  # Convert the score to an integer.


def main():
   writeDictionary()
   #print scores.items()

   for tweetLine in tweet_file:     #read the file line by line
      #looping each tweet in the file   
      sentiment = 0.0
      tweet = json.loads(tweetLine)
      #print tweet     
      
      #if tweet.has_key("text"): 
      if tweet.has_key("place") and tweet.has_key("text"): 
         #if tweet["lang"] == "en" and tweet["place"] is not None :
         if tweet["place"] is not None : 
            #print tweet["lang"], tweet["place"], tweet["user"]
            #print tweet["user"]["location"]
            #print tweet["place"]
            if tweet["place"]["country_code"] == "US":  # filter out only US tweets
               if tweet["place"]["place_type"] == "city":
                  state = tweet["place"]["full_name"][-2:] 
                  #last two digits of the full_name when place_type is city is the state 
                            
                  #print state, tweet["text"]
                  for word in re.sub("[^\w]", " ", tweet["text"]).split():
                  #looping each word of the tweet 
                     #print word
                     encoded_word = word.encode('utf-8')
                     if scores.has_key(encoded_word):
                        sentiment += float(scores[word]) #sentiment of the tweet
                  if states.has_key(state):  #cumulate the sentiment by state in a dict
                     states[state] += sentiment                 
                  else:
                     states[state] = sentiment
                    
   sorted_states = sorted(states, key=states.get, reverse=True)
   # sort the dict by values
   #print sorted_states
   #for k in range(1):
   print sorted_states[0]
   


if __name__ == '__main__':
    main()
