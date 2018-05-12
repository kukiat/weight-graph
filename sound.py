import soundfile as sf
import sounddevice as sd

# arr = ["sofa", "120", "metre"]
# for i in range(len(arr)):
#   data = "sound/"+ str(arr[0]) +".wav"
#   sample, late = sf.read(data)
#   sd.play(sample, late)
#   sd.wait()
data1 = "sound/sofa.wav"
data2 = "sound/18.wav"
data3 = "sound/point.wav"
data4 = "sound/15.wav"
data5 = "sound/metre.wav"
sample, late = sf.read(data1)
sample2, late2 = sf.read(data2)
sample3, late3 = sf.read(data3)
sample4, late4 = sf.read(data4)
sample5, late5 = sf.read(data5)
sd.play(sample, late)
sd.wait()
sd.play(sample2, late2)
sd.wait()
sd.play(sample3, late3)
sd.wait()
sd.play(sample4, late4) 
sd.wait()
sd.play(sample5, late5)
sd.wait()

print 'success'

#  distance < 50 && !class = ["ระวังสิ่งกีดขวาง ภายใน 50 เซน"] --> 2
#  distance > 50-300 && class = ["ระวังโซฟา 1.5 เมตร"] --> 225
#  distance > 300 && class = ["ระวังโซฟาด้านหน้า"] --> 9 