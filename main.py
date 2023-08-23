from sanic import Sanic
from sanic.response import text, json
import redis
from rq import Queue, Worker
import jobs
import time

app = Sanic(__name__)


redis_conn = redis.Redis(password="trunghieu0910")
queue = Queue(name="task_queue", connection=redis_conn)
    
@app.route('/')
async def index(request):
    return text("Welcome to the Sanic App!")


@app.route('/search')
async def search(request):
    low = request.args.get("low")
    high = request.args.get("high")
    
    low = int(low)
    high = int(high)
    
    job1 = queue.enqueue(jobs.print_number, low, high)
    job2 = queue.enqueue(jobs.caculate_sum, 2, 3)
    while not job2.is_finished:
        print("Running")
        time.sleep(1)
    
    print(job2.result)
    
    if low and high:
        return json({
            "status": "success",
            "jobID": job1.id,
            "res": job1.return_value()
        })
    else:
        return text("error")
    
#rq worker --url redis://:trunghieu0910@localhost:6379/0 task_queue
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)