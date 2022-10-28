country_types = ["decentralized", "unrecognized", "recognized"]
country_tiers = ["principality", "grand_principality", "kingdom", "empire"]
writing_type = input("Overwrite or add (w to overwrite, a to add): ")
file_name = input("file to write to: ") + ".txt"
with open(file_name, writing_type) as file:
    looping = True
    while looping:
        tag = input("Country tag: ")
        color = input("Colour (RGB format): ")
        country_recognition = country_types[int(input("Country type \n0 = decentralized \n1 = unrecognized\n2 = recognized: "))]
        country_tier = country_tiers[int(input("Country tier \n0 = principality \n1 = grand_principality\n2 = kingdom\n3 = empire: "))]
        cultures = input("List all primary cultures with a space between each: ")
        capital = input("Capital state (Just the part after the _): ")
        #named_after_capital = input("Named after capital (\"yes\" or \"no\"): ")
        file.write(
            tag + " = {\n"+
            "\tcolor = { "+color+" }"+
            "\n\n"+
            "\tcountry_type = "+country_recognition+
            "\n\n"+
            "\ttier = "+country_tier+
            "\n\n"+
            "\tcultures = { "+cultures+" }\n"+
            "\tcapital = STATE_"+capital+
            "\n}\n\n"
        )
        continuing = input("Continue writing? (0=yes, 1=no): ")
        if continuing != "0":
            looping = False
