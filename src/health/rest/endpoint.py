from src import app


@app.route("/health")
def health():
    return "healthy!"
