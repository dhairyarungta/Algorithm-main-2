import socket
from main import main
import argparse



def receive(args):
    while True:
        text = s.recv(1024)
        print(text.decode())
        send(map=text.decode(), args=args)

def send(map, args):
    #map = 'ROB:25,25;OBS1:55,75,270;OBS2:125,95,0;OBS3:155,45,90;OBS4:155,155,270;OBS5:55,135,180'
    text = main(map, args)#'ROB:15,15;OBS1:215,35,90;OBS2:135,135,90;OBS3:15,95,270;OBS4:55,145,180')#map)#"ROB:15,15;OBS1:45,125,0;OBS2:135,155,270;OBS3:105,105,180;OBS4:145,45,90")
    #text = main('ROB:15,15;OBS1:175,15,180;OBS2:85,55,0;OBS3:105,195,270;OBS4:165,165,270;OBS5:35,135,90')
    s.send(text.encode())

def parse_args():
    """ Parse command line arguments.
    """
    parser = argparse.ArgumentParser(description="MDP Algorithm Client")
    parser.add_argument(
        "--port", help="Port",
        default=5000, required=True)

    parser.add_argument(
        "--use-inplace", help="Use Inplace Place", action="store_true",
        default=False
    )

    parser.add_argument(
        "--padding", help="Turning Padding",
        default=8, type=int
    )

    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    HOST = '192.168.27.27'  # The server's hostname or IP address
    PORT = args.port        # The port used by the server
    if type(PORT) == str:
        PORT = int(PORT)
    s = socket.socket()
    s.connect((HOST, PORT))
    receive(args)
    # print(args.use_inplace)
    # print(type(args.use_inplace))
    # print(main('ROB:25,25;OBS1:55,75,270;OBS2:125,95,0;OBS3:155,45,90;OBS4:155,155,270;OBS5:55,135,180', args))



        