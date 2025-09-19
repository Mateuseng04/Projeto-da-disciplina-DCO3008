import wave
import numpy as np

# Audio parameters
sample_rate = 44100  # samples per second
duration = 2       # seconds
frequency = 440    # Hz (A4 note)

# Generate a sine wave
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
amplitude = 0.5 # between 0 and 1
data = amplitude * np.sin(2 * np.pi * frequency * t)

# Convert to 16-bit integers
data_int16 = (data * 32767).astype(np.int16)

# Open a WAV file in write mode
with wave.open("output.wav", "wb") as wf:
    wf.setnchannels(1)  # Mono
    wf.setsampwidth(2)  # 2 bytes per sample (16-bit)
    wf.setframerate(sample_rate)
    wf.writeframes(data_int16.tobytes())

print("WAV file 'output.wav' created successfully.")