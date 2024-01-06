from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


def write_to_csv(a, b, c, d, e, f, g):
    z = f"{a}|{b}|{c}|{d}|{e}|{f}|{g}\n"
    # print(z)
    # print(type(z))
    with open("./templates/data.csv","a", encoding="utf-8") as csv_write:
        csv_write.write(f"{z}")


@app.route("/next", methods=["GET", "POST"])
def next():
    name = request.form["cafe_name"]
    location = request.form["location"]
    open = request.form["open"]
    close = request.form["close"]
    rating = request.form["coffee_rating"]
    wifi = request.form["wifi_rating"]
    power = request.form["socket_count"]
    # print(name, location, open, close, rating, wifi, power)
    write_to_csv(name, location, open, close, rating, wifi, power)
    return render_template("add.html")


@app.route("/add")
def add():
    return render_template("add.html")


@app.route("/cafe")
def cafe():
    c_new_list = []
    with open("./templates/data.csv", "r", encoding="utf8") as csv_read:
        c = csv_read.readlines()
        for i in c:
            i = i.replace("\n", "")
            c_new_list.append(i.split("|"))
        print(c_new_list)
    lens = len(c_new_list)
    # print(lens)
    return render_template('cafe.html', data=c_new_list, len=lens)


if __name__ == '__main__':
    app.run(debug=True)


