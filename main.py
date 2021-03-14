from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/home')
@app.route('/')
def home():
        return render_template("home.html")

if __name__ == "__main__":
        print("hello mentimeter!")
        app.run(host='0.0.0.0', port=9003, debug=True)