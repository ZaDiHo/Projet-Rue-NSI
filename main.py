from tkinter import *
import yaml
from yaml import Loader

#
# * Nom de classe : main.py
# * Description   : Class principale du projet
# * Version       : 0.1
# * Date          : 12/09/2023
# * Auteur        : Thomas PROVOST
#

# Accès au fichier de configuration config.yml
with open("config.yml", "r") as ymlfile:
    config = yaml.load(ymlfile, Loader=Loader)

# Création de la fenêtre principale
window = Tk()
window.title("Projet Rue NSI - Thomas PROVOST")
window.geometry("1920x1080")
window.config(background=config["global"]["background_color"])

# Création du sol
ground = Canvas(window, width=1920, height=200, highlightthickness=0, bg=config["global"]["ground_color"])
ground.pack(side="bottom")

window.mainloop()

ground = Canvas(window, width=1920, height=200, highlightthickness=0, bg=config["global"]["background_color"])
ground.pack(side="bottom")