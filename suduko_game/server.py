from flask import Flask,render_template,request
from validation import *

app=Flask(__name__)

@app.route("/")
def home():
    data={}
    color={}
    return render_template("suduko.html",data=data,color=color)

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
    print(existed)
    #print(data)
    correct,lis=validate(dic,validated,existed)
    #print(num)
    #print(validated)
    print(correct)
    if correct==False:
       print(lis)
       color="background-color:#f56f6f"
       
    else:
       for i in lis:
           validated.append(i)
       color=""


        
    data=existed
    return render_template("suduko.html",data=data,color=color)

if __name__=="__main__":
    app.run(debug=True)


