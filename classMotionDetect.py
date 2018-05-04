import urllib.request as urllib2
import json, numpy as np
from decimal import Decimal
from time import sleep

class MotionDetect():
    def __init__(self, data, how_many_tries=3, interval=1):
        self.data = data
        self.how_many_tries = how_many_tries
        self.interval = interval


    def isMotionDetect(self):

        #ile_ostatnich_pomiarow = 40
        dane_obrobione = []
        min_final_move = 800
        max_final_move = 3000
        treshold_weight = 1
        drift_weight = 10

        for y in range(0, self.how_many_tries):
            number_of_elements = len(self.data[y][u'motion'][u'data'])


            for x in range(0, number_of_elements):
                dane_obrobione.append(float(str(self.data[y][u'motion'][u'data'][x][1]).replace('[', '').replace(']', '')))

        print("Dane: ", dane_obrobione)
        ile_danych_obrobionych = len(dane_obrobione)
        srednia = np.mean(dane_obrobione);

        diff = 0
        for licznik in range(1, int(ile_danych_obrobionych / 2)):
            diff = diff + abs(
                dane_obrobione[ile_danych_obrobionych - licznik] - dane_obrobione[0 + licznik])  # WYLICZANIE DRIFT
        diff = abs(diff) / ile_danych_obrobionych
        if (diff == 0): diff = 0.1

        summary = (srednia * treshold_weight + diff * drift_weight) / treshold_weight + drift_weight

        if ((summary > min_final_move) and (summary < max_final_move)):
            print("Motion detected: 1")
            return True
        else:
            print("Motion detected: 0")
            return False