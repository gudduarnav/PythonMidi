# PythonMidi  
 Play custom MIDI tone using Python    
  
  
```python
from pymidi.winmidi import Midi
from pymidi.values import Keys, Instruments


m =Midi()

chord1 = [Keys.C5, Keys.E5, Keys.G5]
chord2 = [Keys.E4, Keys.G4, Keys.C5]
chord3 = [Keys.G4, Keys.C5, Keys.E5]

m.ChangeInstrument(instrument=Instruments.ElectricGrandPiano, channel=1)
m.ChangeInstrument(instrument=Instruments.AcousticGrandPiano, channel=2)

m.ChordOn(keys=chord1, channel=2)
m.PlayNote(pitch=Keys.C5, channel=1)
m.ChordOff(keys=chord1, channel=2)

m.ChordOn(keys=chord2, channel=2)
m.PlayNote(pitch=Keys.D5, channel=1)
m.ChordOff(keys=chord2, channel=2)
```