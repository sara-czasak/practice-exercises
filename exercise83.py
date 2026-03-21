import screeninfo

info = screeninfo.get_monitors()[0]
print(f"Width: {info.width}, Height: {info.height}")