from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/api/telemetry')
def telemetry():
    return jsonify({'altitude': 10, 'speed': 2})

if __name__ == '__main__':
    app.run(debug=True)
