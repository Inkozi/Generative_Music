


'''
    This program is intended to be a song writing editor 
    for my mother 32s.

    Ryhthm unfortunately is not analyzed in this script because
    the hardware to play the sequences doesn't have a lot of rhthym control.
    (This is one of the largest restrictions on mother32 modular systems)

    This program will look at other methods to analyze and generate sounds via colorful classifications.
    varying alignments, note proximity factors, repeated notes, and various keys/signatures.


        1) Analyzes sequences for melodious and harmonic sequences.
            + Parses file of notes
            + returns intervals
            + checks for consance and dissonance in melodious and harmonic schemes
                +I could also add a bayesian classification to classify melodious and harmonic tunes.
            +These can come from songs, be parts of songs or things that I write.

        2) Sequences generation.
            +generate triades and streams of sequences that follow rules for melodious and harmonic structure
            +eventually the music can be large vectors comparing multiples, harmonic and melodious sequences.
            +Possible augmentations can possible be down in a time dimension but that'll be fore later

'''


notes = ['C','D','E','F','G','A','B']
semitones = {'flat' : 'b', 'sharp' : '#'}


#Row = Chromatic Interval
#Column = Generic Interval
'''
    reference:
       http://openmusictheory.com/intervals.html

Row = Chromatic Interval
Column = Generic Interval

'''
intervalType = [
        ['P1','d2',0,0,0,0,0,0]
        ['A1','m2',0,0,0,0,0,0]
        [0,'M2','d3',0,0,0,0,0]
        [0,'A2','m3',0,0,0,0,0]
        [0,0,'M3','d4',0,0,0,0]
        [0,0,'A3','P4',0,0,0,0]
        [0,0,0,'A4','d5',0,0,0]
        [0,0,0,0,'P5','d6',0,0]
        [0,0,0,0,'A5','m6',0,0]
        [0,0,0,0,0,'M6','d7',0]
        [0,0,0,0,0,'A6','m7',0]
        [0,0,0,0,0,0,'M7','d8']
        [0,0,0,0,0,0,'A7','P8']]

verses = {"melody" : [], "harmony": []}
intervals = {"melody" : [], "harmony": []}


'''
    Calculate Intervals
'''
def calcIntervals():

    for note in range(len(verse["melody"])):
        if (note < len(verse["melody"]) - 1):
            currNote = verse["melody"][note]
            nextNote = verse["melody"][note+1]
            chromInterval, genInterval = dist(currNote, nextNote)
            chromInterval = exception(chromInterval)
            intervals["melody"].append(intervalType[chromInterval][genInterval])
    
    for note in range(len(verse["harmony"])):
        if (note < len(verse["harmony"]) - 1):
            currNote = verse["harmony"][note]
            nextNote = verse["harmony"][note+1]
            chromInterval, genInterval = dist(currNote, nextNote)
            chromInterval = exception(chromInterval)
            intervals["harmony"].append(intervalType[chromInterval][genInterval])

def exception(chromInterval):
    result = chromInterval
    if (note != 'E' and semitone != '#' or note != 'F' and semitone != 'b'):
        if (semitone == '#'):
            result += 1
        elif (semitone == 'b'):
            result -= 1
    return result

'''
    File parsing routine
'''
def parse(fn):
    f = open(fn, 'r')
    populate(f) #melody
    populate(f) #harmony
    f.close()


def populate(f):
    verse = prologue(f)
    verse.lower()
    while (line != "END"):
        line = f.readline()
        line = line[:-1]
        line.split()
        for note in line:
            verses[verse].append(note)

def prologue(f):
    line = ""
    while (line != "MELODY" or line != "HARMONY"):
        line = f.readline()
        line = line[:-1]
    return line

'''
'''




#TODO args
def main():
    pass
