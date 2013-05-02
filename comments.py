# comments for reddit terminal

#import
import os
import sys
import re
import urllib

#selcts post
def select():
  print 'Input number to view the comments'
  number = raw_input('--> ')
  return 25 - int(float(number))
  #if number >25:
  #  print 'Out of range'

#for parsing and print comments of post
def parsecomments(results, selction):
  link = results[selction]
  sitesearch = urllib.urlopen(link[2])
  sitehtml = sitesearch.read()
  comments = re.findall(r'<a href="http://www.reddit.com/user.+?>(\w+).+?<div class="md"><p>(.+?)</p>', sitehtml)
  comments.reverse()
  for comment in comments:
    print comment[0] + ': ' + comment[1] + '\n'