import time

print("What you want me to remind you?")
GetData = str(input())
GetTime = float(input("Enter time in minutes"))
GetTime = GetTime * 60
time.sleep(GetTime)
print(GetData)