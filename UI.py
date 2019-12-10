import tkinter as tk
import tkinter.scrolledtext as tkst
# tk.Button(root, text="teksti", command=funktio).grid(paikka)
# Entryyn kirjotettu saa ulos kun funktioon laittaa entry_n.get()
# Arvon voi itse määrätä muuttuja.set()
# Jos ei haluta käyttämisen jälkeen pitää muuttujaa -> muuttuja.delete(0, tk.END)
root = tk.Tk()
root.title("THE UI")


#Labels
label_url_input = tk.Label(root, text="URL").grid(row=0, column=0)
label_browserpath_input = tk.Label(root, text="Browser path").grid(row=1)
label_text_input = tk.Label(root, text="Input text").grid(row=2) 
label_output_bs4 = tk.Label(root, text="Named entities (Bs4)").grid(row=4)
label_output_neural = tk.Label(root, text="Named entities (Neural coreference)").grid(row=7)

#Inputs
entry_url = tk.Entry(root).grid(row=0, column=1, sticky=tk.W)
entry_browserpath = tk.Entry(root).grid(row=1, column=1, sticky=tk.W)
entry_textinput = tk.Entry(root).grid(row=2, column=1, sticky=tk.W)

#Output
output_bs4_frame = tk.Frame(master = root, bg='#808000')
output_bs4_frame.grid(row=5,columnspan=2)
output_bs4_area = tkst.ScrolledText(master = output_bs4_frame, wrap = tk.WORD, width = 40, height = 10)
output_bs4_area.grid(row=5,columnspan=2)
output_bs4_area.insert(tk.INSERT, """\
Integer posuere erat a ante venenatis dapibus.
Posuere velit aliquet.
Aenean eu leo quam. Pellentesque ornare sem.
Lacinia quam venenatis vestibulum.
Nulla vitae elit libero, a pharetra augue.
Cum sociis natoque penatibus et magnis dis.
Parturient montes, nascetur ridiculus mus.
""")

output_neuro_frame = tk.Frame(master = root, bg='#808000')
output_neuro_frame.grid(row=8, columnspan=2)
output_neuro_area = tkst.ScrolledText(master = output_neuro_frame, wrap = tk.WORD, width = 40, height = 10)
output_neuro_area.grid(row=8, columnspan=2)




#Buttons
quit = tk.Button(root, text="Quit", width=15, command=root.quit).grid(row=10,column=1, pady=4)
parse = tk.Button(root, text="Parse", width=15, ).grid(row=10,column=0,sticky=tk.E, pady=4)










root.mainloop()