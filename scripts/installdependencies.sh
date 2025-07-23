#!/bin/bash

if ! command -v python >/dev/null 2>&1
then
    echo "Python could not be found. Please install Python to proceed."
    exit 1
fi

if ! command -v pip >/dev/null 2>&1
then
    echo "Pip could not be found. Please install Python and pip to proceed."
    exit 1
fi

pip install -r requirements.txt

if ! command -v node >/dev/null 2>&1
then
    echo "Node.js could not be found. Please install Node.js to proceed."
    exit 1
fi

if ! command -v npm >/dev/null 2>&1
then
    echo "NPM could not be found. Please install Node.js and NPM to proceed."
    exit 1
fi

npm install tailwindcss @tailwindcss/cli



