# PissedMan - A simpler Postman style API querying GUI

The main purpose of this project is to provide the very basic request/response functionality that the postman tool provides, for use in day-to-day development, as Postman cannot be installed on my work laptop without admin privs for some reason.

Initial scope is to build a basic UI for entering uri, auth info, json request body and displaying response details and body.

Functionality can then be expanded upon in the future but my personal requirements for this sort of tool are usually very basic.

## Requirements

- Python version >= 3.8
- requests
- PySide6

## Installation

For now, simply clone the repo and run the app, however, in future we will be making it installable via pip/pipx.

`git clone https://github.com/patrcoff/pissedman`

`cd pissedman`

`python -m pip install -r requirements.txt`

`python pissedman/widget.py`

## Updating UI elements

If running from a fresh clone of the repo then the ui_form.py should be up to date, but if you modify the Qt project in Qt designer, you must run the following command from the root of the repo in order to generate the updated ui_form.py file before running the app.

`pyside6-uic pissedman/form.ui -o pissedman/ui_form.py`