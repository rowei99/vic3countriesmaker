from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
from tkinter import filedialog

class Main:
    def __init__(self, root):
        root.title("Victoria 3 Modding Aid")
        
        current_cultures = StringVar()
        current_colour = StringVar()
        path_to_countries_file = StringVar()
        current_tag = StringVar()
        current_captial = StringVar()

        def choose_color():
            # variable to store hexadecimal code of color
            current_colour.set("Current colour: " + str(colorchooser.askcolor(title ="Choose color")[0]))
            
        def select_file():
            path_to_countries_file.set(filedialog.askopenfilename())

        def write_to_country_definitions():
            with open (path_to_countries_file.get(),radio_writing_mode.get()) as file:
                file.write(
                    current_tag.get() + " = {\n"+
                        "\tcolor = { "+current_colour.get()+" }"+
                        "\n\n"+
                        "\tcountry_type = "+recognition.get()+
                        "\n\n"+
                        "\ttier = "+radio_tier.get()+
                        "\n\n"+
                        "\tcultures = { "+current_cultures.get()+" }\n"+
                        "\tcapital = STATE_"+current_captial.get()+
                        "\n}\n\n"
                    )

        frame = ttk.Frame(root, padding="3 3 12 12")
        frame.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        recognition = StringVar()
        radio_decentralized = ttk.Radiobutton(frame, text="Decentralized", 
        variable=recognition, value=0)
        radio_unrecognized = ttk.Radiobutton(frame, text="Unrecognized", 
        variable=recognition, value=1)
        radio_recognized = ttk.Radiobutton(frame, text="Recognized", 
        variable=recognition, value=2)

        radio_decentralized.grid(column=1, row=0, sticky=W)
        radio_unrecognized.grid(column=1, row=1, sticky=W)
        radio_recognized.grid(column=1, row=2, sticky=W)

        radio_tier = StringVar()
        radio_principality = ttk.Radiobutton(frame, text="Principality", 
        variable=radio_tier, value=0)
        radio_grand_principality = ttk.Radiobutton(frame, text="Grand Principality", 
        variable=radio_tier, value=1)
        radio_kingdom = ttk.Radiobutton(frame, text="Kingdom", 
        variable=radio_tier, value=2)
        radio_empire = ttk.Radiobutton(frame, text="Empire",
        variable=radio_tier, value=3)

        radio_principality.grid(column=2, row=0, sticky=W)
        radio_grand_principality.grid(column=2, row=1, sticky=W)
        radio_kingdom.grid(column=2, row=2, sticky=W)
        radio_empire.grid(column=2, row=3, sticky=W)

        radio_writing_mode = StringVar()
        radio_overwrite = ttk.Radiobutton(frame, text="Overwrite contents", 
        variable=radio_writing_mode, value="w")
        radio_add = ttk.Radiobutton(frame, text="Add to contents", 
        variable=radio_writing_mode, value="a")

        radio_overwrite.grid(column=0,row=0)
        radio_add.grid(column=0,row=1)


        colour_button = ttk.Button(frame, text="Choose Colour", command=choose_color).grid(column=2, row=4)
        colour_label = ttk.Label(frame, textvariable=current_colour).grid(column=3, row=4)
        
        file_select_button = ttk.Button(frame, text="Select file", command=select_file).grid(column=4, row=4)
        path_label = ttk.Label(frame, textvariable=path_to_countries_file).grid(column=5, row=4)

        tag_entry_label = ttk.Label(frame, text="Three letter tag:").grid(column=3,row=0)
        tag_entry = ttk.Entry(frame, textvariable = current_tag).grid(column=4,row=0)

        cultures_entry_label = ttk.Label(frame, text="Primary cultures:").grid(column=3,row=1)
        cultures_entry = ttk.Entry(frame, textvariable = current_cultures).grid(column=4,row=1)

        capital_entry_label = ttk.Label(frame, text="Captial state: STATE_").grid(column=3,row=2)
        capital_entry = ttk.Entry(frame, textvariable = current_captial).grid(column=4,row=2)

        ttk.Button(frame, text="Quit", command=root.destroy).grid(column=0, row=4)

        write_button = ttk.Button(frame, text="Write to file", command = write_to_country_definitions).grid(column=1,row=4)


root = Tk()
Main(root)
root.mainloop()