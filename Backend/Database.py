#from flask import Flask, request, flash, url_for, redirect, render_template
#from flask_sqlalchemy import SQLAlchemy

#app = Flask (__name__)
#app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'

#db = SQLAlchemy(app)
#class students(db.Model):
   #id = db.Column('student_id', db.Integer, primary_key = True)
   #name = db.Column(db.String(100))
   #city = db.Column(db.String(50))  

#def __init__(self, name, city):
   #self.name = name
   #self.city = city

#db.create_all()




#c.execute('''
          #CREATE TABLE IF NOT EXISTS regions
          #([city_name] TEXT, [score] INTEGER PRIMARY KEY)
          #''')



#c.execute('''
          #CREATE TABLE IF NOT EXISTS totalTrees
          #([city] INTEGER PRIMARY KEY, [num_tree] INTEGER)
          #''')

#c.execute('''
         #INSERT INTO regions (city_name, score)
         
                #VALUES
                #('London',1000),
                #('Beijing',900),
                #('Edinburgh',850),
                #('Ohio',600),
                #('Oxford',590),
                #('Manchester',500),
                #('Singapore',480),
                #('Glasgow',450),
                #('Cardiff',400),
                #('Kent',360)
          #''')

#c.execute('''
         #INSERT INTO totalTrees (city_id,num_tree)
         
                #VALUES
                #(1,800),
                #(2,500),
                #(3,600),
                #(4,820),
                #(5,1000),
                #(6,50),
                #(7,760),
                #(8,640),
                #(9,300)
          #''')



#c.execute('''
         #SELECT
         #a.city_name,
         #b.num_tree
         #FROM regions a
         #LEFT JOIN totalTrees b ON a.city_id = b.city_id
         #''')

#conn.commit()
#df = pd.DataFrame(c.fetchall(), columns = ['regions','totalTrees'])
#print(df)




#Create a new Flask application and define a route for the leaderboard page:
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/leaderboard')
def leaderboard():
    import sqlite3
    #import pandas as pd
    conn = sqlite3.connect('database2_team5')
    c = conn.cursor()
    #Implement leaderboard data retrieval
    cur = c.execute('select * from regions')
    result = cur.fetchall()
    #cur1 = c.execute('select * from totalTrees')
    #result1 = cur1.fetchall()
    import json
    return json.dumps(result)
    
    #leaderboard_data = [{'name': 'John', 'score': 100}, {'name': 'Jane', 'score': 90}]
    #return render_template('leaderboard.html', leaderboard_data=leaderboard_data)

if __name__ == '__main__':
    app.run(debug=True)



#Run the Flask application and navigate to the leaderboard page:
#$ FLASK_APP=app.py flask run
#* Running on http://127.0.0.1:5000/




