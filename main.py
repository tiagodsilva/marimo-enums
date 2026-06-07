import marimo

__generated_with = "0.23.9"
app = marimo.App(width="medium")


@app.cell
def _():
    from enums import Fruits
    from utils import is_orange, is_apple

    return Fruits, is_orange


@app.cell
def _(Fruits, is_orange):
    is_orange(Fruits.ORANGE)
    return


if __name__ == "__main__":
    app.run()
