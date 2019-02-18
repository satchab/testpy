from flask import Flask
import json
import requests

#thread
import threading

#database
import mysql.connector
import json

def printit():
    threading.Timer(1.0, printit).start()
    
    r = requests.get(url = "https://www.aismagellan.io/api/things/pull/4e87f860-dc23-11e8-be06-154c92873ad1") 
    
    my_json = r.content.decode('utf8').replace("'", '"')
    r2 = json.loads(my_json)
    print(r2['dc_on'])
    #print(type(r.content))


    #Example Mysql
    # mydb = mysql.connector.connect(
    #     host="localhost",
    #     user="root",
    #     passwd="",
    #     database="weather"
    # )

    # mycursor = mydb.cursor()

    # sql = "INSERT INTO test (firstname,lastname) VALUES (%s,%s)"
    # val = ("John",”Somsom")
    # mycursor.execute(sql, val)

    # mydb.commit()

    # cursor.close()
    # mycursor.close()


printit()


app = Flask(__name__)

@app.route("/",methods=['GET'])
def hello():
    r = requests.get(url = "https://www.aismagellan.io/api/things/pull/4e87f860-dc23-11e8-be06-154c92873ad1") 
    return r.content

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

if __name__ == "__main__":
   app.run()

# if __name__ == "__main__":
#    app.run(host = '0.0.0.0',port=5000)