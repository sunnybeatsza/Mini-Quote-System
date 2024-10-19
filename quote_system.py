import random

Quotees = ["Abdullah Ibrahim","Miriam Makeba", "Nelson Mandela", "Eleanor Roosevelt",
 "Anne Frank", "Alexander Graham Bell","Thomas Edison","Estee Lauder","Maya Angelou", "Walt Disney"]

# TODO: Step 2 - Correct the functionality in the function below to successfully open file
#                and to sucessfully handle the FileNotFoundError. 
def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            text = file.read()
            return text
    except FileNotFoundError as error:
        print(f"""FileNotFoundError successfully handled
{error}""") 
pass



# TODO: Step 1 - update the below function to correctly choose text file chosen from command line arguments. 
#                Use `quotes.txt` for blank user input.

def ask_file_name(user_input):
    if user_input:
        return user_input
    else:
        return "quotes.txt"
pass



# TODO: Step 3 - randomly select quotee from `Quotees` list and return a random quotee. 
def select_random_quotee(Quotees):

    return random_quotee

# TODO: Step 4 - correct the functionality in the function below to 
#                match quote from text file to chosen quotee. 
#                "Quote/quotee does not exist." must be returned for quote that doesn't exist.
def find_quote(random_quotee,quotes):
    return quote


# TODO: Step 5 - Correctly print out the final results to pass the unitests.
def final_output(quote,quotee):
    pass
 
if __name__ == "__main__":
    """
     You can leave this code as is, and only implemented above where the code comments prompt you.
     """
    user_input = input("Desired file? [leave empty to use quotes.txt] :")
    quotes_file = ask_file_name(user_input)
    print(repr(str(quotes_file)) + ': is your chosen file.\n')
    quotes = read_file(quotes_file).split("\n\n")
    random_quotee = select_random_quotee(Quotees)
    if random_quotee == "":
        print('Empty list.\n')
    else:
        print(str(random_quotee) + ' has randomly been chosen.\n')
    true_quote = find_quote(random_quotee,quotes)
    if true_quote == "":
        print(str(random_quotee) + ' is not present in the file\n')
        quit()
    else:
        print(str(random_quotee) + ' is present in the file\n')
        final_output(true_quote,random_quotee)