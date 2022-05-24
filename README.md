### usage
- install requirements: ```pip install -r requirements.txt```

- if you want change some environment variables you should define .env config 

- run docker-compose rabbitmq service: ```docker-compose -f test-env.yml up --build -d```

- start app: ```python run_app.py```

- start consumer: ```python run_consumer.py```

- run example request: ```python code_examples.py```
