from ascript.android.system import Device
display = Device.display()
width = display.widthPixels
height = display.heightPixels

def rc1920(x1, y1, x2, y2):
  
    return [
        int(width * (x1 / 1920)),
        int(height * (y1 / 1080)),
        int(width * (x2 / 1920)),
        int(height * (y2 / 1080))
    ]

def rc19202(x1,y1):
    return [
        int(width * (x1 / 1920)),
        int(height * (y1 / 1080))
    ]