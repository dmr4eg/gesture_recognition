import signal
import sys
from gestures.controller import GestureController

class App:
    def __init__(self) -> None:
        self.app = GestureController()
        signal.signal(signal.SIGINT, self.signal_handler)

    def signal_handler(self, _: signal.Signals, __: object) -> None:
        print('SIGINT received, shutting down...')
        self.app.destroy()
        sys.exit(0)

    def run(self) -> None:
        try:
            self.app.start_recognition()
            self.app.mainloop()
        except KeyboardInterrupt:
            self.app.destroy()