from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/post", methods=["POST"])
def post():
    msg = request.form["msg"]
    print("===Post Request===")
    print(msg)
    print()

    return render_template("index.html", post_result=str(msg))


@app.route("/get", methods=["GET"])
def get():
    msg = request.args.get("msg")
    print("===Get Request===")
    print(msg)
    print()
    return render_template("index.html", get_result=str(msg))


if __name__ == "__main__":
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=9999)
