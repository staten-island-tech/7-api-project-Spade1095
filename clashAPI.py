import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO
from tkinter import Label
endpoint = "/cards"
window = tk.Tk()
data = []
cardStatus = 1
tks = []
def photoShenanigans(imgResponse):
        imgData = imgResponse.content
        img = Image.open(BytesIO(imgData))
        photo = ImageTk.PhotoImage(img)
        photoLabel = Label(window, image=photo)
        photoLabel.grid(column=1,row=2)
        photoLabel.image = photo
def getInput():
    input = inputEntry.get()
    return input
def getCardData():
    global data
    global cardStatus
    name = getInput()
    # Schrödinger's IP Adress
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImQ5YjI1MWIzLTY5M2QtNGVhZS1iZTkxLTI3NmQxZjdlYjcyOSIsImlhdCI6MTc2NDE2ODAzNCwic3ViIjoiZGV2ZWxvcGVyLzIzYzBlM2JhLWQ1YmQtMzU5Zi1hM2NiLTliMzFiZjk0ZDM5YyIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxNjUuMTU1LjE2NC4xNiJdLCJ0eXBlIjoiY2xpZW50In1dfQ.9AyyT7PJcwWUVZvYeb6eS_IpCTJOfyM6i49lM0byv80xLb-nRk3ku0UamzikhK6L_PTCG9GDJtvPpVk0IoWUtA"
    api_key = {"Authorization": f"Bearer {token}"}
    response = requests.get("https://api.clashroyale.com/v1" + endpoint, api_key) 
    if response.status_code != 200 and response.status_code != 403:
        print("Error fetching data!")
        print(response)
        print(response.json())
        # return None
    if response.status_code == 403:
        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjExMDBiMGJkLTViODItNDQ5Yi05ZGZmLWZiNzYwNDg5MmI3OSIsImlhdCI6MTc2NTQ2NTM1NCwic3ViIjoiZGV2ZWxvcGVyLzIzYzBlM2JhLWQ1YmQtMzU5Zi1hM2NiLTliMzFiZjk0ZDM5YyIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxNjUuMTU1LjE3Mi42Il0sInR5cGUiOiJjbGllbnQifV19.MVhP7qf_aF35xsXoANGc5lMo3prBPaHmD-IB0-aKkSGdP2rTiT0nGrWG3Rm6OukOvBkZFagwPJLnWbfnuk9B0g"
        api_key = {"Authorization": f"Bearer {token}"}
        response = requests.get("https://api.clashroyale.com/v1" + endpoint, api_key)
        print("IP number 2")
    
    data = response.json()

    # find data
    try:
        test = data["items"]
    except KeyError:
        print('items doesnt exsit')
    for i in range(len(data["items"])):
        try:
            if data["items"][i]["name"] == name:
                data = data["items"][i]
                # deleate previus labels
                if len(tks) > 0:
                    for i in range(len(tks)):
                        tks[i].destroy()
                # make labels
                nameLabel = tk.Label(window, text=f"Name: {data["name"]}")
                elixirLabel = tk.Label(window, text=f"Elixir Cost: {data["elixirCost"]}")
                rarityLabel = tk.Label(window, text=f"Rarity: {data["rarity"]}")
                nameLabel.grid(column=2,row=2)
                elixirLabel.grid(column=2,row=3)
                rarityLabel.grid(column=2,row=4)
                photoShenanigans(requests.get(data["iconUrls"]["medium"]))
                cardStatus = 1
                # buttons
                evoButton = tk.Button(window, text = "Evolve",command=evo).grid(column=1,row=3)
                heroButton = tk.Button(window, text = "Hero",command=hero).grid(column=1,row=4)
                # add labels to list so they could be delated 
                tks.append(nameLabel)
                tks.append(elixirLabel)
                tks.append(rarityLabel)
            elif i == len(data["items"]) - 1:
                print("card not found")
        except KeyError:
            continue
def evo():
    global cardStatus
    if cardStatus != 2:
        try:
            photoShenanigans(requests.get(data["iconUrls"]["evolutionMedium"]))
            cardStatus = 2
        except KeyError:
            print("Card does not have a evolution.")
            return
    else:
        photoShenanigans(requests.get(data["iconUrls"]["medium"]))
        cardStatus = 1
def hero():
    global cardStatus
    if cardStatus != 3:
        try:
            photoShenanigans(requests.get(data["iconUrls"]["heroMedium"]))
            cardStatus = 3
        except KeyError:
            print("Card does not have a hero.")
            return
    else:
        photoShenanigans(requests.get(data["iconUrls"]["medium"]))
        cardStatus = 1

inputEntry = tk.Entry(window)
inputEntry.grid(column=1,row=1)
searchButton = tk.Button(window, text = "Search", command=getCardData).grid(column=2,row=1)

window.mainloop()