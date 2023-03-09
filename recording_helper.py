#from readline import set_completer
import pyaudio
import numpy as np


FRMAES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
p = pyaudio.PyAudio()

def record_audio():
    stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=FRMAES_PER_BUFFER
    )

    print("start recording")

    frames = []
    second=1
    for i in range(0, int(RATE / FRMAES_PER_BUFFER * second)):
        data = stream.read(FRMAES_PER_BUFFER)
        frames.append(data)

    # print("recording stopped")

    stream.stop_stream()
    stream.close()
    
    return np.frombuffer(b"".join(frames), dtype=np.int16)

def terminate():
    p.terminate()
    
