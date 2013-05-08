import urllib
import json

response = urllib.urlopen('http://search.twitter.com/search.json?q=microsoft')

pyresponse = json.load(response)

# print pyresponse.keys()

# print pyresponse["page"]

# print pyresponse["results"]

results = pyresponse["results"]

# print results[0]

# print type(results[0])

# print results[0].keys()

# print results[0]["text"]

for i in range(10):
	unicode_string = results[i]["text"]
	encoded_string = unicode_string.encode("utf-8")
	print encoded_string

