from flask import Flask, render_template
import webbrowser
from threading import Timer

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

def open_browser():
    webbrowser.open_new("http://127.0.0.1:8080/")

def main():
    print("Hello from nielxs-dummy-flask-display-app!")


if __name__ == "__main__":

    # if os.environ.get("WERKZUG_RUN_MAIN") == "true":
    #     Timer(1, open_browser).start()
    Timer(1, open_browser).start()

    # app.run(debug=True)
    app.run("0.0.0.0", port=8080, debug=True)
    main()
