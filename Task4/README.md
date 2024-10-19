
Запуск теста на 30 секунд

```

locust -f locustfile.py --headless -u 100 -r 10 -H http://localhost:8000 --html stat.html --run-time 30

```

![Начало загрузки CPU](images/start_cpu.png)
![Конец загрузки CPU](images/end_cpu.png)