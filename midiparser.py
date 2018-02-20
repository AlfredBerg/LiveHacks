from mido import MidiFile

mid = MidiFile('\\Users\\Administrator\\Downloads\\We_Will_Rock_You.MID')

array = []
for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    
    for msg in track:
        print(msg)