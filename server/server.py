# Source - https://stackoverflow.com/a
# Posted by Florian Metzger-Noel
# Retrieved 2025-11-15, License - CC BY-SA 4.0

import eventlet
import socketio

sio = socketio.Server(cors_allowed_origins="*", async_mode='eventlet', pingInterval=1000, pingTimeout=1000)
app = socketio.WSGIApp(sio)    

data_publish = {
                    'bms': {'voltage': 12.3, 'current': 1.2, 'soc': 85},
                    'gpio_input': {'brake': True, 'estop': False, 'overcurrent': False, 'flow': 123}
                }

def ping_in_intervals():
    while True:
        sio.sleep(1)
        sio.emit('ping')   
        print('Ping sent to client')

def publish_message():
    while True:
        sio.sleep(0.5)
        sio.emit('publish', data_publish)   
        # print('Published message to client')     

@sio.on('connect')
def connect(sid, environ):
    print('Client connected:', sid)

@sio.on('disconnect')
def disconnect(sid):
    print('Client disconnected:', sid)

# @sio.on('ping')
# def ping(*args):
#     print('Ping received from client')
#     sio.emit('pong')

# thread1 = sio.start_background_task(ping_in_intervals)
thread2 = sio.start_background_task(publish_message)
eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
