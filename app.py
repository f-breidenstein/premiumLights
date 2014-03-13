#! /usr/bin/env python2

from flask import Flask,render_template, redirect, url_for
from time import sleep
import colorsys
import socket

UDP_IP = "192.168.23.190"
UDP_PORT = 2702
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# create our little application :)
app = Flask(__name__)

@app.route('/send/<channel>/<value>')
def send(channel,value):
    if(channel == "red"):
        channel = 2
    elif (channel == "green"):
        channel = 0
    elif (channel == "blue"):
        channel = 1

    MESSAGE = chr(0) + chr(channel) + chr(int(value))
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    return redirect(url_for('index'))


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
        app.run(host="0.0.0.0",
                debug=True)
