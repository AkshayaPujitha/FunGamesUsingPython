from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def home():
    data={}
    return render_template("suduko.html",data=data)

@app.route("/submit",methods=["POST"])
def submit():
    num2=request.form.get("2")
    num5=request.form.get("5")
    data={'num2':num2,'num5':num5}
    print(num2)
    print(num5)
    return render_template("suduko.html",data=data)

if __name__=="__main__":
    app.run(debug=True)


