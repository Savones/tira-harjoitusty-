from ui.ui import UI
from services.logic import Logic


def main():
    logic = Logic()
    app = UI(logic)

    app.start()


if __name__ == "__main__":
    main()
