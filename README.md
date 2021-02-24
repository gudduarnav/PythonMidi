# PythonMidi  
 Play custom MIDI tone using Python    
  
  
```python
from pymidi.winmidi import Midi
from pymidi.values import Keys, Instruments

m =Midi()

chord1 = [Keys.C5, Keys.E5, Keys.G5]
chord2 = [Keys.E4, Keys.G4, Keys.C5]

m.ChangeInstrument(instrument=Instruments.ElectricGrandPiano, channel=1)
m.ChangeInstrument(instrument=Instruments.AcousticGrandPiano, channel=2)

m.ChordOn(keys=chord1, channel=2)
m.PlayNote(pitch=Keys.C5, channel=1)
m.ChordOff(keys=chord1, channel=2)

m.ChordOn(keys=chord2, channel=2)
m.PlayNote(pitch=Keys.D5, channel=1)
m.ChordOff(keys=chord2, channel=2)
```  
  
Line 1 and 2 imports the modules and enums required.  
Line 4 create the MIDI object.  
Line 6, 7 creats 2 chords with respective pitch (from Cmajor scale).  
Line 9, 10 associates 2 different musical instruments for 2 channels.  
Chord will be played on channel-2 and Keys on channel-1.  
  
Line-12, 16 will play the chord and Line-14, 18 will turn the respective chords off.  
Line-13, 17 will play the given key on key-channel for 1 seconds by default.  
  
  
## Developed by:
** 1. Arnav Mukhopadhyay**  
** 2. Ruby Jane Pedronan Agullana**  
  
#midi #python #computermusic #instrumental #programming  
