import datetime
readLog = open("_log.txt", "rt")
logFileLine = datetime.datetime.now().strftime("[%a %b  %d %X %Y] [notice] Logs checked by Python script")
errors = []
lineNum = 0
errorKeyword = "error".lower()
noticeKeyword = "notice".lower()
infoKeyword = "info".lower()
for line in readLog:
  lineNum += 1
  if line.lower().find(errorKeyword) != -1:
    foundErrorMSG = "ERROR FOUND! Line: " + str(lineNum)
    errors.append(foundErrorMSG + "\n" + line)
readLog.close()
logMessage = open("_log.txt", "at")
logMessage.write("\n\n\n" + logFileLine)
logMessage.close()
logErrors = open("found_errors.txt", "w")
for item in errors:
  logErrors.write("%s\n" % item)
logErrors.close()
