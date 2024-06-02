from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def adjust_volume(change):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    
    current_volume = volume.GetMasterVolumeLevelScalar()
    
    if change == '1':
        current_volume -= 0.01
    elif change == '2':
        current_volume += 0.01
    
    current_volume = max(0.0, min(current_volume, 1.0))
    
    volume.SetMasterVolumeLevelScalar(current_volume, None)

while True:
    command = input("Enter '1' to decrease volume or '2' to increase volume (or 'q' to quit): ")
    if command == 'q':
        break
    elif command in ['1', '2']:
        adjust_volume(command)
    else:
        print("Invalid command! Please enter '1' or '2'.")

print("Goodbye!")
