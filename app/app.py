from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Azure Enterprise DevOps Platform</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f1f5f9;
                text-align: center;
                padding: 80px 20px;
            }
            .card {
                background: white;
                max-width: 650px;
                margin: auto;
                padding: 40px;
                border-radius: 16px;
                box-shadow: 0 4px 20px #0001;
            }
            h1 { color: #1558a6; }
            .status {
                background: #dcfce7;
                color: #166534;
                padding: 15px;
                border-radius: 10px;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Azure Enterprise DevOps Platform</h1>
            <p>Cloud-native application running on Microsoft Azure</p>
            <div class="status">
                <h2>Application Healthy</h2>
                <p>Status: Running</p>
            </div>
            <p>Deployed with Docker, AKS and GitHub Actions</p>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", "5000"))
    )
