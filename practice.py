def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            text = file.read()
            return text
    except FileNotFoundError as error:
        print(f"""FileNotFoundError successfully handled
{error}""") 
