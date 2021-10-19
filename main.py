

from rando import Randomizer
from controller import Controller
#from synthesizer import Synth
import time



def main():
    synth = Controller()
    synth.testSequence(20)
    synth.loop()

    r = Randomizer()
    r.permute('', 2)
    r.prettyPrint();



main()
