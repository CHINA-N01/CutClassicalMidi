import os
import sys
# import midi
import mido
new_tempo=500000
save_path='cut_yanni\\'
metad=[]
path = 'data_yanni\\'
sum=0
fnum=0
if not os.path.exists(save_path.rstrip('\\')):
    save_path = save_path.strip()
    os.makedirs(save_path)
    print(path + ' 创建成功')
files = os.listdir(path)
for file in files:
    sum+=fnum
    tempoEvent = []
    metad = []
    f = mido.MidiFile(path+file)
    fnum = 0
    ftime = 0
    maxtime = 60
    maxFileLen=120
    mid = mido.MidiFile()
    t = mido.MidiTrack()
    mid.tracks.append(t)
    # print f
    j = 0
    mid.ticks_per_beat = f.ticks_per_beat
    for i, track in enumerate(f.tracks):
        #(f)
        #exit(0)

       # print('track{}:{} \nlen:{}'.format(i, track.name, len(track)))
        for note in track:

            if note.is_meta==True:
                dnote = note.dict()
                if dnote['type'] == 'set_tempo':
                    t.append(note)
                    tempoEvent = note
                if dnote['type'] == 'time_signature' or dnote['type'] == 'key_signature':
                    t.append(note)
                    metad.append(note)
                if dnote['type'] == 'set_tempo':
                    new_tempo = dnote['tempo']
                    print(new_tempo)

            tt = mido.tick2second(note.time, mid.ticks_per_beat, new_tempo)
            ftime += tt
            t.append(note)




            if ftime >= maxtime:

                mid.save(save_path+"{}_part_{}.mid".format(file, fnum))

                mid = mido.MidiFile()
                mid.ticks_per_beat = f.ticks_per_beat
                t = mido.MidiTrack()
                mid.tracks.append(t)

                for msg in metad:
                    t.append(msg)
                t.append(tempoEvent)
                ftime -= maxtime
                fnum += 1
                if fnum > maxFileLen:
                    exit(1)

    mid.save(save_path + "{}_part_{}.mid".format(file, fnum))

    mid = mido.MidiFile()
    mid.ticks_per_beat = f.ticks_per_beat
    t = mido.MidiTrack()
    mid.tracks.append(t)

    for msg in metad:
        t.append(msg)
    t.append(tempoEvent)
    ftime -= maxtime
    fnum += 1
    if fnum > maxFileLen:
        exit(1)

    print('midi nums:{}'.format(fnum))
    print('f tick:{},mid tick:{}'.format(f.ticks_per_beat,mid.ticks_per_beat))
    print('file:{}\n'.format(file))

    j = 0
    #mid.save(save_path+"/{}_part_{}.mid".format(file, fnum))


