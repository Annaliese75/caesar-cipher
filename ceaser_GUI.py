# Released under BSD License
# Sarah Schaffer


import decrypt as ck
import encrypt as ak
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
import sys, os

def btn_clear():
    txt_edit.delete("1.0", tk.END)
    txt_edit1.delete("1.0", tk.END)

# Decryption Function

def decrypt():
    message = txt_edit1.get(1.0, tk.END)
# Error catching for empty text boxes
    if message.strip() == '':
        messagebox.showinfo("Warning", "Text cannot be left blank.")
    else:

        l = len(message)
        decrypt_text = message[:l-1]
        cipher_txt = decrypt_text
        key=int(shift.get())
        decrypt_txt = ck.decrypt(cipher_txt, key)
        
# Read Textbox into string leaves random character so using l = len
# and Remove_last = decrypt_txt[:l-1] to strip last character
    l = len(decrypt_txt)
    Remove_last = decrypt_txt[:l-1]
    
    txt_edit1.delete("1.0", tk.END)
    txt_edit.insert(1.0, ""+ Remove_last)
    
def encrypt():
    message = txt_edit.get(1.0, tk.END)
# Error catching for empty text boxes
    if message.strip() == '':
        messagebox.showinfo("Warning", "Text cannot be left blank.")
    else:
        l = len(message)
        encrypt_text = message[:l-1]
        cipher_txt = encrypt_text
        key=int(shift.get())
        encrypt_txt = ak.encrypt(cipher_txt, key)
        
# Read Textbox into string leaves random character so using l = len
# and Remove_last = decrypt_txt[:l-1] to strip last character
    l = len(encrypt_txt)
    Remove_last = encrypt_txt[:l-1]
    
    txt_edit.delete("1.0", tk.END)
    txt_edit1.insert(1.0, ""+ Remove_last)

# Setup main window with form, this section also includes layout for text boxes
# and buttons
window = tk.Tk()
window.title("Encrypt/Decrypt")
window.rowconfigure(0, minsize=500, weight=1)
window.columnconfigure(1, minsize=500, weight=1)
txt_edit = tk.Text(window)
txt_edit1 = tk.Text(window)

frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=3)

btn_clear = tk.Button(frm_buttons, text="Clear!", command=btn_clear)
btn_encrypt = tk.Button(frm_buttons, text="Encrypt", command=encrypt)
btn_decrypt = tk.Button(frm_buttons, text="Decrypt", command=decrypt)
shift = tk.Entry(frm_buttons)

namelbl = tk.Label(frm_buttons, text="Shift Value 1-26")


btn_clear.grid(row=2, column=0, sticky="ew",padx=5)
btn_encrypt.grid(row=3, column=0, sticky="ew",padx=5)
btn_decrypt.grid(row=4, column=0, sticky="ew",padx=5)

namelbl.grid(row=7, column=0, sticky="ew", padx=5)
shift.grid(row=8, column=0, sticky="ew", padx=5)

frm_buttons.grid(row=0, column=0, sticky="ns")

txt_edit.grid(row=0, column=1, sticky="nsew")
txt_edit1.grid(row=0, column=2, sticky="nsew")


window.mainloop()
