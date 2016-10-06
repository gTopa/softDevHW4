from flask import Flask, render_template, request, redirect, url_for, session
import hashlib

app=Flask(__name__)

@app.route("/jacobo")
def js():
    print url_for("disp_loginpage")
    return redirect("http://xkcd.com")

@app.route("/")
def disp_loginpage():
    return render_template("input.html")

@app.route("/auth", methods=['POST'])
def disp_auth():
    myHashObj = hashlib.sha1()
    myHashObj.update(request.form['passwd'])
    if 'login' in request.form.keys():
        f = open('data/loginInfo.csv', 'r')
        userPass = f.read()
        f.close()
        userPass=userPass.split('\n')[0:-1]
        userPassDic={}
        for stuff in userPass:
            stuff=stuff.split(',')
            userPassDic[stuff[0]]=stuff[1]
        if request.form['username'] in userPassDic.keys():
            if myHashObj.hexdigest()==userPassDic[request.form['username']]:
                return render_template("auth.html", status='success')
        return render_template("auth.html", status='fail')
    else:
        f = open('data/loginInfo.csv', 'a')
        f.write(request.form['username']+','+myHashObj.hexdigest()+'\n')
        f.close()
        return render_template("register.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
