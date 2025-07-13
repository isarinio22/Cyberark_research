# main.py
# A simple Flask application to serve the static index.html file.

from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def serve_index():
    """
    Serves the index.html file from the current directory.
    """
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    # Cloud Run will set the PORT environment variable.
    # We default to 8080 for local testing.
    import os
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
