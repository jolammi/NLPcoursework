import tkinter as tk
import tkinter.scrolledtext as tkst
# tk.Button(root, text="teksti", command=funktio).grid(paikka)
# Entryyn kirjotettu saa ulos kun funktioon laittaa entry_n.get()
# Arvon voi itse määrätä muuttuja.set()
# Jos ei haluta käyttämisen jälkeen pitää muuttujaa -> funktion loppuun muuttuja.delete(0, tk.END)

def click():
    url = entry_url.get()
    browser_path = entry_browserpath.get()
    print(url)
    print(browser_path)
    return url, browser_path

#Window
#######
root = tk.Tk()
root.title("THE UI")
root.resizable(False, False)

#Labels
#######
tk.Label(root, text="URL").grid(row=0, column=0)
tk.Label(root, text="Browser path").grid(row=1)
tk.Label(root, text="Input text").grid(row=2)
tk.Label(root, text="Output:").grid(row=5, padx=21,sticky=tk.W)
tk.Label(root, text="Named entities (NLTK & spaCy)").grid(row=6)
tk.Label(root, text="Named entities (Neural coreference)").grid(row=8)

#Inputs
#######
entry_url = tk.Entry(root)
entry_url.grid(row=0, column=1,ipadx=200, sticky=tk.W)

entry_browserpath = tk.Entry(root)
entry_browserpath.grid(row=1, column=1,ipadx=200, sticky=tk.W)

entry_textinput = tkst.ScrolledText(root, wrap = tk.WORD, width = 90, height = 10)
entry_textinput.grid(row=4, column=0, columnspan=3, sticky=tk.W+tk.E)


#Output
#######
output_bs4_frame = tk.Frame(master = root)
output_bs4_frame.grid(row=7, columnspan=3, sticky=tk.W+tk.E)
output_bs4_area = tkst.ScrolledText(master = output_bs4_frame, wrap = tk.WORD, width = 110, height = 10)
output_bs4_area.grid(row=7 ,columnspan=3, sticky=tk.W+tk.E)

output_neuro_frame = tk.Frame(master = root)
output_neuro_frame.grid(row=10, columnspan=3, sticky=tk.W+tk.E)
output_neuro_area = tkst.ScrolledText(master = output_neuro_frame, wrap = tk.WORD, width = 110, height = 10)
output_neuro_area.grid(row=10, columnspan=3, sticky=tk.W+tk.E)


#Buttons
########
tk.Button(root, text="Quit", width=15, command=root.quit).grid(row=15,column=2, pady=4)
tk.Button(root, text="Parse", width=15, ).grid(row=15,column=1,sticky=tk.E, pady=4)
tk.Button(root, text="Ok", width=15, command=click).grid(row=0, column=2, rowspan=2, sticky=tk.N+tk.S)




##############
root.mainloop()