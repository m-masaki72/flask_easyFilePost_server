from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['POST'])
def upload():
    print(request.headers)
    upfile = request.files['data']
    upfile.save("test.log")

    return request.data

if __name__ == "__main__":
    app.run(debug=False, host="127.0.0.1", port=8080)
