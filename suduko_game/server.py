from flask import Flask,render_template,request
from validation import *

app=Flask(__name__)

@app.route("/")
def home():
    data={}
    
    error={}
    return render_template("suduko.html",data=data,error=error)

validated=[]
existed={}

@app.route("/submit",methods=["POST"])

def submit():
    global validated
    global existed
    dic={}
    data={}
    l=['1','2','3','4','5','6','7','8','9']
    
    for i in range(1,83):
        x="num"+str(i)
        num=request.form.get(str(i))
        if (len(existed)==0 and num in l) :
            existed[x]=num
            dic[x]=num
        if x in existed and num=='':
            del existed[x]
        

        elif num  in l :
            try:
                num1=existed[x]
                if num1!=num:
                    dic[x]=num
                    existed[x]=num
                else:
                    pass
            except:
                dic[x]=num
                existed[x]=num
    
    
    print(dic)
    #print(existed)
    #print(data)
    correct,lis=validate(existed)
    print(lis)
    #print(num)
    #print(validated)
    print(correct)
    error={}
    if correct==False:
       color="background-color:#f56f6f"
       for i in lis:
           error[i]=color
       
       
    else:
       color=""


        
    data=existed
    return render_template("suduko.html",data=data,error=error)

if __name__=="__main__":
    app.run(debug=True)


