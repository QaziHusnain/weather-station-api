from flask import Flask,render_template
import pandas as pd
import numpy as np
from datetime import datetime
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/api/v1/<station>/<date>")
def about(station,date):
    filepath="data/TG_STAID"+str(station).zfill(6)+".txt"
    df=pd.read_csv(filepath,skiprows=20,parse_dates=["    DATE"])
    df["TG0"] = df["   TG"].mask(df["   TG"] == -9999, np.nan)
    df["TG1"]=df["TG0"] /10

    date_obj = datetime.strptime(date, "%Y%m%d")
    formatted_date = date_obj.strftime("%Y-%m-%d")

    temperature=df.loc[df["    DATE"]==formatted_date]["TG1"].squeeze()
    tem_dict={"station":station,"date":formatted_date,"temp":temperature}
    return tem_dict
if __name__=="__main__":
    app.run(debug=True)