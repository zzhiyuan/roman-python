from flask import Flask, render_template, request

from roman import Roman

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index() -> str:
    roman: str = str(request.form.get("roman"))
    arabic: int = 0
    if len(roman) > 0:
        arabic = Roman.convert(roman)
    return render_template("index.html", roman=roman, arabic=arabic)


if __name__ == '__main__':
    app.run()
