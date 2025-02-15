# main.py
from interactive_cli import InteractiveCli
from response_handler import PrintResponse

def main():
    print("Vítejte v interaktivním režimu:")
    print("--------------------------------")
    while True:
        InteractiveCli().run()
        if PrintResponse.response:
            PrintResponse.print_response()
        else:
            print("Ukončuji interaktivní režim...")
            break

if __name__ == "__main__":
    main()