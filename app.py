import requests
import tkinter
tk = tkinter
def getInput():
    input = inputEntry.get()
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{input.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    data = response.json()
    nameLabel = tk.Label(window,text=f"name: {data["name"]}").grid(column=5,row=1)
    heightLabel = tk.Label(window,text=f"height: {data["height"]}").grid(column=5,row=2)
    weightLabel = tk.Label(window,text=f"weight: {data["weight"]}").grid(column=5,row=3)
    typesLabel = tk.Label(window,text=f"types:{[t["type"]["name"] for t in data["types"]]}").grid(column=5,row=4)
window = tk.Tk()
inputLabel = tk.Label(window,text="What pokemon?")
inputEntry = tk.Entry(window)
inputButton = tk.Button(window,text="Submit pokemon",command=getInput)
inputEntry.grid(row=1,column=2)
inputLabel.grid(row=1,column=1)
inputButton.grid(row=1,column=3)

window.mainloop()