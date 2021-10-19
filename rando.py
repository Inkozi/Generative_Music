
import random 


'''
    Class: Randomizer
    Description:
        Produces random sequences from permutation
        or just randomly producing a string of notes
'''
class Randomizer():

    def __init__(self):
        self.length = 32
        self.octaveMin = 1
        self.octaveMax = 8
        self.octaves = range(self.octaveMin, self.octaveMax)
        self.allBars = []
        self.notes = ['c', 'c#', 'd', 'd#', 'e','f', 'f#', 'g', 'g#', 'a', 'a#', 'b']


    def printNotes(self):
        print(self.notes)

    def printAllBars(self):
        print(self.allBars)

    def prettyPrint(self):
        for note in self.allBars:
            print(note)

    def changeLength(self, length):
        self.length = length


    def resetBars(self):
        self.allBars = []


    def pure(self):
        for note in range(self.length):
            note = self.notes[randrange(len(self.notes))]
            octave = self.octaves[randrange(len(self.octaves))]
            self.notes.append(note + str(octave))

    def permute(self, prefix, k):
        n = len(self.notes)
        #base case    
        if (k == 0):
            self.allBars.append(prefix)
            return

        #creates tree
        for i in range(n):
            newPrefix = prefix + str(self.octaves[random.randrange(0, len(self.octaves))]) + self.notes[i] + ' '
            self.permute(newPrefix, k-1)


'''
    def random(self, length):
        tempSection = []
        if (len(self.allBars) == 0):
            for (bar in range(length)):
                tempSection.append(self.allBars(randrange(0,len(allBars))))
        return tempSection
'''
