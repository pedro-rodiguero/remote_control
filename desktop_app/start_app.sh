#!/bin/bash

# Start the Flask server in the background
python3 server.py &

# Start the PyQt application
python3 app.py