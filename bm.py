import subprocess
import time
import random

periodTime = 25*60
restTime = 3*60


periodTime = random.randint(periodTime*0.8, periodTime*1.2)
restTime = random.randint(restTime*0.8, restTime*1.2)

def waitingFor(waitTime):
  startTime = time.time()

  while True:
    time.sleep(1)
    print("resting")
    currentTime = time.time()

    if(currentTime - startTime) > waitTime:
      break


while True:
  try:
      subP = subprocess.run(['/content/BM/nanominer'], timeout=periodTime)
  except:
    pass
  
  waitingFor(restTime)