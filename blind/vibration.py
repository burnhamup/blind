import ctypes

class XinputVibration(object):
    xinput = ctypes.windll.xinput1_1
    class XINPUT_VIBRATION_STRUCT(ctypes.Structure):
        _fields_ = [("wLeftMotorSpeed", ctypes.c_ushort),
                ("wRightMotorSpeed", ctypes.c_ushort)]

    def __init__(self):
        self.setState = self.xinput.XInputSetState
        self.setState.argtypes = [ctypes.c_uint, ctypes.POINTER(self.XINPUT_VIBRATION_STRUCT)]
        self.setState.restype = ctypes.c_uint
        self.timer = 0

    def vibrate(self, amount, time):
        vibration_amount = self.XINPUT_VIBRATION_STRUCT(int(amount * 65535), int(amount * 65535))
        self.setState(0, vibration_amount)
        self.timer = time

    def update(self):
        self.timer -= 1
        if self.timer < 0:
            self.vibrate(0, 0)

    def draw(self):
        pass
