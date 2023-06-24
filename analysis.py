import numpy as np
import matplotlib.pyplot as plt

def generate_sinusoidal_signal(amplitude, frequency, duration, sampling_rate):
    t = np.arange(0, duration, 1/sampling_rate)
    signal = amplitude * np.sin(2 * np.pi * frequency * t)
    return t, signal

def generate_combined_signal(offset_time, amplitude, frequency, duration, sampling_rate):
    t = np.arange(0, duration, 1/sampling_rate)
    signal2 = amplitude* np.sin(2 * np.pi * frequency * (t + offset_time))
    combined_signal = signal1 + signal2
    return t, combined_signal

def generate_shifted_frequency_signal(offset_frequency, offset_time, amplitude, frequency, duration, sampling_rate):
    t = np.arange(0, duration, 1/sampling_rate)
    signal2 = amplitude * np.sin(2 * np.pi * (frequency + offset_frequency) * (t - offset_time))
    combined_signal = signal1 + signal2
    return t, combined_signal

# Parametry sygnałów
amplitude = 1.0
frequency = 4.02
offset_time = 0.24
offset_frequency = 0.42

# Ustawienia czasu i próbkowania
duration = 1.0
sampling_rate = 1000

# Generowanie sygnałów
t1, signal1 = generate_sinusoidal_signal(amplitude, frequency, duration, sampling_rate)
t2, signal2 = generate_combined_signal(offset_time, amplitude, frequency, duration, sampling_rate)
t3, signal3 = generate_shifted_frequency_signal(offset_frequency, offset_time, amplitude, frequency, duration, sampling_rate)

# Wyświetlanie sygnałów w dziedzinie czasu
plt.figure(figsize=(16, 8))

plt.subplot(3, 2, 1)
plt.plot(t1, signal1)
plt.title('Sinusoidal Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(3, 2, 3)
plt.plot(t1, signal1)
plt.plot(t2, signal2)
plt.title('Combined Signals with Time Offset')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(3, 2, 5)
plt.plot(t1, signal1)
plt.plot(t3, signal3)
plt.title('Combined Signals with Frequency and Time Offset')
plt.xlabel('Time')
plt.ylabel('Amplitude')

# Wyświetlanie sygnałów w dziedzinie częstotliwości
plt.subplot(3, 2, 2)
plt.magnitude_spectrum(signal1, Fs=sampling_rate)
plt.title('Frequency Spectrum - Sinusoidal Signal')

plt.subplot(3, 2, 4)
plt.magnitude_spectrum(signal1, Fs=sampling_rate)
plt.magnitude_spectrum(signal2, Fs=sampling_rate)
plt.title('Frequency Spectrum - Combined Signals with Time Offset')

plt.subplot(3, 2, 6)
plt.magnitude_spectrum(signal1, Fs=sampling_rate)
plt.magnitude_spectrum(signal3, Fs=sampling_rate)
plt.title('Frequency Spectrum - Combined Signals with Frequency and Time Offset')

plt.tight_layout()
plt.show()
