#!/bin/bash
# Run unit and system tests
pip3 install -r requirements.txt

echo "Running unit tests.."
python3 project/tests.py 

