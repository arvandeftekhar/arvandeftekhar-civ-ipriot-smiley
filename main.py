""""Demonstrates the use of the Smiley class and its subclasses.
If you have access to a SenseHAT (either via a Raspberry Pi or a SenseHAT emulator), you can use the real SenseHAT class instead of the mock SenseHAT class.
That is, delete the sense_hat.py file that is included in this bundle.
"""

import time
from happy import Happy
from sad import Sad

if __name__ == '__main__':
    # Displaying the Happy Smiley (Yellow)
    happy_smiley = Happy()
    print("Displaying Happy Smiley (Yellow):")
    happy_smiley.show()
    time.sleep(1)
    
    # Making the Happy Smiley Blink
    print("Making Happy Smiley Blink:")
    happy_smiley.blink(delay=0.5)
    time.sleep(1)

    # Displaying the Sad Smiley (Blue)
    sad_smiley = Sad()
    print("Displaying Sad Smiley (Blue):")
    sad_smiley.show()
    time.sleep(1)
    
    # Making the Sad Smiley Blink
    print("Making Sad Smiley Blink:")
    sad_smiley.blink(delay=0.5)
    time.sleep(1)

    # Demonstrating polymorphism with the show method
    smiley = Happy()
    smiley.show()
    time.sleep(1)
    
    # Demonstrating polymorphism with the blink method
    smiley.blink(delay=0.5)
