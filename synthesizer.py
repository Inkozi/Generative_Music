import pyaudio
import sounddevice as sd
import numpy as np
import time


class Frame():
    def __init__(self, audio):
        self.frame = 0
        self.data = audio

    def updateAudio(self, audio):
        self.data = audio

    def readFrames(self, n):
        ret = self.data[self.frame:self.frame + n]
        self.frame = self.frame + n
        return bytes(ret)

class Synth():
    def __init__(self):
        self.audio = np.empty(2)
        self.bitrate = 96000
        self.framerate = 44100
        self.numChannels = 1
        self.sampwidth = 1
        self.duration = 0.1
        self.frequency = 440
        self.s = pyaudio.PyAudio()
        self.stream = ''
        self.f = Frame(self.audio)

    def generate(self):
        points = int(self.bitrate * self.duration)
        times = np.linspace(0, self.duration, points, endpoint=False) 
        self.audio = np.array((np.sin(times*self.frequency*2*np.pi) + 1.0)*127.5, dtype=np.int8).tostring()
        self.f.data = self.audio

    def updateFreq(self, freq):
        self.frequency = freq

    def callback(self, in_data, frame_count, time_info, status):
        data = self.f.readFrames(frame_count)
        print(frame_count)
        return (data, pyaudio.paContinue)

    def openStream(self):
        self.stream = self.s.open(format=self.s.get_format_from_width(self.sampwidth),
            channels=self.numChannels,
            rate=self.framerate,
            output=True,
            stream_callback=self.callback)
    
    def start(self):
        self.stream.start_stream()
        print("started-stream")

    def active(self):
        return self.stream.is_active()

    def end(self):
        self.stream.stop_stream()
        self.stream.close()
        print("stream closed")

    def terminate(self):
        self.s.terminate()

    def play(self):
        self.generate()
        self.openStream()
        self.start()
        while (self.active()):
            time.sleep(0.1)
        self.end()

