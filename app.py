from flask import Flask, render_template, request
import hashlib
app=Flask(__name__)


@app.route("/")
def disp_loginpage():
    print "\n\n\n"
    print ":::DIAG::: this Flask obj"
    print app
    print ":::DIAG::: this request obj"
    print request
    print ":::DIAG::: this request.headers obj"
    print request.headers
    print ":::DIAG::: this request.method obj"
    print request.method
    print ":::DIAG::: this request.args obj"
    print request.args
    print ":::DIAG::: this request.form obj"
    print request.form
    return render_template("input.html")

@app.route("/auth", methods=['POST'])
def disp_auth():
    print "\n\n\n"
    print ":::DIAG::: this Flask obj"
    print app
    print ":::DIAG::: this request obj"
    print request
    print ":::DIAG::: this request.headers obj"
    print request.headers
    print ":::DIAG::: this request.method obj"
    print request.method
    print ":::DIAG::: this request.form obj"
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
