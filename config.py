import os

import dotenv

dotenv.load_dotenv()

host = os.getenv('APP_HOST', '0.0.0.0')
port = os.getenv('APP_PORT', 8001)
rabbitmq_host = os.getenv('RABBITMQ_HOST', '127.0.0.1')
rabbitmq_port = os.getenv('RABBITMQ_PORT', 5672)
rabbitmq_default_virtualhost = os.getenv('RABBITMQ_DEFAULT_VIRTUALHOST', 'test')
rabbitmq_managment_port = os.getenv('RABBITMQ_MANAGEMENT_PORT', 45672)
queue_name = os.getenv('QUEUE_NAME', 'events')
rabbitmq_login = os.getenv('RABBITMQ_LOGIN')
rabbitmq_password = os.getenv('RABBITMQ_PASSWORD')

rabbitmq_config = {
    'host': rabbitmq_host,
    'port': rabbitmq_port,
    'virtualhost': rabbitmq_default_virtualhost,
    'login': rabbitmq_login,
    'password': rabbitmq_password,
    'management_port': rabbitmq_managment_port
}
