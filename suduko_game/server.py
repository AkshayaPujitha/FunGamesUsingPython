from flask import Flask,render_template,request
from validation import *

app=Flask(__name__)

@app.route("/")
def home():
    data={}
    return render_template("suduko.html",data=data)

@app.route("/submit",methods=["POST"])
def submit():
    dic={}
    l=['1','2','3','4','5','6','7','8','9']
    for i in range(1,83):
        x="num"+str(i)
        num=request.form.get(str(i))
        if num  in l:
            dic[x]=num
    #print(dic)
        
    data=dic
    return render_template("suduko.html",data=data)

if __name__=="__main__":
    app.run(debug=True)


