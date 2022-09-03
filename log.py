from PyQt5.QtWidgets import *
from datetime import datetime

def errLog(auth, errMsg, crit=False):
    #errNum = getErr(errNo)
    now = datetime.now()
    out = [now.strftime("%d/%m/%Y %H:%M:%S"),' ', auth, ' ', errMsg, ' ']
    if crit:
        out.append('CRITICAL')
    out.append('\n')
    errlogfile = open('eLog.txt', 'a')
    for item in out:
        errlogfile.write(item)
    errlogfile.close()
    if crit:
        exit()

def getErr(errNo):
    #TBC
    pass

def msgDisp(icon, title, text, infoText, detailedText=None, auth=None):
    """If icon is set to W or C, an author must be provided in the auth variable
       as these are automatically entered in the error log"""
    msgBox = QMessageBox()
    if icon == 'Q':
        msgBox.setIcon(QMessageBox.Question)
    elif icon == 'I':
        msgBox.setIcon(QMessageBox.Information)
    elif icon == 'W':
        msgBox.setIcon(QMessageBox.Warning)
        if auth == None:
            auth == '??'
        errLog(auth, infoText, False)
    elif icon == 'C':
        msgBox.setIcon(QMessageBox.Critical)
        if auth == None:
            auth == '??'
        errLog(auth, infoText, True)
    msgBox.setWindowTitle(title)
    msgBox.setText(text)
    msgBox.setInformativeText(infoText)
    if detailedText:
        msgBox.setDetailedText(detailedText)
