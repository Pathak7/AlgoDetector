from bs4 import BeautifulSoup
import pandas as pd
from requests import *
import sys
from random import *
f=open("CNNBSWhile.doc","a")
sys.stdout=f;
#page=get("http://codeforces.com/problemset/status/946/problem/G")
#page=get("http://codeforces.com/problemset/status/883/problem/I")
#page=get("http://codeforces.com/problemset/status/847/problem/E")
#page=get("http://codeforces.com/problemset/status/812/problem/C")
#page=get("http://codeforces.com/problemset/status/932/problem/B")
#page=get("http://codeforces.com/problemset/status/930/problem/B")
page=get("http://codeforces.com/problemset/status/946/problem/E")
soup=BeautifulSoup(page.content,"html.parser")
#print(soup.prettify())
ans=soup.find_all("a", class_="view-source")
ans1=ans
totalCodes=50
t="http://www.codeforces.com"
count=0
for i in ans1:
    url=t+i["href"]
    page=get(url)
    soup=BeautifulSoup(page.content,"html.parser")
    #=(soup.prettify())
    ans=soup.find_all("pre", class_="prettyprint lang-cpp program-source")

    ans=list(ans);
    #print(ans)
    if(len(ans)!=0):
        ans=ans[0]
        count=count+1;
        #print(ans)
        prev=0
        for i in ans:
            code=i
            df = pd.DataFrame({'A':[code]})
            #print(df)
            df = df.replace('\n',' ', regex=True)
            df = df.replace('\t',' ', regex=True)
            df = df.replace('\r',' ', regex=True)
            df = df.replace(',',' ', regex=True)
            
            #print (df)
            c=0
            for i in df['A']:
                c=0
                aa=i.split()
                ff=0
                #print(aa)
                for it in aa:
                    if "while" in it:
                        ff=1
                        #print("While found at",it)
                    if ff==1:
                        for xx in it:
                            
                            if c<=100:
                                print(ord(xx),end=' ')
                                c=c+1
                    if "lower_bound" in it :
                        for xx in it:
                            
                            if c<=100:
                                print(ord(xx),end=' ')
                                c=c+1
                    if "upper_bound" in it :
                        for xx in it:
                            
                            if c<=100:
                                print(ord(xx),end=' ')
                                c=c+1
                        
                
                """for x in i:
                    if(c==500):
                        break
                    try:
                        if(x==' '):
                            continue;
                        #print(ord(x),end=' ')
                    except:
                        
                        print(ord('?'),end=' ')
                    c=c+1
                while(c<=500):
                    #print(randint(0,140),end=' ')
                    c=c+1"""
            while(c<=100):
                print(0,end=' ')
                c=c+1
            print(",0")

            """for word in code:
                try:
                    if "\n" in word:
                        print(' ',end='')
                        continue
                    if "\t" in word:
                        print(' ',end='')
                        continue
                    if word!=',' :
                        if word!=' ':
                            print(word,end='')
                            prev=0
                        elif word==' ' and prev==0:
                            print(word,end='')
                            prev=1
                            
                        
                    else:
                        print(' ',end='')
                        
                    
                except:
                    print('?',end=' ')
            print(',yes')"""


f.close();

            
