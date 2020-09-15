from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)



@app.route('/')
def display_metrics_info():
    metrics = ['Number of trips', 'Duration of trips', 'Number of bicycles']
    return render_template("index.html",len = len(metrics), metrics = metrics)

@app.route('/metrics', methods=['GET'])
def display_metrics():
    return render_template("metrics.html")


if __name__ == '__main__':
    app.run(debug=True)
