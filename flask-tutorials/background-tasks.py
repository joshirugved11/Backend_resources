from flask import Flask
from celery import Celery

app = Flask(__name__)

app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@celery.task
def background_task(name):
    return f"Hello, {name} from Celery!"

@app.route('/run_task/<name>')
def run_task(name):
    task = background_task.delay(name)
    return f"Task started! Task ID: {task.id}"

if __name__ == '__main__':
    app.run(debug=True)
