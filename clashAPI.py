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
def getInput():
    input = inputEntry.get()
    return input
def getCardData():
    global data
    global cardStatus
    name = getInput()
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImQ5YjI1MWIzLTY5M2QtNGVhZS1iZTkxLTI3NmQxZjdlYjcyOSIsImlhdCI6MTc2NDE2ODAzNCwic3ViIjoiZGV2ZWxvcGVyLzIzYzBlM2JhLWQ1YmQtMzU5Zi1hM2NiLTliMzFiZjk0ZDM5YyIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxNjUuMTU1LjE2NC4xNiJdLCJ0eXBlIjoiY2xpZW50In1dfQ.9AyyT7PJcwWUVZvYeb6eS_IpCTJOfyM6i49lM0byv80xLb-nRk3ku0UamzikhK6L_PTCG9GDJtvPpVk0IoWUtA"
    api_key = {"Authorization": f"Bearer {token}"}
    response = requests.get("https://api.clashroyale.com/v1" + endpoint, api_key) 
    if response.status_code != 200 and response.status_code!= 403:
        print("Error fetching data!")
        print(response)
        print(response.json())
        return None
    if response.status_code == 403:
        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjhlZTU1MTg0LTg4MzQtNDI5ZC1iZTE5LTI3ODhhNWM2MjM0NyIsImlhdCI6MTc2NDE2ODEwMiwic3ViIjoiZGV2ZWxvcGVyLzIzYzBlM2JhLWQ1YmQtMzU5Zi1hM2NiLTliMzFiZjk0ZDM5YyIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxNjUuMTU1LjE2My41Il0sInR5cGUiOiJjbGllbnQifV19.qDGz1KhmbidyL0HsNEmoipsXDOFrZJhetbfOYlDb7sI9TW6VUsvkMAHJOMOIR8tRxRW0kq8VJEMxgtvyhxUibA"
        api_key = {"Authorization": f"Bearer {token}"}
        response = requests.get("https://api.clashroyale.com/v1" + endpoint, api_key)
    data = response.json()
    for i in range(len(data["items"])):
        try:
            if data["items"][i]["name"] == name:
                data = data["items"][i]
                nameLabel = tk.Label(window, text=f"Name: {data["name"]}").grid(column=2,row=2)
                elixirLabel = tk.Label(window, text=f"Elixir Cost: {data["elixirCost"]}").grid(column=2,row=3)
                rarityLabel = tk.Label(window, text=f"Rarity: {data["rarity"]}").grid(column=2,row=4)
                imgResponse = requests.get(data["iconUrls"]["medium"])
                imgData = imgResponse.content
                img = Image.open(BytesIO(imgData))
                photo = ImageTk.PhotoImage(img)
                photoLabel = Label(window, image=photo)
                photoLabel.grid(column=1,row=2)
                photoLabel.image = photo
                evoButton = tk.Button(window, text = "Evolve",command=evo).grid(column=1,row=3)
                heroButton = tk.Button(window, text = "Hero",command=hero).grid(column=1,row=4)
                tks.append(nameLabel)
                
                cardStatus = 1

            elif i == len(data["items"]) - 1:
                print("card not found")
        except KeyError:
            continue
def evo():
    global cardStatus
    if cardStatus != 2:
        try:
            imgResponse = requests.get(data["iconUrls"]["evolutionMedium"])
            imgData = imgResponse.content
            img = Image.open(BytesIO(imgData))
            photo = ImageTk.PhotoImage(img)
            photoLabel = Label(window, image=photo)
            photoLabel.grid(column=1,row=2)
            photoLabel.image = photo
            cardStatus = 2
        except KeyError:
            print("Card does not have a evolution.")
            return
    else:
        imgResponse = requests.get(data["iconUrls"]["medium"])
        imgData = imgResponse.content
        img = Image.open(BytesIO(imgData))
        photo = ImageTk.PhotoImage(img)
        photoLabel = Label(window, image=photo)
        photoLabel.grid(column=1,row=2)
        photoLabel.image = photo
        cardStatus = 1
def hero():
    global cardStatus
    if cardStatus != 3:
        try:
            imgResponse = requests.get(data["iconUrls"]["heroMedium"])
            imgData = imgResponse.content
            img = Image.open(BytesIO(imgData))
            photo = ImageTk.PhotoImage(img)
            photoLabel = Label(window, image=photo)
            photoLabel.grid(column=1,row=2)
            photoLabel.image = photo
            cardStatus = 3
        except KeyError:
            print("Card does not have a hero.")
            return
    else:
        imgResponse = requests.get(data["iconUrls"]["medium"])
        imgData = imgResponse.content
        img = Image.open(BytesIO(imgData))
        photo = ImageTk.PhotoImage(img)
        photoLabel = Label(window, image=photo)
        photoLabel.grid(column=1,row=2)
        photoLabel.image = photo
        cardStatus = 1

inputEntry = tk.Entry(window)
inputEntry.grid(column=1,row=1)
searchButton = tk.Button(window, text = "Search", command=getCardData).grid(column=2,row=1)


window.mainloop()