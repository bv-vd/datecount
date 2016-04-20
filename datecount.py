# coding: utf-8

# Find the dates on a webpage

from urllib import urlopen
import re
import collections

url = "https://en.wikipedia.org/wiki/September_11_attacks"
pattern = "(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[.a-z]* [0-9][0-9]?(?:, (?:19|20)[0-9]{2})?"
NUM_MOST_FREQ = 20

link = urlopen(url)
htmlText =  link.read()
link.close()

dates = re.findall(pattern, htmlText)
print("\nPage: '%s'" % url)
print("%s dates found" % len(dates))

counter = collections.Counter(dates)
print("%s are unique\n" % len(counter))

freq = counter.most_common(NUM_MOST_FREQ)
print("Most frequently appeared:")
for (k, v) in freq:
	print("%5d : %-20s" % (v, k))

# print dates
