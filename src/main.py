from ui.ui import UI
from services.logic import Logic
from services.room_service import RoomService


def main():
    room_service = RoomService()
    logic = Logic(room_service)
    app = UI(logic)

    app.start()


if __name__ == "__main__":
    main()
