import tkinter
import requests
from PIL import ImageTk, Image
import io


window = tkinter.Tk()
window.minsize(height=450, width=400)
window.title("Pokemon APP")


def Pokemon_info(pokemon_name):

    get_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(get_url)

    if response.status_code == 200:
        pokemon_data = response.json()
        pokemon_info = {
            "name": pokemon_data["name"],
            "height": pokemon_data["height"],
            "weight": pokemon_data["weight"],
            "abilities": [ability["ability"]["name"] for ability in pokemon_data["abilities"]],
            "types": [type_data["type"]["name"] for type_data in pokemon_data["types"]]
        }
        return pokemon_info
    else:
        return None

def Display_pokemon_info():

    pokemon_name = pokemon_name_Entry.get()
    pokemon_info = Pokemon_info(pokemon_name)
    if pokemon_info:
        info_text = f"Name:{pokemon_info['name']}\n"
        info_text += f"Height: {pokemon_info['height']}\n"
        info_text += f"Weight: {pokemon_info['weight']}\n"
        info_text += f"  Abilities: {', '.join(pokemon_info['abilities'])}\n"
        info_text += f"Types: {', '.join(pokemon_info['types'])}\n"
        pokemon_lastLabel.config(text=info_text,font=("Helvetica",13,"bold"))
    else:
        pokemon_lastLabel.config(text="Pokémon not found!",font=("Helvetica",13,"bold"),bg="yellow")



#button
pokemon_name_Button = tkinter.Button(text= "POKEMON NAME", command=Display_pokemon_info)
pokemon_name_Button.place(x=140,y=245)

# ENTRY
pokemon_name_Entry = tkinter.Entry()
pokemon_name_Entry.place(x=128, y=225)

#LABEL
pokemon_Label = tkinter.Label(text="Enter your Pokemon name")
pokemon_Label.place(x=120,y=200)
pokemon_lastLabel = tkinter.Label()
pokemon_lastLabel.place(x=90,y=270)
#Image

image = ImageTk.PhotoImage(Image.open("pokemon.png"))

image_label = tkinter.Label(width=200,height=200, image=image)
image_label.pack()



tkinter.mainloop()