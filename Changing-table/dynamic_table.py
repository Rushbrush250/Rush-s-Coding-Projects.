from flask import Flask, render_template, request, jsonify
import pandas as pd
import os
import sys
import time


tableapp = Flask(__name__)
datatable = pd.read_csv('dataframe.csv')

dt0 = datatable.iloc[0].item()
dt1 = datatable.iloc[1].item()
dt2 = datatable.iloc[2].item()
dt3 = datatable.iloc[3].item()
dt4 = datatable.iloc[4].item()
dt5 = datatable.iloc[5].item()
dt6 = datatable.iloc[6].item()
dt7 = datatable.iloc[7].item()
dt8 = datatable.iloc[8].item()
dt9 = datatable.iloc[9].item()

@tableapp.route("/")
def table():
   return render_template("data_table.html", dt0 = dt0, 
                          dt1 = dt1, dt2 = dt2, dt3 = dt3, dt4 = dt4, dt5 = dt5, dt6 = dt6,
                          dt7 = dt7, dt8 = dt8, dt9 = dt9)


@tableapp.route("/update", methods=['POST'])
def update():
    given_data = request.get_json()
    given_text = given_data.get('texts')
    given_number = given_data.get('intver')
    final_number = given_number - 1
    change = given_text
    datatable.iloc[final_number] = change
    datatable.to_csv('dataframe.csv', index=False)
    return "hi"
    

@tableapp.route("/reload")
def reload():
    return render_template("data_table.html", dt0 = datatable.iloc[0].item(), 
                          dt1 = datatable.iloc[1].item(), dt2 = datatable.iloc[2].item(), dt3 = datatable.iloc[3].item(), 
                          dt4 = datatable.iloc[4].item(), dt5 = datatable.iloc[5].item(), dt6 = datatable.iloc[6].item(),
                          dt7 = datatable.iloc[7].item(), dt8 = datatable.iloc[8], dt9 = datatable.iloc[9].item())


if __name__ == "__main__":
    tableapp.run(debug=True)
