speed_mph = float(input("Enter car speed in MPH: "))

if speed_mph < 20:
    print("SAFE - You are driving slowly")
elif speed_mph <= 50:
    print("CAUTION - You are driving at a moderate speed")
else:
    print("EMERGENCY - You are driving too fast")

if speed_mph -- 0:
    print("Your car is stationary")
if speed_mph < 30:
    print("You are driving at a safe speed")
if speed_mph <= 60:
    print("You are driving at a high speed")
if speed_mph < 60:
    print("You are driving at a dangerous speed")

speeds = [0, 15, 35, 55, 70]#this is a list

for speed in speeds:
    print("Testing speed:", speed)

    if speed == 0:
        print("Car is stopped")
    elif speed < 30:
        print("SAFE")
    elif speed <= 60:
        print("CAUTION")
    else:
        print("EMERGENCY")

    print("-----------------")



speeds = [0, 15, 35, 55, 70]
results = []

for speed in speeds:
    if speed == 0:
        status = "Car is stopped"
    elif speed < 30:
        status = "SAFE"
    elif speed <= 60:
        status = "CAUTION"
    else:
        status = "EMERGENCY"
    
    results.append(status)  # Add the result to the list
print(results)
['Car is stopped', 'SAFE', 'CAUTION', 'CAUTION', 'EMERGENCY']





summary = []

for speed in speeds:
    if speed == 0:
        status = "Car is stopped"
    elif speed < 30:
        status = "SAFE"
    elif speed <= 60:
        status = "CAUTION"
    else:
        status = "EMERGENCY"
    
    summary.append((speed, status))  # store as a pair (tuple)
    
print(summary)
