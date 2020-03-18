from flask import Flask, render_template


app = Flask(__name__, static_url_path="/assets")


@app.route("/core", methods=["GET"])
def core():
    return render_template("core.html")


@app.route("/index", methods=["GET", "POST"])
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
