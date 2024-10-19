#!/bin/bash

cd ../Task3

uvicorn service:app --host 127.0.0.1 --port 8000 &

sleep 1

cd ../Task4

locust -f locustfile.py --headless -u 100 -r 10 -H http://localhost:8000 --html stat.html --run-time 30


