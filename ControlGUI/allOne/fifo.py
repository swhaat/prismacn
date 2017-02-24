import os

path = "/tmp/my_program.fifo"
os.mkfifo(path)

fifo = open(path, "w")
fifo.write("Message from the sender!\n")
fifo.close()



import os


path = "/tmp/my_program.fifo"
fifo = open(path, "r")
for line in fifo:
    print ("Received: " + line)
fifo.close()
