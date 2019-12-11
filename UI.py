import tkinter as tk
import tkinter.scrolledtext as tkst
# tk.Button(root, text="teksti", command=funktio).grid(paikka)
# Entryyn kirjotettu saa ulos kun funktioon laittaa entry_n.get()
# Arvon voi itse määrätä muuttuja.set()
# Jos ei haluta käyttämisen jälkeen pitää muuttujaa -> muuttuja.delete(0, tk.END)

def click():
    txt = entry_textinput.get("1.0",'end-1c')
    return txt
#Window
#######
root = tk.Tk()
root.title("THE UI")
root.resizable(False, False)

#Labels
#######
label_url_input = tk.Label(root, text="URL").grid(row=0, column=0)
label_browserpath_input = tk.Label(root, text="Browser path").grid(row=1)
label_text_input = tk.Label(root, text="Input text").grid(row=2)
label_ = tk.Label(root, text=" ").grid(row=5)
label_output_bs4 = tk.Label(root, text="Named entities (Bs4)").grid(row=6)
label_output_neural = tk.Label(root, text="Named entities (Neural coreference)").grid(row=8)

#Inputs
#######
entry_url = tk.Entry(root).grid(row=0, column=1,ipadx=200, sticky=tk.W)
entry_browserpath = tk.Entry(root).grid(row=1, column=1,ipadx=200, sticky=tk.W)

entry_textinput = tkst.ScrolledText(root, wrap = tk.WORD, width = 90, height = 10)
entry_textinput.grid(row=4, column=0, columnspan=2)



#Output
#######
output_bs4_frame = tk.Frame(master = root, bg='#808000')
output_bs4_frame.grid(row=7, columnspan=2, sticky=tk.W)
output_bs4_area = tkst.ScrolledText(master = output_bs4_frame, wrap = tk.WORD, width = 90, height = 10)
output_bs4_area.grid(row=7 ,columnspan=2)

output_neuro_frame = tk.Frame(master = root, bg='#808000')
output_neuro_frame.grid(row=10, columnspan=2, sticky=tk.W)
output_neuro_area = tkst.ScrolledText(master = output_neuro_frame, wrap = tk.WORD, width = 90, height = 10)
output_neuro_area.grid(row=10, columnspan=2)


#Buttons
########
quit = tk.Button(root, text="Quit", width=15, command=root.quit).grid(row=15,column=1, pady=4)
parse = tk.Button(root, text="Parse", width=15, ).grid(row=15,column=0,sticky=tk.E, pady=4)
ok = tk.Button(root, text="Ok", width=15, command=click).grid(row=5, column=1)




##############
root.mainloop()