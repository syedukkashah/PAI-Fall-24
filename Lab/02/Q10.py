def build_message(**info):
    if not info:
        print("No info given\n")
        return
    for i, j in info.items(): #looping through both the keys and values in the dictionary by using the items function
        print(i,":",j,"\n")


build_message(name = "ukkashah", age = 20, occupation = "student")
    