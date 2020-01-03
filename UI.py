import tkinter as tk
import tkinter.scrolledtext as tkst
from parse_url_to_text import parse_body_text_from_url
from test import download_nltk_packages, TextContainer 


# tk.Button(root, text="teksti", command=funktio).grid(paikka)
# Entryyn kirjotettu saa ulos kun funktioon laittaa entry_n.get()
# Arvon voi itse määrätä muuttuja.set()
# Jos ei haluta käyttämisen jälkeen pitää muuttujaa -> funktion loppuun muuttuja.delete(0, tk.END)


def click_ok():
    global TEXT_FROM_URL
    url = entry_url.get()
    browser_path = entry_browserpath.get()
    TEXT_FROM_URL = parse_body_text_from_url(url)

    # print(url)
    # print(browser_path)
    entry_textinput.insert("insert",TEXT_FROM_URL)
    return url, browser_path


def click_parse():
    global TEXT_FROM_URL
    str = ""
    wholetext = TextContainer(TEXT_FROM_URL)
    for index, sentence in enumerate(wholetext.sentences):
        if len(sentence.nes) != len(sentence.ne_indexes): # sanity check
            print("index mismatch in sentence", index)
            exit()
        # print("─"*80)
        # print("SENTENCE INDEX:", index)
        str += sentence.tmp_output()
    output_bs4_area.insert("insert",str)


# download needed nltk packages to be ready for use
download_nltk_packages()

# Window
#######
root = tk.Tk()
root.title("THE UI")
root.resizable(False, False)

# Labels
#######
tk.Label(root, text="URL").grid(row=0, column=0)
tk.Label(root, text="Browser path").grid(row=1)
tk.Label(root, text="Input text").grid(row=2)
tk.Label(root, text="Output:").grid(row=5, padx=21, sticky=tk.W)
tk.Label(root, text="Named entities (NLTK & spaCy)").grid(row=6)
tk.Label(root, text="Named entities (Neural coreference)").grid(row=8)

# Inputs
#######
entry_url = tk.Entry(root)
entry_url.grid(row=0, column=1, ipadx=200, sticky=tk.W)

entry_browserpath = tk.Entry(root)
entry_browserpath.grid(row=1, column=1, ipadx=200, sticky=tk.W)

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
ok_button = tk.Button(root, text="Ok", width=15, command=click_ok).grid(
    row=0, column=2, rowspan=2, sticky=tk.N + tk.S
)
quit_button = tk.Button(root, text="Quit", width=15, command=root.quit).grid(
    row=15, column=2, pady=4
)
parse_button = tk.Button(root, text="Parse", width=15, command=click_parse).grid(
    row=15, column=1, sticky=tk.E, pady=4
)


##############
root.mainloop()
