from quart import Quart
from quart import render_template

app = Quart(__name__)

def run() -> None:
    app.run()

@app.get("/")
async def index():
    return await render_template("index.html")