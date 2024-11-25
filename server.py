from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/team')
def team():
    return render_template('team.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=4000)