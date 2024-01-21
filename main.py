from tkinter import Tk
from ui.ez_requests import EzRequests
import sys
import threading

from local import mockserver

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "dev":
        s: threading.Thread = threading.Thread(target=mockserver.run, daemon=True)
        s.start()

    root: Tk = Tk()
    EzRequests(root)
    root.mainloop()
