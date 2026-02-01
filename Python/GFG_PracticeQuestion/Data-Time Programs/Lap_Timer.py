import time

starttime =time.time()
lastime = starttime
lapnum = 1
print("Press Enter to count laps.\n Press CTRL + C to stop")

try:
    while True:
        input()

        laptime = round((time.time() - lastime),2)
        totaltime = round((time.time() - starttime),2)
        print("Lap No: "  + str(lapnum))
        print("Total Time: "  + str(totaltime))
        print("Lap Time: "  + str(laptime))


except KeyboardInterrupt:
    print("Done")