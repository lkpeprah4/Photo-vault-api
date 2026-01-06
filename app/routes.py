@app.route("/health")
def health():
    return {"status": "ok"}
