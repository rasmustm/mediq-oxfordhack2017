# mediQ @ OxfordHack 2017

## Brief Explanation

This is a simple web application designed to give doctors and physicians the ability to record interactions with patients and, based on the voice data collected, receive a brief report of possibly relevant studies. Hopefully this will assist doctors in keeping updated with research and assist them in finding diagnoses and interventions that might help their patients, all the while saving doctors precious time that they can spend better helping other patients and doing research.

## Getting up and running

The main web application, run with Python Flask, runs on Python 3. The dependencies can be found in requirements.python.txt

To get the system running:

```
$ pip install -r requirements.python.txt
$ cd python-flask && export FLASK_APP=app.py
$ flask run
```
