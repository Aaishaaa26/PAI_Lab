logs = {}
num = int(input("Enter number of logs: "))

for i in range(num):
    log = input("Enter log: ")
    if log in logs:
        logs[log] = logs[log] + 1
    else:
        logs[log] = 1

print("logs", logs)
print("Log types:\n", logs.keys())

highest = 0
typeLog = 0
for log in logs:
    if logs[log] > highest:
        highest = logs[log]
        typeLog = log

print("Highest log:",  typeLog)