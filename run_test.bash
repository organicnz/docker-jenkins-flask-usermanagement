echo ‘Start installing dependencies’

#!/bin/bash
pip3 install -r /calc_app//requirements.txt

echo ‘Start running test cases’
pytest testcalculator.py