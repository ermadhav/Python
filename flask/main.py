import flask    

app = Flask(__name__)

# Define a route for the root URL
@app.route("/")
def home():
return "Hello, Flask!"