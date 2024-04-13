from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host='kevinxia.mysql.pythonanywhere-services.com',
    user='kevinxia',
    password='SUSlabDBadmin',
    database='kevinxia$default'
)
cursor = db.cursor()

# Index route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/student')
def student():
    cursor = db.cursor()
    cursor.execute("INSERT INTO page_views (page_name, view_count) VALUES ('your-page', 1) ON DUPLICATE KEY UPDATE view_count = view_count + 1")
    db.commit()
    cursor.close()
    return render_template('student.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/student',methods = ['GET','POST'])
def supplier():
    return "supplier placeholder"

@app.route('/student/cnc')
def cnc():
    return "CNC placeholder"



if __name__ == '__main__':
    app.run(debug=True)