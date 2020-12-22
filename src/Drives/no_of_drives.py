from ctypes import windll
import string
def no_of_drives():
    drive = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drive.append(letter)
        bitmask >>= 1
    return drive

