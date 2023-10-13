from flask import Flask
app= Flask(__Name__)

@app.route('/')
def hello_world():
    return 'Greymatters'


if__name__ == "__main__":
    app.run()
