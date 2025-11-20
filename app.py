import requests
import tkinter
tk = tkinter
def getInput():
    input = inputEntry.get()
    return input
window = tk.Tk()
inputLabel = tk.Label(window,text="What pokemon?")
inputEntry = tk.Entry(window)
inputButton = tk.Button(window,text="Submit pokemon",command=getInput)
inputEntry.grid(row=1,column=2)
inputLabel.grid(row=1,column=1)
inputButton.grid(row=1,column=3)
def getPokeData(poke):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    data = response.json()
    return {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]]
    }
print(getPokeData("Bulbasaur"))
window.mainloop()