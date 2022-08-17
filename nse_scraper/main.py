from localpackage import nse

from flask import Flask
app = Flask(__name__)

@app.route("/sync_nse", methods=['GET'])
def sync_nse():

    nse.sync_nse_data()
    return "Hello World!"

app.run()
