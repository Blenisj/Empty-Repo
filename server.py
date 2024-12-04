from flask import Flask, render_template, request, redirect, url_for
import ganttChart  # Import the modified ganttChart.py
import calender  # Import the modified calender.py

app = Flask(__name__)

tasks = []
events = []

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/deliverables', methods=['GET', 'POST'])
def deliverables():
    global tasks, events  # Ensure tasks and events are recognized as global variables

    if request.method == 'POST':
        if 'add_task' in request.form:
            task_name = request.form['task_name']
            start_date = request.form['start_date']
            end_date = request.form['end_date']
            tasks.append(dict(Task=task_name, Start=start_date, Finish=end_date))
        elif 'remove_task' in request.form:
            task_name = request.form['task_name']
            tasks = [task for task in tasks if task['Task'] != task_name]
        elif 'add_event' in request.form:
            event_name = request.form['event_name']
            event_date = request.form['event_date']
            events.append(dict(name=event_name, date=event_date))
        return redirect(url_for('deliverables'))
    
    gantt_html = ganttChart.create_gantt_chart(tasks)  # Generate the Gantt chart HTML
    calendar_html = calender.generate_calendar_html(events)  # Generate the calendar HTML
    return render_template('deliverables.html', gantt_html=gantt_html, calendar_html=calendar_html, tasks=tasks, events=events)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)