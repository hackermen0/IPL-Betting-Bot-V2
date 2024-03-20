import schedule
from Modules.dbFunctions import redeemBet
import time

schedule.every().day.at("19:00").do(redeemBet)

while True:
    schedule.run_pending()
    time.sleep(1)