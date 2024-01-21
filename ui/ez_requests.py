from tkinter import *
from tkinter import ttk

import json

from app import requestor


class EzRequests:
    method: StringVar
    url: StringVar
    headers: StringVar
    body: StringVar

    def __init__(self, root: Tk):
        root.title("ezrequests")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.method = StringVar(value="GET")
        method_combobox: ttk.Combobox = ttk.Combobox(
            mainframe,
            textvariable=self.method,
            state=["readonly"],
            values=["GET", "POST", "PUT", "PATCH", "DELETE"],
        )
        method_combobox.grid(column=2, row=1)
        ttk.Label(mainframe, text="method").grid(column=1, row=1, sticky=(E, W))

        self.url = StringVar(value="http://localhost:8080")
        url_entry: ttk.Entry = ttk.Entry(mainframe, textvariable=self.url)
        url_entry.grid(column=2, row=2)
        ttk.Label(mainframe, text="url").grid(column=1, row=2, sticky=(E, W))

        self.headers = StringVar(value=json.dumps({"Accept": "application/json"}))
        headers_entry: ttk.Entry = ttk.Entry(mainframe, textvariable=self.headers)
        headers_entry.grid(column=2, row=3)
        ttk.Label(mainframe, text="headers").grid(column=1, row=3, sticky=(E, W))

        self.body = StringVar(value=json.dumps({}))
        body_entry: ttk.Entry = ttk.Entry(mainframe, textvariable=self.body)
        body_entry.grid(column=2, row=4)
        ttk.Label(mainframe, text="body").grid(column=1, row=4, sticky=(E, W))

        ttk.Button = ttk.Button(
            mainframe, text="Send Request", command=self.invoke_requestor
        ).grid(
            column=2,
            row=5,
        )

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        url_entry.focus()
        root.bind("<Return>", self.invoke_requestor)

    def invoke_requestor(self, *args):
        requestor.send_request(
            method=self.method.get(),
            url=self.url.get(),
            auth=None,
            headers=json.loads(self.headers.get()),
            body=json.loads(self.body.get()),
            params=None,
        )
