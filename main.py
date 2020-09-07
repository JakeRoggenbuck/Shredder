import argparse
import requests


api_url = "http://swquotesapi.digitaljedi.dk/api/SWQuote/RandomStarWarsQuote"
request = requests.get(api_url)
quote = request.json()['starWarsQuote']


def get_file_size(filename: str) -> int:
    with open(filename, 'rb') as file:
        data = file.read()
        file.close()
        file_length = len(data)
        return file_length


def overwite_file(file_length: int, filename: str, letters: str):
    with open(filename, 'w') as file:
        letter = 0
        for num in range(file_length):
            if letter == 4:
                letter = 0
            file.seek(num)
            file.write(letters[letter])
            letter += 1


def parse() -> list:
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", type=str, help="Set file")
    parser.add_argument("-s", help="Star Wars quote", action='store_true')
    args = parser.parse_args()
    return args


def star_wars_quote():
    url = "http://swquotesapi.digitaljedi.dk/api/SWQuote/RandomStarWarsQuote"
    request = requests.get(url)
    quote = request.json()['starWarsQuote']
    return quote


if __name__ == "__main__":
    arguments = parse()
    if arguments.s:
        letters = star_wars_quote()
    else:
        letters = "fred"
    if arguments.f is not None:
        file_size = get_file_size(arguments.f)
        overwite_file(file_size, arguments.f, letters)
    else:
        print("Use -f filename.txt to specify filename")
