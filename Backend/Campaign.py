#import pandas as pd
#import matplotlib.pyplot as plt

#name = ["Lily","Amy","Ben","Emily","Olivia"]
#num_users =[20,10,2,3,8]
#city = ["London","Tokyo","London","Nanjing","Ohio"]

#dict = {'name': name, 'city': city}

#df = pd.DataFrame(dict)

#X = list(df.iloc[:, 0])
#Y = list(df.iloc[:, 1])

#plt.bar(Y, X, color = 'g')
#plt.plot(city,num_users)
#plt.title("Region population")
#plt.xlabel("Region")
#plt.ylabel("Number of Users")

#plt.show()


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



import sqlite3
import pandas as pd
conn = sqlite3.connect('database_team5')
c = conn.cursor()
c.execute('''
          CREATE TABLE regions
          ([city_id] INTEGER PRIMARY KEY, [city_name] TEXT)
          ''')

c.execute('''
          CREATE TABLE totalTrees
          ([city_id] INTEGER PRIMARY KEY, [num_tree] INTEGER)
          ''')

c.execute('''
         INSERT INTO regions (city_id, city_name)
         
                VALUES
                (1,'London'),
                (2,'BeiJing'),
                (3,'HongKong'),
                (4,'Ohio'),
                (5,'Oxford'),
                (6,'London'),
                (7,'Singapore')
          ''')

c.execute('''
         INSERT INTO totalTrees (city_id,num_tree)
         
                VALUES
                (1,800),
                (2,500),
                (3,600),
                (4,820),
                (5,1000),
                (6,50),
                (7,760)
          ''')



c.execute('''
         SELECT
         a.city_name,
         b.num_tree
         FROM regions a
         LEFT JOIN totalTrees b ON a.city_id = b.city_id
         ''')

conn.commit()
df = pd.DataFrame(c.fetchall(), columns = ['regions','totalTrees'])
print(df)



#fen
#Create a new Flask application and define a route for the leaderboard page:
#from flask import Flask, jsonify, render_template

#app = Flask(__name__)

#@app.route('/leaderboard')
#def leaderboard():
    #Implement leaderboard data retrieval
    #leaderboard_data = [{'name': 'John', 'score': 100}, {'name': 'Jane', 'score': 90}]
    #return render_template('leaderboard.html', leaderboard_data=leaderboard_data)

#if __name__ == '__main__':
    #app.run(debug=True)

#function Leaderboard(props) {
    #const leaderboardData = props.leaderboardData;
    #return (
        #<div>
            #<h1>Leaderboard</h1>
            #<table>
                #<thead>
                    #<tr>
                        #<th>Name</th>
                        #<th>Score</th>
                    #</tr>
                #</thead>
                #<tbody>
                    #{leaderboardData.map((player, index) => (
                        #<tr key={index}>
                            #<td>{player.name}</td>
                            #<td>{player.score}</td>
                        #</tr>
                    #))}
                #</tbody>
            #</table>
        #</div>
    #);
#}

#export default Leaderboard;

#Create a new HTML file for the leaderboard page and include the React component
#<!DOCTYPE html>
#<html>
  #<head>
    #<meta charset="utf-8">
    #<title>Leaderboard</title>
  #</head>
  #<body>
    #<div id="root"></div>
    #<script src="{{ url_for('static', filename='build/bundle.js') }}"></script>
    #<script>
        #const leaderboardData = JSON.parse('{{ leaderboard_data | tojson | safe }}');
        #ReactDOM.render(
            #<Leaderboard leaderboardData={leaderboardData} />,
            #document.getElementById('root')
        #);
    #</script>
  #</body>
#</html>

#Create a new JavaScript file to compile the React code
#import React from 'react';
#import ReactDOM from 'react-dom';
#import Leaderboard from './Leaderboard';

#ReactDOM.render(
    #<Leaderboard />,
    #document.getElementById('root')
#);

#Run the Flask application and navigate to the leaderboard page:

#$ FLASK_APP=app.py flask run
#* Running on http://127.0.0.1:5000/




