from flask import Flask, render_template, jsonify, redirect, url_for, request, flash
from mysql.connector import pooling

app = Flask(__name__)

dbconfig = {
    'host':'kevinxia.mysql.pythonanywhere-services.com',
    'user':'kevinxia',
    'password':'SUSlabDBadmin',
    'database':'kevinxia$default'
}
pool = pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=6,
    pool_reset_session=True,
    **dbconfig
)

# Index route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/student')
def student():
    conn = pool.get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO page_views (page_name, view_count) VALUES ('student', 1) ON DUPLICATE KEY UPDATE view_count = view_count + 1")
    conn.commit()
    cursor.close()
    conn.close()
    return render_template('student.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/task1')
def task1():
    return render_template('task1.html')

@app.route('/task2')
def task2():
    return render_template('task2.html')

@app.route('/task3')
def task3():
    return render_template('task3.html')

@app.route('/get-access-counts')
def get_access_counts():
    conn = None
    cursor = None
    try:
        conn = pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT page_name, view_count FROM page_views;")
        results = cursor.fetchall()
        return jsonify(results)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


@app.route('/submit-materials', methods=['POST'])
def submit_materials():
    selected_materials = request.form.getlist('materials')
    if selected_materials != None:
        conn = pool.get_connection()
        cursor = conn.cursor()
        for material in selected_materials:
            cursor.execute(
                f"INSERT INTO material_list (material_name, used_num) VALUES ({material}, 1) ON DUPLICATE KEY UPDATE used_num = used_num + 1",
            )
            conn.commit()
            
        
        cursor.close()
        conn.close()
    flash('Materials submitted successfully!')
    return redirect(url_for('student'))  # Redirect to the next page or confirmation page



@app.route('/increment-task1-view', methods=['POST'])
def increment_task1_view():
    # Database update logic to increment the view count
    conn = pool.get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO page_views (page_name, view_count) VALUES ('task1', 1) ON DUPLICATE KEY UPDATE view_count = view_count + 1")
    conn.commit()
    cursor.execute("INSERT INTO page_views (page_name, view_count) VALUES ('CNC', 1) ON DUPLICATE KEY UPDATE view_count = view_count + 1")
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('task2'))  # Assuming 'task2' is the endpoint for the next task page

@app.route('/increment-task2-view', methods=['POST'])
def increment_task2_view():
    # Database update logic to increment the view count
    conn = pool.get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO page_views (page_name, view_count) VALUES ('task2', 1) ON DUPLICATE KEY UPDATE view_count = view_count + 1")
    conn.commit()
    cursor.execute("INSERT INTO page_views (page_name, view_count) VALUES ('3Dprint', 1) ON DUPLICATE KEY UPDATE view_count = view_count + 1")
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('task3'))  # Assuming 'task2' is the endpoint for the next task page

@app.route('/increment-task3-view', methods=['POST'])
def increment_task3_view():
    # Database update logic to increment the view count
    conn = pool.get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO page_views (page_name, view_count) VALUES ('task3', 1) ON DUPLICATE KEY UPDATE view_count = view_count + 1")
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('student'))  # Assuming 'task2' is the endpoint for the next task page

if __name__ == '__main__':
    app.run(debug=True)