import datetime
openLog = open("error_log.txt", "r")
logFileLine = datetime.datetime.now().strftime("[%a %b  %d %X %Y] [notice] Logs checked by Python script")
logs = openLog.read()
