
import rtmidi
import pysine
from communication import DAC as d 
from synthesizer import Synth

class Controller():

    def __init__(self):
        self.notesOn = [False]*128
        self.activeNotes = []
        self.midiin = rtmidi.RtMidiIn()
        self.comm = d()
        self.synth = Synth()
        self.packet = {'Name': '', 'Number': 0, 'Active': False, 'Velocity': 0}
        self.test = False
    
    def getActive(self):
        return self.packet['Active']

    def getName(self):
        return self.packet['Name']
    
    def getVelocity(self):
        return self.packet['Velocity']

    def onNote(self):
        if self.packet['Name'] not in self.activeNotes:
            self.activeNotes.append(self.packet['Name'])

    def offNote(self):
        if self.packet['Name'] in self.activeNotes:
            self.activeNotes.remove(self.packet['Name'])

    def print_message(self, midi):
        self.packet['Name'] = midi.getMidiNoteName(midi.getNoteNumber())
        self.packet['Number'] = midi.getNoteNumber()
        self.packet['Velocity'] = midi.getVelocity()
        if midi.isNoteOn():
            self.onNote()
        elif midi.isNoteOff():
            self.offNote()
        elif midi.isController():
            print('CONTROLLER', midi.getControllerNumber(), midi.getControllerValue())
  

    def testSequence(self, length=0):
        self.test = True
        sequence = ['c4', 'e4', 'g4', 'c4', 'e4', 'g4', 
                        'c4', 'e4', 'g4', 'a4', 'c5', 'e5', 
                        'd4', 'f5', 'a4', 'e4', 'c4', 'e4', 
                        'g4', 'c4', 'e4', 'g4', 'c4', 'e4', 
                        'g4', 'a4', 'c5', 'e5', 'd4', 'f5',
                        'a4', 'e4', 'c4', 'e4', 'g4', 'c4', 
                        'e4', 'g4', 'c4', 'e4', 'g4', 'a4', 
                        'c5', 'e5', 'd4', 'f5', 'a4', 'e4', 
                        'c4', 'c4', 'e4', 'g4', 'c4', 'e4', 
                        'g4', 'c4', 'e4', 'g4', 'a4', 'c5', 
                        'e5', 'd4', 'f5', 'a4', 'e4', 'c4', 
                        'e4', 'g4', 'c4', 'e4', 'g4', 'c4', 
                        'e4', 'g4', 'a4', 'c5', 'e5', 'd4', 
                        'f5', 'a4', 'e4', 'c4', 'e4', 'g4', 
                        'c4', 'e4', 'g4', 'c4', 'e4', 'g4', 
                        'a4', 'c5', 'e5', 'd4', 'f5', 'a4', 
                        'e4', 'c4', 'e4', 'g4', 'c4', 'e4', 
                        'g4', 'c4', 'e4', 'g4', 'a4', 'c5', 
                        'e5', 'd4', 'f5', 'a4', 'e4', 'c4', 
                        'e4', 'g4', 'c4', 'e4', 'g4', 'c4', 
                        'e4', 'g4', 'a4', 'c5', 'e5', 'd4', 
                        'f5', 'a4', 'e4', 'c4']
        if (length !=0):
            self.activeNotes = sequence[0:length]
        else:
            self.activeNotes = sequence

    def play(self):
        for note in self.activeNotes:
            print(note)
            temp = note[0] + note[1]
            temp = temp.lower()
            self.synth.updateFreq(self.comm.noteToFreq(temp))
            self.synth.play()

    ''' turn midi data into frequency data for purr data '''
    def noteToFreq(self, note):
        a = (2.0)**(1/12.0)
        freq = self.rootFreq * (a**self.dist(note))
        return freq

    def loop(self):
        if (not self.test):
            ports = range(self.midiin.getPortCount())
            print(ports)
            if ports:
                for i in ports:
                    print("port-name: " + self.midiin.getPortName(i))
                    print("Opening port 0!") 
                    self.midiin.openPort(1)
                while True:
                    m = self.midiin.getMessage(250) # some timeout in ms
                    if m:
                        self.print_message(m)
                        self.play()
            else:
                print('NO MIDI INPUT PORTS!')
        else:
            self.play()
