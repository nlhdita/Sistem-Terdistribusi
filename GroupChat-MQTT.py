import paho.mqtt.client as mqtt
import time
from datetime import datetime
import os
# broker_address = "192.168.0.44"
broker_address = "localhost"
port = 3577

user = input("Input username: ")
client = mqtt.Client(user)
group = int(input("Make a group! How many person? (int) >>"))
pubtop = user
kunyit=[]
def on_message(client, userdata, message):
    msg = str(message.topic)
    time_now = datetime.now()
    time_string = time_now.strftime("%H:%M")
    if (msg != pubtop and msg != "photo"):
        string = str(message.payload.decode("utf-8"))
        print(f"{message.topic} > ", string , "(",time_string, ")")
        pubchat = f"{message.topic} > " + string
        vaar = str(message.topic)
        if ((vaar == "aldi" and string == "pendek")):
            test = "bisa"
            kunyit.append(test)
        if ((vaar == "ecky" and string == "pendek")):
            test = "bisa"
            kunyit.append(test)
    if (msg != pubtop and msg == "photo"):
        print("Messsage received")
        string = message.payload
        print("check")
        file = open("download.jpg", "wb")
        file.write(string)
        print(time_string)
        file.close()
        pubchat = f"{vaar} > Sent a photo"
    hist = open("history_chat.txt", "a")
    var = pubchat + " " + "(" + time_string + ")"
    hist.write(var + "\n")
    hist.close()
client.on_message = on_message

def on_publish(client, userdata, result):
    pass
client.on_publish = on_publish

print("connecting to broker")
client.connect(broker_address, port)


client.loop_start()
for i in range(group -1):
    subtop = input("Member group: ")
    client.subscribe(subtop)
client.subscribe("photo")
print("subscribing")
os.system('clear')

print(f"--- {pubtop} --- ")
while True:
    time.sleep(1)
    chat = input()
    if (chat == "photo" or chat == "Photo" or chat == "PHOTO"):
        print("uploading photo")
        print("Choose photo")
        print("============")
        print("1. Photo 1")
        print("2. Photo 2")
        print("3. Photo 3")
        choose = str(input("Input number (1/2/3): "))
        if (choose == "1"):
            print("uploading photo")
            file_upload = open("foto1.jpg", "rb")
            content = file_upload.read()
            # pubfot = f"{pubtop} > Send Photo 1"
        elif (choose == "2"):
            print("uploading photo")
            file_upload = open("foto2.jpg", "rb")
            content = file_upload.read()
            # pubfot = f"{pubtop} > Send Photo 2"
        elif (choose == "3"):
            print("uploading photo")
            file_upload = open("foto3.jpg", "rb")
            content = file_upload.read()
            # pubfot = f"{pubtop} > Send Photo 3"
        print(kunyit)
        for i in range(len(kunyit)):
            if (choose == kunyit[i]):
                print("jangan sama woi")
            client.publish("photo", content)
        kunyit.append(choose)


    if (chat == "pendek"):
        kunyit.append("bisa")
        print(kunyit)
        if (len(kunyit) == 3):
            for i in range(len(kunyit)):
                if (kunyit[i] == "bisa" and kunyit[i+1] == "bisa" and kunyit[i+2] == "bisa"):
                    print("SELAMAT BOI")
        # print("SELAMAT BOIIIII")
    client.publish(pubtop, chat.encode())

    time_now = datetime.now()
    time_string = time_now.strftime("%H:%M")
    pubchat = f"{pubtop} > " + chat
    if (chat == "photo" or chat == "Photo" or chat == "PHOTO"):
        pubchat = f"{pubtop} > Sent a photo"
    hist = open("history_chat.txt", "a")
    var = pubchat + " " + "(" + time_string + ")"
    hist.write(var + "\n")
    hist.close()

client.loop_stop()
