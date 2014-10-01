#! /usr/bin/env python2

from flask import Flask,render_template, redirect, url_for
import socket
import subprocess

UDP_IP = "192.168.23.190"
UDP_PORT = 2702
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

homecode = "00001"

# create our little application :)
app = Flask(__name__)

@app.route('/send/<channel>/<value>')
def send(channel,value):
    if(channel == "red"):
        channel = 2
    elif (channel == "green"):
        channel = 3
    elif (channel == "blue"):
        channel = 1

    MESSAGE = chr(0) + chr(channel) + chr(int(value))
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    return redirect(url_for('index'))

@app.route('/off')
def off():
    send("red",0)
    send("blue",0)
    send("green",0)
    return redirect(url_for('index'))

@app.route('/power/<channel>/<value>')
def switch_power(channel,value):
    args = ("sudo","/usr/bin/send",homecode,str(channel),str(value)) 
    popen = subprocess.Popen(args)
    popen.wait()
    return redirect(url_for('index'))

@app.route('/')
def index():
    #return render_template('index.html')
    return light() 

@app.route('/light')
def light():
    return render_template('light.html')

@app.route('/power')
def power():
    return render_template('power.html')

@app.route('/temp')
def temp():
    return render_template('temp.html')

if __name__ == '__main__':
        app.run(host="0.0.0.0",
                debug=True)
