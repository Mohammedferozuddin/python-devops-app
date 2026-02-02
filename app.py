from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚀 DevOps App is Running!</h1>
    <p>Deployed using Azure DevOps Pipeline + Docker + AWS EC2</p>
    """

@app.route("/health")
def health():
    return {"status": "OK"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
