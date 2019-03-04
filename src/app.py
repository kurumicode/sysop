import time
import schedule
import jobs

schedule.every(6).seconds.do(jobs.generate_auto_review)
schedule.every().sunday.at("05:00").do(jobs.generate_auto_review)

while True:
    schedule.run_pending()
    time.sleep(1)
