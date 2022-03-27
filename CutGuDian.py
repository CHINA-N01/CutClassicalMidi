import os
# import midi
import mido

save_path='cut\\'

path = 'data\\'
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

       # print('track{}:{} \nlen:{}'.format(i, track.name, len(track)))
        for note in track:
            tt = mido.tick2second(note.time, mid.ticks_per_beat, 500000)
            ftime += tt
            t.append(note)
            if ftime >= maxtime:
                mid.save(save_path+"{}_part_{}.mid".format(file, fnum))

                mid = mido.MidiFile()
                mid.ticks_per_beat = f.ticks_per_beat
                t = mido.MidiTrack()
                mid.tracks.append(t)

                for msg in f.tracks[0]:
                    t.append(msg)
                ftime -= maxtime
                fnum += 1
                if fnum > maxFileLen:
                    exit(1)

    print('\nmid:')
    print(fnum)
    print('\nfile:{}'.format(file))
    j = 0
    mid.save(save_path+"/{}_part_{}.mid".format(file, fnum))


