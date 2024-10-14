# beginner tbh anyways

import tkinter as tk
import random

root = tk.Tk()
root.title("Lua Obfuscator")
root.geometry("600x400")

def obfuscate_lua():
    lua_input = lua_input_text.get("1.0", tk.END)
    words = lua_input.split()
    obfuscated_words = []
    
    for word in words:
        if word.isalpha():
            obfuscated_word = "var" + str(random.randint(1000, 9999))
            obfuscated_words.append(obfuscated_word)
        else:
            obfuscated_words.append(word)
    
    obfuscated_code = " ".join(obfuscated_words)
    lua_output_text.delete("1.0", tk.END)
    lua_output_text.insert(tk.END, obfuscated_code)

lua_input_label = tk.Label(root, text="Enter Lua code:")
lua_input_label.pack()

lua_input_text = tk.Text(root, height=10)
lua_input_text.pack()

obfuscate_button = tk.Button(root, text="Obfuscate", command=obfuscate_lua)
obfuscate_button.pack()

lua_output_label = tk.Label(root, text="Obfuscated Lua code:")
lua_output_label.pack()

lua_output_text = tk.Text(root, height=10)
lua_output_text.pack()

root.mainloop()
