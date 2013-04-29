#reddit py

#browse reddit subreddits or search in the terminal and get links to the link & comments
#next on todo: let user browse comments in terminal by selecting post 

#imports
import sys
import re
import os
import urllib

#receives url, then opens, reads, then parse w/ regexp to find title, link, and comment link
def parsereddit(httpquery):
  sitesearch = urllib.urlopen(httpquery)
  sitehtml = sitesearch.read()
  #stores in tuples of title, link, comments, and comment count
  links = re.findall(r'\<a class=\"title \" href=\"(\S+)\" >(.+?)<.+?\<a class=\"comments\" href=\"(\S+)\".+?>(\d+)', sitehtml)
  for link in links:
    if link[0].startswith('/r/'):
      link = [('http://www.reddit.com' + link[0]), (link[1]), (link[2]), (link[3])]
    print link[1]
    #if comments same as link (self post)
    if link[0] == link[2]:
      print 'self post/comments: ' + link[0] + '\n'
    else:
      print 'link: ' + link[0]
      print 'comments (' + link[3] + '): ' + link[2] + '\n'
  print 'Showing results for: ' + httpquery

#passend search args list and makes search url
def search(query):
  fullquery = ''
  for terms in query:
    fullquery += terms + '+'
  httpquery = 'http://www.reddit.com/search?q=' + fullquery
  parsereddit(httpquery)
  
#passed r/(subreddit) and makes subreddit url
def subreddit(sub):
  #if sub[1].isdigit():
  #  httpquery = 'http://www.reddit.com/' + sub[0] + '/?count=' + str(sub[1]*25)
  httpquery = 'http://www.reddit.com/' + sub[0]
  parsereddit(httpquery)

def main():
  args= sys.argv[1:]
  #determins if search, subreddit, or blank (frontpage) and calls approriate methods
  if not args:
    args = ['']
    subreddit(args)
  if args[0] == 'search':
    args = args[1:]
    search(args)
  if args[0].startswith('r/'):
    subreddit(args)

if __name__ == '__main__':
  main()