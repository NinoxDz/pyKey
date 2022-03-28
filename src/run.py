from threading import Thread, Event

from main import main
API_KEYS = [
    'F92Z14GE2DTF6PBBYY1YPHPJ438PT3P2VI',
    'H6MN1IRWW86BWYNEQCYSIEAUIY5BP9VBQ6', #'M6H2AHFNM71I79KJWUSVXB72UR44MWUCV3', 'VM4Z83S7Z52UTR7GXXRFWS6P8D15A6STKS',
    'W3ZENV1S93Z85WVJRCAKTNWB81DM8TF8CK', #'KS6W9J7IUSJ1MJKKXCB5QXXUN87JA1BBP2', '1RDVZM2GP1XEJFU59XG7B3UJ8SFH6NPKRH',
    'RU7XKR2Y8PBJXHREJIRQGD3DTNSJ53RJKT', #'8SNW24W6D39IH3NRS37M3WP93EBA1BBPYP', 'GFW7UVN7NXMB7ZMUTMUX5MRK4FKD6BKXCI'
]
if __name__ == "__main__":
    stop_threads_event = Event()
    i = 0

    while i < len(API_KEYS):
        try:
            Thread(target=main, args=(API_KEYS[i],)).start()
            i+=1
        except Exception as e:
            print("Exception while in the tread")

