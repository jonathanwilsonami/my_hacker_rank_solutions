import re

pattern = re.compile('(?<=<)\s*\w+')    

testStr1 = """<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p>"""
testStr2 = """<div class="more-info"><a href="http://www.quackit.com/html/examples/html_links_examples.cfm">More Link Examples...</a></div>"""

lineNum = int(input())

#Using a list comprehension - This is more optimized by a few hundred nanoseconds (this of course depends on how many lines we use). 
#Not much improvment but looks cleaner.  
#Time: 6.00814819336e-05
matchesList = [pattern.findall(input()) for i in range(lineNum)]
matchesList = [val for sublist in matchesList for val in sublist]#flatten list

#Using a for loop
#for i in range(lineNum):   
 #   lineString = input()
  #  inputList = pattern.findall(lineString) 
   # matchesList = matchesList + inputList    
#Time: 6.29425048828e-05

tagsSet = set(matchesList)
tags = ";".join(sorted(tagsSet))
print(tags)
