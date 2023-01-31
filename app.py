from flask import Flask

app = Flask(__name__)
app.json.ensure_ascii = False


@app.route('/')
def start_page():
    """
    Вьюшка для стартовой страницы
    """
    return 'Start_page'


if __name__ == "__main__":
    app.run()
