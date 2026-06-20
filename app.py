from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route("/")
def current_time():
    tz = pytz.timezone("America/Los_Angeles")
    now = datetime.now(tz)
    return f"<h2>Current Local Time:</h2><p>{now.strftime('%Y-%m-%d %H:%M:%S %Z')}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
