# coding:utf-8
from apscheduler.schedulers.blocking import BlockingScheduler
from refresh import main, refresh

if __name__ == '__main__':
    sched = BlockingScheduler()
    sched.add_job(refresh, 'interval', minutes=5)
    sched.start()
