from flask import Flask, render_template, Response
from flask_socketio import SocketIO
import time
import datetime
import threading
import random
from BlessRNG import RNG, RNGS
import system
import cv2

app = Flask('SecurityApp')
socketio = SocketIO(app)
clientthread = threading.Thread()
core = system.FullSystem()
numrngs = core.cameraNum

def imgtobytes(img):
    return cv2.imencode('.jpg',img)[1].tobytes()

@app.route('/')
def home():
    return render_template('test.html')

@app.route('/face/<camID>/<faceID>')
def face(camID, faceID):
    global core
    faceimg = core.cameras[int(camID)].faces[int(faceID)]
    return Response((b'--frame\r\n'
                     b'Content-Type: image/jpeg\r\n\r\n' + imgtobytes(faceimg) + b'\r\n\r\n'),
                    mimetype='multipart/x-mixed-replace; boundary=frame')      

def continuoussend():
    global core
    while True:
        datas = []
        # for i, gen in enumerate(rng.gens):
        #     number = gen.number
        #     data = {'id':i,'number':number}
        #     datas.append(data)
        datas = core.get_faces()
        socketio.emit('new numbers',datas,namespace='/time')
        print("Send time")
        time.sleep(4)

@socketio.on('connect',namespace='/time')
def connect():
    global clientthread
    print("A CLIENT CONNECTED")
    if not clientthread.is_alive():
        clientthread = threading.Thread(target=continuoussend)
        clientthread.daemon = True
        clientthread.start()
    data = {'numrng':numrngs}
    socketio.emit('info',data,namespace='/time')

@socketio.on('disconnect',namespace='/time')
def disconnect():
    print("A Client has disconnected..")

        

if __name__ == "__main__":
    socketio.run(app,port=6969)