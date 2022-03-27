import os
# import midi
import mido

save_path='cut_pop\\'

metad=[]
new_tempo=500000
path = 'data_pop\\'
files = os.listdir(path)
for file in files:
    f = mido.MidiFile(path+file)
    fnum = 0
    ftime = 0
    maxtime = 30
    maxFileLen=120
    mid = mido.MidiFile()
    t = mido.MidiTrack()
    mid.tracks.append(t)
    # print f
    j = 0
    mid.ticks_per_beat = f.ticks_per_beat
    for i, track in enumerate(f.tracks):

        print('track{}:{} \nlen:{}'.format(i, track.name, len(track)))
        for note in track:
            dnote=note.dict()
            if dnote['type']=='set_tempo':
                print(note)
            j+=1
            if j>=20:
                break

    print('\nmid:')
    print(fnum)
    print('\nfile:{}'.format(file))
    j = 0
    mid.save(save_path+"/{}_part_{}.mid".format(file, fnum))


