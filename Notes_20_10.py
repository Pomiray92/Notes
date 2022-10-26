# TODO: design a prompt 
import sys, os
import uuid
 
ROOT_FOLDER = os.getcwd()
ARTICLE_FOLDER = f"{ROOT_FOLDER}/src/data/articles"
LOG_FOLDER = f"{ROOT_FOLDER}/src/data/log"
 
# print(ROOT_FOLDER)
# list = os.listdir(ROOT_FOLDER) # shows the contents of a folder
def log(username, search_term, matches):
    user_log_file = os.path.join(LOG_FOLDER, username)
    try: 
        os.mkdir(user_log_file)
    except FileExistsError:
        pass
    file_name = f"{uuid.uuid4()}.txt"
    
    # /src/data/log/shaban/ljljasf.xt
    with open(os.path.join(user_log_file, file_name), 'w') as logger:
        # over-ridden version of print
        print("Search term:", search_term, end=".\n", file=logger)
        print("Matches:", end=" ", file=logger)
        print(*matches, sep=", ", end=".\n", file=logger)
 
 
 
def do_search(username, search_term):
    matches = []
    for file in os.listdir(ARTICLE_FOLDER):
        # print(file)#
        # how do we open the file?
        # file_path = ARTICLE_FOLDER + "/" + file
        file_path = os.path.join(ARTICLE_FOLDER, file)
        with open(file_path) as f:
            content = f.read().lower()
            if search_term.lower() in content:
                matches.append(file)
            # find the search_term in content
    if matches:
        print(f"** Found {len(matches)} matching articles: **")
        print(*matches, sep="\n\t")
        # print(matches)
        # for match in matches:
        #     print(f"\t{match}")
    else:
        print("No match was found.")
    # after printing the result, the script will log the query
    # TODO: "logging" 
    """
    It will add a new file in that directory. The name of the file will be random (use uuid.uuid4() to generate file names) and the content will include: 1. A first line with a label Search term: and the user input. 1. A second line with the label Matches: and the name of the matching files found, in a single line, separated by commas and with a final dot ., and without the extension.
 
 
    search term: web 
    Matches: Aws , orientation, etc. (.txt)
    """
    log(username, search_term, matches)
    repeat = input("Would you like to search for something else? (Y/N) or (Yes/No)")
    if repeat.lower() in ['y', 'yes']:
        print('*' * 100)
        do_search(username, input("What word would you like to search for? "))
 
 
 
# when you want the code to run 
if __name__ == '__main__':
    # ask user for name
    username = input("What is your name?")
    # if username.strip() == "":
    if not username.strip():        
        print("Please, provide a name")
        # code should quit here
        sys.exit(1)
    print(f"Welcome {username}!")
 
    search_term = input("What word would you like to search for? ")
    if not search_term.strip():
        print("Please, provide a search term")
        sys.exit(1)
    
    #TODO: Do a search
    # write code procedurely or call a function
    do_search(username, search_term)