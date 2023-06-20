from flask import Flask,render_template
app=Flask("Website")
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/api/v1/<station>/<date>")
def about(station,date):
    temperature=23
    tem_dict={"station":station,"date":date,"temp":temperature}
    return tem_dict
app.run(debug=True)