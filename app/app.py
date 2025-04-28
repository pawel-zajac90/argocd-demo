from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Witaj w ArgoCD Demo!</h1><p>Wersja 1.0</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
