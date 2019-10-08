import random
import threading
import time



class RNG:
    def __init__(self):
        self.number = -1
        thrd = threading.Thread(target=self._update)
        thrd.daemon = True
        thrd.start()
    
    def _update(self):
        while True:
            number = random.randint(0,100)
            if number == 69:
                number = 'nice'
            self.number = number
            time.sleep(1)

class RNGS:
    def __init__(self,number=0):
        self.gens = []
        if number != 0:
            self.init_gens(number)
    
    def init_gens(self,number):
        for _ in range(number):
            rng = RNG()
            self.gens.append(rng)
