
from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import psycopg2.extras

# create application route
app = Flask(__name__)

# create database connection
conn = psycopg2.connect(
    host="localhost",
    database="olympicdata2",
    user="postgres",
    password="admin")
cur = conn.cursor()

@app.route('/')
def homepage():
   return render_template('homepage.html')

# create a route

@app.route('/insertcountry')
def forms():
    return render_template('insertcountry.html')

# add post method
@app.route('/insertcountry', methods=['POST'])
def showcountry_post():
    countryname =  request.form['countryname']
    year =  request.form['year']
    print(countryname, year)
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("INSERT INTO country (countryname, year) VALUES (%s, %s)", (countryname, year))
    conn.commit()
    
    return(redirect(url_for('display')))

# display data from database
@app.route('/showcountry')
def display():
    cur = conn.cursor()
    cur.execute("SELECT * FROM country")
    rows = cur.fetchall()
    return (render_template('showcountry.html', rows=rows))


# add post method

   

@app.route('/deletecountry', methods=['POST','GET'])

def deletecountry_post():
    if request.method == 'GET':
        return(render_template('deletecountry.html'))
    else:
        countryname =  request.form['countryname']
        year =  request.form['year']
        print(countryname, year)
        cur = conn.cursor()
        cur.execute("delete from  country  where countryname = %s and year = %s ", (countryname,year))
    # database specific query
    conn.commit()
    return redirect(url_for('display'))





@app.route('/insertgame')
def forms_fun():
    return render_template('insertgame.html')

# add post method
@app.route('/insertgame', methods=['POST'])
def showgame_post():
    gamename =  request.form['gamename']
    yearadded =  request.form['yearadded']
    yearremoved =  request.form['yearremoved']
    year =  request.form['year']
    print(gamename, yearadded,yearremoved,year)
    cur = conn.cursor()
    cur.execute("INSERT INTO game (gamename, yearadded,yearremoved,year) VALUES (%s, %s , %s, %s)", (gamename, yearadded,yearremoved,year))
    # database specific query
    conn.commit()
    return redirect(url_for('displaygame'))

# display data from database
@app.route('/showgame')
def displaygame():
    cur = conn.cursor()
    cur.execute("SELECT * FROM game")
    rows = cur.fetchall()
    return (render_template('showgame.html', rows=rows))

# add post method
@app.route('/editgame', methods=['POST','GET'])

def editgame_post():
    if request.method == 'GET':
        return(render_template('editgame.html'))
    else:
        gamename =  request.form['gamename']
        yearadded =  request.form['yearadded']
        yearremoved =  request.form['yearremoved']
        year =  request.form['year']
        print(gamename, yearadded,yearremoved,year)
        cur = conn.cursor()
        cur.execute("update game set yearadded = %s ,yearremoved = %s where gamename = %s and year = %s ", (yearadded,yearremoved,gamename,year))
        # database specific query
        conn.commit()
        return redirect(url_for('displaygame'))

@app.route('/deletegame', methods=['POST','GET'])
def deletegame_post():
    if request.method == 'GET':
        return(render_template('deletegame.html'))
    else:
            gamename =  request.form['gamename']
            yearadded =  request.form['yearadded']
            yearremoved =  request.form['yearremoved']
            year =  request.form['year']
            print(gamename, yearadded,yearremoved,year)
            cur = conn.cursor()
            cur.execute("delete from  game  where gamename = %s and yearadded =%s and yearremoved =%s and year=%s", (gamename,yearadded,yearremoved,year))
    # database specific query
            conn.commit()
            return redirect(url_for('displaygame'))


@app.route('/runquerygame')
def runquerygame_post():
     
            
            cur = conn.cursor()
            cur.execute("select gamename ,yearadded ,yearremoved ,year  from game where year = 1991 ")
    # database specific query
            rows = cur.fetchall()
            return (render_template('runquerygame.html', rows=rows))

@app.route('/runquerycountry')       
def runquerycountry_post():
    
    cur = conn.cursor()
    cur.execute("SELECT countryname , year  from country order by year")
    # database specific query
    rows = cur.fetchall()
    return (render_template('runquerycountry.html', rows=rows))

# run the application
if __name__ == '__main__':
    app.run(debug=True)