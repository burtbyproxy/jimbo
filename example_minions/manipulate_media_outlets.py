import media_outlets

def manipulate_outlets():
    outlets = media_outlets.get_outlets()
    manipulated_outlets = [outlet.upper() for outlet in outlets]
    return manipulated_outlets

manipulated_outlets = manipulate_outlets()
print(manipulated_outlets)