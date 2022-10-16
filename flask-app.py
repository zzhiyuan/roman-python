from flask import Flask, render_template, request

from app.roman import Roman

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index() -> str:
    roman: str = str(request.args.get("roman"))
    arabic: int = -1
    if roman != "None":
        arabic = Roman.convert(roman)

    return render_template("index.html", roman=roman, arabic=arabic)


if __name__ == '__main__':
    app.run()
