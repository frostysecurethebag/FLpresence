from running import t_get
import pygetwindow as gw
from pypresence import Presence
import time



client_id = '833657447369146389'
RPC = Presence(client_id,pipe=0)
RPC.connect()

tm=time.time()

def close():
    RPC.close()

def rpc():
    RPC.update(state="Cooking Beats",details=f"Working on {t_get()}",start=tm,large_image="rcp",small_image="rcp_2")
    while True:
        time.sleep(10)
        rpc()









