#import re

#pattern = re.compile(r"\w")
# Let's feed in some strings to match
#string = "regex is awesome!"
# Then call a matching method to match our pattern
#result = pattern.match(string)
# print result.group()  # will print out 'r'
import re
# allinform = re.findall(
# "inform", "we need to inform him  with latest information")
# for i in allinform:
#   print(i)
#str = "wen need all inform with lates infomation"
# or i in re.finditer("inform", str):
#loctup = i.span()
# print(loctup)
str = "sat,hat ,mat ,cat ,pat"
allstr = re.findall("[smc]at", str)
