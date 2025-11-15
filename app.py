from flask import Flask, render_template, request
import mysql.connector
import os

app = Flask(__name__)

db_config = {
    'host': os.getenv("DB_HOST", "db"),
    'user': os.getenv("DB_USER", "root"),
    'password': os.getenv("DB_PASSWORD", "rootpassword"),
    'database': os.getenv("DB_NAME", "tariktambangdb")
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    team_a = int(request.form['team_a'])
    team_b = int(request.form['team_b'])
    winner = "Tim A" if team_a > team_b else "Tim B" if team_b > team_a else "Seri"

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO results (team_a, team_b, winner) VALUES (%s, %s, %s)",
                   (team_a, team_b, winner))
    conn.commit()
    cursor.close()
    conn.close()

    return render_template('result.html', team_a=team_a, team_b=team_b, winner=winner)

@app.route('/history')
def history():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM results ORDER BY id DESC")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return {"history": rows}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
