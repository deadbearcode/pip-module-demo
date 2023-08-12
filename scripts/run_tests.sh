#!/usr/bin/env bash

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"

source .venv/bin/activate
cd $SCRIPTPATH
cd ..
export PYTHONPATH="./deadbear_fib_py"
python -m unittest discover