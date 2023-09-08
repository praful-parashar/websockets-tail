import time
import os
def follow(thefile):
    '''generator function that yields new lines in a file
    '''
    # seek the end of the file
    thefile.seek(0, os.SEEK_END)
    
    # start infinite loop
    while True:
        # read last line of file
        line = thefile.readline()
        # sleep if file hasn't been updated
        if not line:
            # print("in not line")
            time.sleep(0.1)
            continue
        # print("out of loop, near yield")
        yield line

# if __name__ == '__main__':

def main():

    logfile = open("/Users/praful/websockets/access.log","r")
    loglines = follow(logfile)
    # iterate over the generator
    print("aise hi kuch bhi")
    for line in loglines:
        # print(line)
        # str s = line
        yield line


import asyncio
import websockets
# from  import tail
connected = set()
# import ipdb; 
async def server(websocket, path):
    # Register.
    connected.add(websocket)
    ws = websocket
    # ipdb.set_trace()
    print("at first", connected)
    try:
        async for message in websocket:
            # for conn in connected:
                # if conn != websocket:
                    # main()
            print("print in ")
            
            await ws.send(f'Got a new MSG FOR YOU: {message}')
            # import ipdb; ipdb.set_trace()
            logfile = open("/Users/praful/websockets/access.log","r")
            loglines = follow(logfile)
            # iterate over the generator
            print("aise hi kuch bhi") # -- function control
            for line in loglines:
                print(line)
                # str s = line
                # yield line
                print("we are here")
                await ws.send("log file is here for you , bitches - {logs}".format(logs=line))
            print("we are not here")
                    # implement 
        
    finally:
        print("now at finally", connected)
        # Unregister.
        connected.remove(websocket)
    

start_server = websockets.serve(server, "localhost", 5000)

asyncio.get_event_loop().run_until_complete(start_server) # --> thread 1 - start_server
asyncio.get_event_loop().run_forever() # --> thread 1




    