import time 
def countdowntimer():
    while seconds > 0:
        min=int(seconds/60)
        sec=int(seconds%60)
        timer=f"{min} : {sec}"
        print(timer,end="\r")
        time.sleep(1)
        seconds= seconds-1
    print("timeup")



seconds=input("Enter the time :")
countdowntimer(int(seconds))