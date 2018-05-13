from flask import Flask, render_template,request,redirect,url_for
import pandas as pd 
import numpy as np
import pickle
from keras.models import model_from_json
import h5py
from keras.models import load_model
from keras.models import model_from_json
app=Flask(__name__)
# load json and create model
json_file = open('Segtree_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("Segtree_model.h5")
print("Loaded model from disk")
#binary_model=load_model("segmentTree_model.h5")
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/selection',methods=["POST"])
def selectt():
    global code;
    code=request.form.get('Code')
    algoType=request.form.get('algoType')
    if(algoType=="fastExpo"):
        return redirect("/FASTEXPO")
    
    if(algoType=="segmentTree"):
        return redirect("/SEGTREE")
    if(algoType=="binarySearch"):
        return redirect("/BINARYSEARCH")
    if(algoType=="bfs"):
        return redirect("/BFS")
    
            

    return algoType

@app.route('/SEGTREE',methods=["GET"])
def segtree():
    global binary_model
    tc=901
    def cleanData(c):
        code=c
        df1 = pd.DataFrame({'A':[code]})
                
        df1 = df1.replace('\n',' ', regex=True)
        df1 = df1.replace('\t',' ', regex=True)
        df1 = df1.replace('\r',' ', regex=True)
        df1 = df1.replace(',',' ', regex=True)
        c=0
        tmp=""
        for i in df1['A']:
                    c=0
                    aa=i.split()
                    ff=0
                    #print(aa)
                    for it in aa:
                        if "const" or "int" or "void" or "ll" or "long" or "priority" or "vector" or "set" in it:
                            ff=1
                            #print("While found at",it)
                        if ff==1:
                            for xx in it:
                                
                                if c<=900:
                                    tmp=tmp+str(ord(xx))+' '
                                    #print(ord(xx),end=' ')
                                    c=c+1
                        if "query" in it :
                            for xx in it:
                                
                                if c<=900:
                                    tmp=tmp+str(ord(xx))+' '
                                    #print(ord(xx),end=' ')
                                    c=c+1
                        
                    while(c<=900):
                        tmp=tmp+"0 "
                        #print(0,end=' ')
                        c=c+1
                            
                   
                
        #print(ff)          
        return tmp
                
    
    
        
              
    def makeCNNReady(c):
        tmp=[]
        tmp=c.split()
        aa=np.array(tmp)
        aa=aa.astype('float32')
        
        aa=aa.reshape(tc,1)
        aa=aa.reshape(-1,tc,1,1)
        aa=aa/155
        return aa
    def getPrediction(c):
        
        pred=loaded_model.predict(makeCNNReady(cleanData(c)))
        print(pred)
        #cc=np.argmax(np.round(pred),axis=1)
        if pred[0][1]>=pred[0][0]:
            return "yes"
        else:
            return "no"
    print("hey");
  
    
    
    print(code)
    

    
    return render_template("answer.html",AlgoName="SEGMENT TREE", result=getPrediction(code))


@app.route('/FASTEXPO',methods=["GET"])
def fastexpo():
    tc=201
    def cleanData(c):
        code=c
        df1 = pd.DataFrame({'A':[code]})
                
        df1 = df1.replace('\n',' ', regex=True)
        df1 = df1.replace('\t',' ', regex=True)
        df1 = df1.replace('\r',' ', regex=True)
        df1 = df1.replace(',',' ', regex=True)
        c=0
        tmp=""
        for i in df1['A']:
                    c=0
                    aa=i.split()
                    ff=0
                    #print(aa)
                    for it in aa:
                        #print(it)
                        if ("(ll" in it and "for" not in it and "while" not in it) or ( "(long" in it and "for" not in it and "while" not in it)  or ("(int" in it and "for" not in it and "while" not in it)  :
                            #print("First",it)
                            ff=1
                            #print("While found at",it)
                        if ff==1:
                            for xx in it:
                                
                                if c<=200:
                                    tmp=tmp+str(ord(xx))+' '
                                    #print(ord(xx),end=' ')
                                    c=c+1
                        
                    while(c<=200):
                        tmp=tmp+"0 "
                        #print(0,end=' ')
                        c=c+1
                        
               
            
           
        return tmp
    def makeCNNReady(c):
        tmp=[]
        tmp=c.split()
        aa=np.array(tmp)
        aa=aa.astype('float32')
        
        aa=aa.reshape(tc,1)
        aa=aa.reshape(-1,tc,1,1)
        aa=aa/155
        return aa
    def getPrediction(c):
        fastexpo_model=load_model("FASTEXPO_model.h5")
        pred=fastexpo_model.predict(makeCNNReady(cleanData(c)))
        print(pred)
        #cc=np.argmax(np.round(pred),axis=1)
        if pred[0][1]>=pred[0][0]:
            return "yes"
        else:
            return "no"
    
    return render_template("answer.html",AlgoName="Fast exponentiation", result=getPrediction(code))



@app.route('/BINARYSEARCH',methods=["GET"])
def binarySearch():
    tc=101
    def cleanData(c):
        code=c
        df1 = pd.DataFrame({'A':[code]})
                
        df1 = df1.replace('\n',' ', regex=True)
        df1 = df1.replace('\t',' ', regex=True)
        df1 = df1.replace('\r',' ', regex=True)
        df1 = df1.replace(',',' ', regex=True)
        c=0
        tmp=""
        for i in df1['A']:
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
                                    tmp=tmp+str(ord(xx))+' '
                                    #print(ord(xx),end=' ')
                                    c=c+1
                        if "lower_bound" in it :
                            for xx in it:
                                
                                if c<=100:
                                    tmp=tmp+str(ord(xx))+' '
                                    #print(ord(xx),end=' ')
                                    c=c+1
                        if "upper_bound" in it :
                            for xx in it:
                                
                                if c<=100:
                                    tmp=tmp+str(ord(xx))+' '
                                    #print(ord(xx),end=' ')
                                    c=c+1
                    while(c<=100):
                        tmp=tmp+"0 "
                        #print(0,end=' ')
                        c=c+1
                            
                   
                
        #print(ff)          
        return tmp
            
    
    
       
               
            
           
        
    def makeCNNReady(c):
        tmp=[]
        tmp=c.split()
        aa=np.array(tmp)
        aa=aa.astype('float32')
        
        aa=aa.reshape(tc,1)
        aa=aa.reshape(-1,tc,1,1)
        aa=aa/155
        return aa
    def getPrediction(c):
        binary_model=load_model("binary_model.h5")
        pred=binary_model.predict(makeCNNReady(cleanData(c)))
        print(pred)
        #cc=np.argmax(np.round(pred),axis=1)
        if pred[0][1]>=pred[0][0]:
            return "yes"
        else:
            return "no"
    
    return render_template("answer.html",AlgoName="Binary Search", result=getPrediction(code))
    


@app.route('/BFS',methods=["GET"])
def bfs():
    tc=551
    def cleanData(c):
        code=c
        df1 = pd.DataFrame({'A':[code]})
                
        df1 = df1.replace('\n',' ', regex=True)
        df1 = df1.replace('\t',' ', regex=True)
        df1 = df1.replace('\r',' ', regex=True)
        df1 = df1.replace(',',' ', regex=True)
        c=0
        tmp=""
        for i in df1['A']:
                    c=0
                    aa=i.split()
                    ff=0
                    #print(aa)
                    for it in aa:
                        if "int" or "void" in it:
                            ff=1
                            #print("While found at",it)
                        if ff==1:
                            for xx in it:
                                
                                if c<=550:
                                    tmp=tmp+str(ord(xx))+' '
                                    #print(ord(xx),end=' ')
                                    c=c+1
                        
                    while(c<=550):
                        tmp=tmp+"0 "
                        #print(0,end=' ')
                        c=c+1
                            
                   
                
        #print(ff)          
        return tmp
            
    
    
    
       
               
            
           
        
    def makeCNNReady(c):
        tmp=[]
        tmp=c.split()
        aa=np.array(tmp)
        aa=aa.astype('float32')
        
        aa=aa.reshape(tc,1)
        aa=aa.reshape(-1,tc,1,1)
        aa=aa/155
        return aa
    def getPrediction(c):
        binary_model=load_model("BFS_model.h5")
        pred=binary_model.predict(makeCNNReady(cleanData(c)))
        print(pred)
        #cc=np.argmax(np.round(pred),axis=1)
        if pred[0][1]>=pred[0][0]:
            return "yes"
        else:
            return "no"
    
    return render_template("answer.html",AlgoName="BFS", result=getPrediction(code))
    
    
                
    
    

app.run(port=5176,threaded=False)
