
# Example of using Python and Flask as a web site
# Example uses port 8080 so need to browse to site as http://localhost:8080

from flask import Flask, send_from_directory
app = Flask(__name__)


# setup a route for when browsing to just the domain name (http://localhost:8080)
@app.route('/')
def hello_world():
    # return whatever string you want.
    return """
        <html>
            <head>
                <title>hello world</title>
            </head>
            <bod>
                <div style="text-align:center">Hello, World!</div>
                <div>
                    <a href="/static/static.html">Link to Static Html</a>
                </div>
                <div>
                    <img src="/static/WP_20160710_001.jpg"/>
                </div>
            </body>
        </html>
        """


# can also return a static page from disk. 
# do this for any url that starts with /pages
@app.route("/static/<path:path>")
def static_page(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(port=8080)