from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1>TESTE DE PIPELINE!!!</h1>\nMBA! o/"

if __name__ == '__main__':
    application.run()
