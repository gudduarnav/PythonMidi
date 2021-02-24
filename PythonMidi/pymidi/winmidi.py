# https://cmtext.indiana.edu/MIDI/chapter3_channel_voice_messages.php

import platform
import ctypes as ct
from time import sleep
from pymidi.exceptions import ExceptionPlatformNotSupported
from pymidi.exceptions import ExceptionDeviceError

class Midi:
    def __init__(self, deviceID=0):
        if "windows" not in platform.system().lower():
            raise ExceptionPlatformNotSupported

        try:
            self.winmm = ct.windll.winmm
            self.hmidi = ct.c_void_p()
            rc = self.winmm.midiOutOpen(ct.byref(self.hmidi), deviceID, 0, 0, 0)
            if rc != 0:
                raise Exception("MMRESULT during midiOutOpen is {}".format(rc))
        except Exception as ex:
            raise ExceptionDeviceError(msg=str(ex))

    def __del__(self):
        try:
            self.winmm.midiOutClose(self.hmidi)
        except:
            pass

    def Send(self, message):
        try:
            rc = self.winmm.midiOutShortMsg(self.hmidi, ct.c_int(message))
            if rc != 0:
                raise Exception("MMRESULT during midiOutShortMsg is {}".format(rc))
        except Exception as ex:
            raise ExceptionDeviceError(ex)

    def NoteOn(self, pitch, channel=1, volume=80):
        msg = 0x90 + ((pitch)*0x100) + ((volume)*0x10000) + (channel)
        self.Send(msg)

    def NoteOff(self, pitch, channel=1):
        msg = 0x80 + ((pitch)*0x100) + (channel)
        self.Send(msg)

    def PlayNote(self, pitch, duration=1.0, channel=1, volume=80):
        self.NoteOn(pitch, channel, volume)
        sleep(duration)
        self.NoteOff(pitch, channel)

    def ChangeController(self, controller, value, channel=1):
        msg = 0xB0 + ((controller)*0x100) + ((value)*0x10000) + channel
        self.Send(msg)

    def ChangeInstrument(self, instrument, value=0, channel=1):
        msg = 0xC0 + ((instrument)*0x100) + ((value)*0x10000) + channel
        self.Send(msg)

    def ChordOn(self, keys, channel=1, volume=80):
        for key in keys:
            self.NoteOn(pitch=key, channel=channel, volume=volume)

    def ChordOff(self, keys, channel=1):
        for key in keys:
            self.NoteOff(pitch=key, channel=channel)

    def PlayChord(self, keys, duration=0.05, channel=1, volume=80):
        self.ChordOn(keys, channel,volume)
        sleep(duration)
        self.ChordOff(keys, channel)