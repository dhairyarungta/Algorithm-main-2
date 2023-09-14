import socket 
from main import main
import argparse

def receive(args):
    while True:
        text = s.recv(1024)
        print(text.decdode())
        send(map = text.decode(),args = args)

def send (map, args):
    