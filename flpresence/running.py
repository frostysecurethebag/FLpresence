import psutil
import pygetwindow as gw
import time

def p_check():
    ls = []
    for p in psutil.process_iter(attrs=['name']):
        if p.info['name'] == "fl.exe":
            return(True)
        elif p.info['name'] == "FL64.exe":
            return(True)
        elif p.info['name'] == "FL32.exe":
            return(True)

    print("Process is not running, checking again")
    time.sleep(5)
    p_check()
        
def t_get():
    x=(gw.getWindowsWithTitle('FL Studio')[0])
    titles=(x.title)
    titles=titles.split("-")
    return(titles[0])
