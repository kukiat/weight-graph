import soundfile as sf
import sounddevice as sd

arr = ["care", "soundnaja"]
for i in range(len(arr)):
  sample, late = sf.read(arr[i] + ".wav")
  sd.play(sample, late)
  sd.wait()

arr = []
print 'success'