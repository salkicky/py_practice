#encoding: shift-jis

import pickle
from Event import *

if __name__ == '__main__':
    event = Event(4)

    with open('event.pickle', 'wb') as f:
        pickle.dump(event, f)
