from flask import Flask, render_template, request
from time import time

app = Flask(__name__)

times = {}
start_time = time()


@app.route("/")  # Send time ✅
def index():
    return render_template("index.html")


@app.route("/time", methods=["POST"])  # Receive time ✅
def record():
    data = request.get_json()

    name = data["name"]
    user_time = time() - start_time

    seconds = range(98, 128, 2)
    frequencies = [4600, 5400, ] # TODO!!!!!

    if user_time < 98:
        times[name] = 4200

    for t, freq in zip(seconds, frequencies):
        if 0 < t - user_time < 1:
            times[name] = freq

        print(name, "->", user_time)
    print(times)

    return str(times)


@app.route("/admin")  # Start session page ✅
def admin():
    return render_template("admin.html")


@app.route("/startup")  # Start session ✅
def startup():
    global start_time

    times.clear()
    start_time = time()
    print(start_time)

    return str(start_time)


@app.route("/results/<name>")  # Display results
@app.route("/results")  # Display results
def results(name: str = ""):
    average = sum(times.values()) / (len(times) or 1)
    return render_template("results.html", results=times, average=average, name=name)

if __name__ == "__main__":
    app.run()
