import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt

musikk_fil = "/Users/malinberg/Downloads/scherzo nr 2 - malin klipp.mp3"
data, samplerate = sf.read(musikk_fil)

sek = 20
antall_sample = int(samplerate*sek)
segmenter = data[:antall_sample]

fourier = np.fft.fft(segmenter)
frekvens = np.fft.fftfreq(len(segmenter), d=1/samplerate)

positive_freqs = frekvens[:len(frekvens)//2]
positive_magnitude = np.abs(fourier)[:len(fourier)//2]

plt.plot(positive_freqs, positive_magnitude)
plt.title("Frekvensspekter (første 20 sek)")
plt.xlabel("Frekvens (Hz)")
plt.ylabel("Amplitude")
plt.xlim(0, 5000)
plt.show()

