import socket
import subprocess
import shlex
import argparse

# Netcat class. Builds objects using args passed to argparse.
class NetCat:
    def __init__(self, cmd_args):
        # self.args = args passed to argparse, self.buffer is empty string, self.socket is socket object
        self.args = cmd_args
        self.buffer = ''
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # TODO: Define function to run our program in a specific way depending on listen argument or send argument
    def run(self):
        if self.args.listen:
            self.listen()
        else:
            self.send()

    # TODO: Define the listen and send functions to initiate the program in a specific way.
    # TODO: Listen will setup a server socket and wait for incoming connections
    def listen(self):
        self.socket.bind((self.args.address, self.args.port))
        self.socket.listen()
        print('[*] Listening')
        while True:
            try:
                conn, addr = self.socket.accept()
                print(f"Accepted connection from client: {addr}")
                self.handle(conn)
            except Exception as e:
                print(f'Error: {e}')

    # TODO: Build handle method to handle a client socket
    def handle(self, conn):
        self.buffer = conn.recv(1024)
        try:
            while self.buffer:
                print(self.buffer.decode())
                conn.close()
                break
        except Exception as e:
            print(f'Error: {e}')

    # TODO: Send will send messages to the socket server to control what it does
    def send(self):
        message = args.execute
        self.socket.connect((args.address, args.port))
        self.socket.send(message.encode())
        self.socket.close()

# TODO: Define an argument parser to pass args from command line and create a class instance
parser = argparse.ArgumentParser(description='Netcat like program')
parser.add_argument('-l', '--listen', action='store_true', help='Setup as a listener')
parser.add_argument('-e', '--execute', help='Command to execute on listener')
parser.add_argument('-a', '--address', help='IP address')
parser.add_argument('-p', '--port', type=int, help='Port number')
args = parser.parse_args()

netcat = NetCat(args)
netcat.run()
