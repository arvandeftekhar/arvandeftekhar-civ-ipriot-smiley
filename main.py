import time
from happy import Happy
from sad import Sad

if __name__ == '__main__':
    happy_smiley = Happy()
    print("Displaying Happy Smiley (Yellow):")
    happy_smiley.show()
    time.sleep(1)

    sad_smiley = Sad()
    print("Displaying Sad Smiley (Blue):")
    sad_smiley.show()
    time.sleep(1)

    print("Making Sad Smiley Blink:")
    sad_smiley.blink(delay=0.5)
    time.sleep(1)

    print("Making Happy Smiley Blink:")
    happy_smiley.blink(delay=0.5)
    time.sleep(1)
