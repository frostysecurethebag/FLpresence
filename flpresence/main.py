from project_checker import rpc,close
from running import p_check, t_get
import time
from pypresence import presence


def gg():
    while(p_check()==True):
        rpc()

def end():
    close()
    
if __name__=="__main__":
    gg()
        
