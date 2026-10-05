def convert(text):
    text = text.replace(':)', '🙂')
    text = text.replace(':(', '🙁')
    return text


def main():
    user_input = input('enter what you want to say: ')
    print(convert(user_input))


if __name__ == "__main__":
    main()