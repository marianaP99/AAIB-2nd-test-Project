import sounddevice as sd
import pandas as pd
import matplotlib.pyplot as plt
import tsfel

duration = 3  # seconds
fs = 44100
sd.default.samplerate = fs
sd.default.channels = 2

def record():
    myrecording = sd.rec(int(duration * fs))
    sd.wait()
    t = [n/fs for n in range(duration*fs)]
    sound = [myrecording[n][0] for n in range(duration * fs)]
    
    cfg = tsfel.get_features_by_domain()
    s_tsfel = tsfel.time_series_features_extractor(cfg, sound, fs=fs)
    
    sonogram = '\n'.join([','.join([str(t[n]),str(sound[n])]) for n in range(len(t))])
    features = ','.join(s_tsfel.columns) + '\n' + ','.join([str(n) for n in s_tsfel.loc[0] ])

    message = sonogram + '||' + features 
    return message

def save_file(message):
    sound_f = open("sonograme.csv", "w")
    sound_f.write('\n'.join([','.join([str(t[n]),str(sound[n])]) for n in range(len(t))]))

    feat_f = open("features.csv", "w")
    feat_f.write(','.join(s_tsfel))