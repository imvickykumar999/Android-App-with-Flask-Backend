from flask import Flask

# Flask Constructor
app = Flask(__name__)

# decorator to associate
# a function with the url
@app.route("/")
def showHomePage():
	# response from the server
	return "This is home page"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
