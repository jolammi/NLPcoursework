import tkinter as tk
import tkinter.scrolledtext as tkst
from parse_url_to_text import parse_body_text_from_url
from parse_refs_from_text import download_nltk_packages, TextContainer
from neural_coreference import neural_coreference
import time


# tk.Button(root, text="teksti", command=funktio).grid(paikka)
# Entryyn kirjotettu saa ulos kun funktioon laittaa entry_n.get()
# Arvon voi itse määrätä muuttuja.set()
# Jos ei haluta käyttämisen jälkeen pitää muuttujaa -> funktion loppuun muuttuja.delete(0, tk.END)


def click_ok(root):
    a = tk.Label(root, text="Getting article text...", font='Helvetica 14 bold')
    a.grid(row=15)
    root.update_idletasks()
    global TEXT_FROM_URL
    url = entry_url.get()
    TEXT_FROM_URL = parse_body_text_from_url(url)

    # print(url)
    entry_textinput.delete('1.0', tk.END)
    entry_textinput.insert("insert", TEXT_FROM_URL)
    a.grid_forget()

    return url

def click_parse(root):
    global TEXT_FROM_URL
    b = tk.Label(
        root,
        text="Parsing, please wait...",
        font='Helvetica 14 bold'
    )
    b.grid(row=15)
    root.update_idletasks()
    str = ""
    wholetext = TextContainer(entry_textinput.get(1.0, tk.END))
    # for index, sentence in enumerate(wholetext.sentences):
    #     if len(sentence.nes) != len(sentence.ne_indexes): # sanity check
    #         print("index mismatch in sentence", index)
    #         exit()
    #     # print("─"*80)
    #     # print("SENTENCE INDEX:", index)
        # str += sentence.tmp_output()
    wholetext.parse_corefs()
    output_bs4 = wholetext.pprint_final()

    output_bs4_area.delete('1.0', tk.END)
    output_neuro_area.delete('1.0', tk.END)

    output_bs4_area.insert("insert",output_bs4)
    output_neuro_area.insert(
        "insert", neural_coreference(entry_textinput.get(1.0, tk.END))
    )

    b.grid_forget()


# download needed nltk packages to be ready for use
download_nltk_packages()

# Window
#######
root = tk.Tk()
root.title("Named Entity Coreference Resolution")
root.resizable(False, False)

# Labels
#######
tk.Label(root, text="URL").grid(row=0, column=0)
tk.Label(root, text="Input text").grid(row=2)
tk.Label(root, text="Output:").grid(row=5, padx=21, sticky=tk.W)
tk.Label(root, text="Named entities (NLTK & spaCy)").grid(row=6)
tk.Label(root, text="Named entities (Neural coreference)").grid(row=8)

# Inputs
#######
entry_url = tk.Entry(root)
entry_url.grid(row=0, column=1, ipadx=200, sticky=tk.W)

entry_textinput = tkst.ScrolledText(root, wrap=tk.WORD, width=90, height=10)
entry_textinput.grid(row=4, column=0, columnspan=3, sticky=tk.W + tk.E)


# Output
#######
output_bs4_frame = tk.Frame(master=root)
output_bs4_frame.grid(row=7, columnspan=3, sticky=tk.W + tk.E)
output_bs4_area = tkst.ScrolledText(
    master=output_bs4_frame, wrap=tk.WORD, width=110, height=10
)
output_bs4_area.grid(row=7, columnspan=3, sticky=tk.W + tk.E)

output_neuro_frame = tk.Frame(master=root)
output_neuro_frame.grid(row=10, columnspan=3, sticky=tk.W + tk.E)
output_neuro_area = tkst.ScrolledText(
    master=output_neuro_frame, wrap=tk.WORD, width=110, height=10
)
output_neuro_area.grid(row=10, columnspan=3, sticky=tk.W + tk.E)


# Buttons
########
ok_button = tk.Button(root, text="Ok", width=15,
    command=lambda: click_ok(root)).grid(
    row=0, column=2, rowspan=2, sticky=tk.N + tk.S
)
quit_button = tk.Button(root, text="Quit", width=15, command=root.quit).grid(
    row=15, column=2, pady=4
)
parse_button = tk.Button(root, text="Parse", width=15,
    command=lambda: click_parse(root)).grid(
    row=15, column=1, sticky=tk.E, pady=4
)

##############
root.mainloop()
