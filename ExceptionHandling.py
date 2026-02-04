try:
    x = int("abc")
except ValueError:
    print("Caught a ValueError: invalid literal for int()")