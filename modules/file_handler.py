def read_text_file(filepath:str) -> str:
    
    try:

        f = open(filepath, "r")
        text = f.read()
    except FileNotFoundError as e:
            print("File '{}' not found.".format(filepath))
            exit()
    
    return text