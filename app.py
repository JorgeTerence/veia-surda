from flask import Flask, render_template
from time import time

app = Flask(__name__)

times = {}
start_time = time()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/time/<name>", methods=["POST"])
def record(name: str):
    user_time = time() - start_time

    seconds = range(98, 125, 2)
    frequencies = [ 4600, 5400, 6000, 6400, 7200, 8000, 9000, 10000, 11200, 12700, 14000, 15600, 17500, 19500, 20000 ]

    if user_time < 98:
        times[name] = 4200

    if user_time > 124:
        times[name] = 20000

    for t, freq in zip(seconds, frequencies):
        if 0 < t - user_time < 1:
            times[name] = freq

    return str(times)


@app.route("/admin")
def admin():
    return render_template("admin.html")


@app.route("/startup")
def startup():
    global start_time

    times.clear()
    start_time = time()

    return str(start_time)


@app.route("/results/<name>")
def results(name: str = ""):
    average = sum(times.values()) / (len(times) or 1)
    return render_template("results.html", results=times, average=average, name=name)


if __name__ == "__main__":
    app.run()
