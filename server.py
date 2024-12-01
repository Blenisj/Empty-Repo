from flask import Flask, render_template, request, redirect, url_for
import ganttChart  # Import the modified ganttChart.py

app = Flask(__name__)

tasks = []

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/deliverables', methods=['GET', 'POST'])
def deliverables():
    if request.method == 'POST':
        task_name = request.form['task_name']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        tasks.append(dict(Task=task_name, Start=start_date, Finish=end_date))
        return redirect(url_for('deliverables'))
    
    gantt_html = ganttChart.create_gantt_chart(tasks)  # Generate the Gantt chart HTML
    return render_template('deliverables.html', gantt_html=gantt_html, tasks=tasks)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)