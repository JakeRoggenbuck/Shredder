import argparse
import requests


def get_file_size(filename: str) -> int:
    """Gets file size in bytes"""
    with open(filename, 'rb') as file:
        data = file.read()
        file_length = len(data)
        return file_length


def overwite_file(file_length: int, filename: str, letters: str):
    """Overwrites each byte with a letter from letters"""
    with open(filename, 'w') as file:
        letter = 0
        for num in range(file_length):
            # If the string is at the end, reset index
            if letter == len(letters):
                letter = 0
            # Find the location in the file
            file.seek(num)
            # Write the letter to the location
            file.write(letters[letter])
            letter += 1


def parse() -> list:
    """Gets arg parameters"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", type=str, help="Set file")
    parser.add_argument("-s", help="Star Wars quote", action='store_true')
    args = parser.parse_args()
    return args


def star_wars_quote():
    """Sends a request to star wars api and gets a quote"""
    url = "http://swquotesapi.digitaljedi.dk/api/SWQuote/RandomStarWarsQuote"
    request = requests.get(url)
    quote = request.json()['starWarsQuote']
    return quote


if __name__ == "__main__":
    # Runs parse on args
    arguments = parse()
    # Check for arg param s (star wars)
    if arguments.s:
        letters = star_wars_quote()
    else:
        letters = "fred"
    # Check for filename
    if arguments.f is not None:
        file_size = get_file_size(arguments.f)
        overwite_file(file_size, arguments.f, letters)
    else:
        print("Use -f filename.txt to specify filename")
