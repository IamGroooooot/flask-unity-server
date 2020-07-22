from flask import Flask, request, jsonify, render_template


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/post", methods=["POST"])
def post_test():
    res = list(request.form.values())
    print(res)

    return render_template("index.html", post_result=str(res))


@app.route("/get", methods=["GET"])
def get_test():
    print("결과: " + str(list(request.get_json(force=True).values())))
    try:
        data = request.get_json(force=True)
    except:
        print("json 파싱 실패")
        return jsonify(-1)
    else:
        print("파싱 성공")

    return render_template("index.html", post_result=str(data))
    # return jsonify(0)


if __name__ == "__main__":
    app = Flask(__name__)
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=9999)
