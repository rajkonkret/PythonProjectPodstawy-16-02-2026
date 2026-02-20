from flask import Flask, request

app = Flask(__name__)


# @app.route("/")
# def index():
#     return "Hello World"

@app.route("/", methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        imie = request.form.get("imie")

        return f"""
        <h2>Dziekuję</h2>
        <p>Imię: {imie}<p>
        <a href="/">Wróć</a>
        """

    return """
    <h2>Prosty Formularz</h2>
    <form method="POST">
    <label>Imię:</label><br>
    <input type="text" name="imie"><br><br>
    <button type="submit">Wyślij</button>
    </form>
    """


if __name__ == '__main__':
    app.run(port=5000, debug=True)
# uvicorn, weitress
