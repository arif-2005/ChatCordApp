import asyncio
import json
import websockets
import time
import formatTime as now

host = "localhost"
port = 6789

print("Survice Starts At: " +  now.time("ymdhms")  )
print("Survice Started at "+host+":"+str(port))

# variables to get/send from/to the client :
	#username, room_id, message, time
USERS = set()

#notify other users for the joining of a new user
async def notify_users(message):
    if USERS:  # asyncio.wait doesn't accept an empty list
        await asyncio.wait([user.send(message) for user in USERS])

# Register
async def register(websocket):
    USERS.add(websocket)
    message = json.dumps({"username": "ChatCord", "message":  "new user join " + str(len(USERS)) , "time": now.time("hm"),"msgType":"text", "available_user" : str(len(USERS))  })
    print("A new user connected")
    print("Current Users Number: " + str(len(USERS)))
    print(USERS)
    await notify_users(message)
# Unregister
async def unregister(websocket):
    USERS.remove(websocket)
    message = json.dumps({"username": "ChatCord", "message":  "A user gets out " + str(len(USERS)) , "time": now.time("hm"),"msgType":"text", "available_user" : str(len(USERS))  })
    print("A user gets out")
    print("Current Users Number: " + str(len(USERS)))
    await notify_users(message)




# Control Room
async def counter(websocket, path):
    webid = str(websocket)
    await websocket.send(json.dumps({"username": "ChatCord", "message":  "Welcome To SPI ChatCord" , "time": now.time("hm"),"webid":webid,"msgType":"text", "available_user" : str(len(USERS))  }))
    #await print(json.load(websocket))
    await register(websocket)
    try:
        async for message in websocket:
            data = json.loads(message)
            print(data)
            recvUser = data['username']
            recvMSG = data['message']
            recvtype = data['msgType']
            if (recvMSG == "™™~π™™"):
            	recvMSG = "A User Join '" + recvUser + " ' "
            	recvUser = "ChatCord"
            MSG = json.dumps({"username": recvUser, "message": recvMSG, "time": now.time("hm"), "msgType":recvtype , "available_user" : str(len(USERS))  })
            await asyncio.wait([user.send(MSG) for user in USERS])
    finally:
        await unregister(websocket)

#start server
start_server = websockets.serve(counter, host, port)
#make a loop to rerun the server again 
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
