import feedparser
import re
import time
def getwordcounts(url):
# Parse the feed
 d=feedparser.parse(url)
 wc={}
# Loop over all the entries
 for e in d.entries:
  #print(e.keys())
  if 'summary' in e: summary=e.summary
  else: summary=e.description
# Extract a list of words
  words=getwords(e.title+' '+summary)
  for word in words:
   wc.setdefault(word,0)
   wc[word]+=1
 return d.feed.title,wc

def getwords(html):
# Remove all the HTML tags
 txt=re.compile(r'<[^>]+>').sub('',html)
# Split words by all non-alpha characters
 words=re.compile(r'[^A-Z^a-z]+').split(txt)
# Convert to lowercase
 return [word.lower( ) for word in words if word!='']


if __name__ == "__main__": 
 #title,count=getwordcounts("http://rss.cnn.com/rss/cnn_topstories.rss");
 #print title
 #for k,v in count.items():
 # print k+":"+str(v)+"\n"
  
 apcount={}
 wordcounts={}
 ll = open('feedlist.txt','r')
 f = ll.readlines()
 for feedurl in f:
  print(feedurl)
  #time.sleep(1)
  title,wc=getwordcounts(feedurl)
  wordcounts[title]=wc
  for word,count in wc.items():
   apcount.setdefault(word,0)
   if count >1:
    apcount[word]+=1
 wordlist=[]
 feedlist=0
 for w,bc in apcount.items( ):
  frac=float(bc)/len(wordcounts)
  if frac>0.1 and frac<0.5: wordlist.append(w)
 #writing dataset to output file
 out=open('blogdata.ods','w')
 out.write("Blog")
 for word in wordlist: out.write('\t%s' %word)
 out.write('\n')
 for blog,wc in wordcounts.items():
  out.write(blog)
  for word in wordlist:
   if word in wc: out.write('\t%d'%wc[word])
   else: out.write('\t0')
  out.write('\n')
 out.close() 
