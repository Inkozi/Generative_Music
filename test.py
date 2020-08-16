




from rando import Randomizer as r
from controller import Controller
from communication import DAC as dac
from synthesizer import Synth

#import pyaudio
#import wave
import time
#import sys
import unittest


class testConstruction(unittest.TestCase):

    def testRandomizer(self):
        x = r()

    def testController(self):
        x = Controller() 
        
    def testComm(self):
        x = dac()

    def testSynth(self):
        x = Synth()

def testSream():
    if len(sys.argv) < 2:
        print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
        sys.exit(-1)

    wf = wave.open(sys.argv[1], 'rb')

    # instantiate PyAudio (1)
    p = pyaudio.PyAudio()

    # define callback (2)
    def callback(in_data, frame_count, time_info, status):
        data = wf.readframes(frame_count)
        #print(data)
        print(in_data)
        print(time_info)
        print(status)
        print(frame_count)
        print(wf.getsampwidth())
        time.sleep(1)
        return (data, pyaudio.paContinue)

    # open stream using callback (3)
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True,
        stream_callback=callback)

    # start the stream (4)
    stream.start_stream()

    # wait for stream to finish (5)
    while stream.is_active():
        time.sleep(0.1)

    # stop stream (6)
    stream.stop_stream()
    stream.close()
    wf.close()

    # close PyAudio (7)
    p.terminate()

'''
    This section will be for testing the randomizer
'''
def testRando():
    x = r()
    x.permute('', 2)
    x.prettyPrint()
    x.permute('', 3)
    x.prettyPrint()




if __name__ == '__main__':

    '''
    print("testing construction of objects")
    time.sleep(2)
    unittest.main()
    '''

    print("testing randomize class")
    time.sleep(2)
    testRando()
