#!/usr/bin/env python3
"""Bloco de notas

$ notes.py new "Minha nota"
tag: tech
text:
Anotacao geral sobre carreira de tecnologia

$ notes.py read tech
...
...
"""

__version__ = "0.1.0" 
__author__ = "Bruno Nascimento"
__license__ = "Unlicense"

import os
import sys

cmds = ("read", "new")
path = os.curdir
filepath = os.path.join(path, "notes.txt")

# Lê/Valida argumentos
arguments = sys.argv[1:]

if not arguments:
    print("Invalid usage.") 
    print(f"You must specify one of the subcommands: {cmds}.")
    sys.exit(1)

if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}.")
    sys.exit(1)

while True:

    # Leitura de notas        
    if arguments[0] == "read":
        try:
            arg_tag = arguments[1].lower()
        except IndexError:
            arg_tag = input("What is the tag? ").strip().lower()
        
        for line in open(filepath):
            title, tag, text = line.split("\t")
            
            if tag.lower() == arg_tag:
                print(f"Title: {title}")
                print(f"Text: {text}")
                print("-" * 30)
                print()

    # Criação de nova nota
    if arguments[0] == "new":
        try:
            title = arguments[1]
        except IndexError:
            title = input("What is the title? ").strip().title()

        text = [
            f"{title}",
            input("tag: ").strip(),
            input("text: \n").strip()
        ]
        # \t - tsv (tab separated values)
        with open(filepath, "a") as note_file:
            note_file.write("\t".join(text) + "\n")
    
    cont = input(f"Would you like to continue add/read-ing notes? [n/y]").strip().lower()
    
    if cont != "y":
        break