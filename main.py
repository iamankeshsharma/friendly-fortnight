from flask import Flask
from dataStore import DataStore
import json

app = Flask(__name__)
data_store = DataStore()

@app.route('/about')
def about():
    about_data = data_store.get("about")
    return json.dumps(about_data)


if __name__ == "__main__":
    app.run(debug=True)
