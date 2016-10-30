from collections import Counter
import sys

txtfile = open(sys.argv[1], "r")
resultfile = open(sys.argv[1]+'.result', "w")

wordcount = Counter(txtfile.read().split())
for item in wordcount.items(): resultfile.write("{0:30}\t{1:4}\n".format(*item))

txtfile.close()
resultfile.close()