"""
CP1404 Practical
Hex Colour Names Dictionary
"""

COLOUR_NAMES = {"Apricot": "#fbceb1", "Cadetblue": "#5f9ea0", "Ferngreen": "#4f7942", "Goldenrod": "#daa520",
                "Jade": "#00a86b", "Limegreen": "#32cd32", "Pacificblue": "#1ca9c9", "Plum": "#8e4585",
                "Springbud": "#a7fc00", "Wisteria": "#c9a0dc"}

colour_name = input("Enter colour name: ").title()
while colour_name != "":
    try:
        print(f"{colour_name} is {COLOUR_NAMES[colour_name]}")
    except KeyError:
        print("Invalid Colour")
    colour_name = input("Enter colour name: ").title()
