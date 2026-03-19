from flask import Flask
from flask_cors import CORS
from dataStore import DataStore
import json, os
import dotenv
dotenv.load_dotenv()

app = Flask(__name__)
origins = os.getenv("ORIGINS","")
print("ORIGINS:", os.getenv("ORIGINS"))
if not origins:
    raise ValueError("ORIGINS environment variable is not set")

CORS(app, origins=origins.split(","))
data_store = DataStore()

@app.route('/about')
def about():
    about_data = data_store.get("about")
    return json.dumps(about_data)


if __name__ == "__main__":
    app.run(debug=True)
