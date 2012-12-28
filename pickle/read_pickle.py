#encoding: shift-jis

import pickle
from Event import *

def main():
    with open('event.pickle', 'rb') as f:
        event = pickle.load(f)
    print event
    print dir(event)
    print event._setting


if __name__ == '__main__':
    main()
