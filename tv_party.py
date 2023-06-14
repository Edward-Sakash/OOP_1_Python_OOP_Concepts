"""Overview of tv_party.py:
Create an instance object of the TV class;
Part 1:
Turn the TV on;
Set the channel to 3;
Set the volume to 7;
Set the TV off for food break;
Part 2:
Turn the TV on;
Set the channel to 95;
Set the volume to 5;"""

# Solution

from tv import TV

# Create an instance object of the TV class
tv = TV()

# Part 1:
# Turn the TV on
tv.turn_on()

# Set the channel to 3
tv.set_channel(3)

# Set the volume to 7
tv.volume_level = 7

# Set the TV off for a food break
tv.turn_off()

# Part 2:
# Turn the TV on
tv.turn_on()

# Set the channel to 95
tv.set_channel(95)

# Set the volume to 5
tv.volume_level = 5

#################################################################
from tv import TV

# Create an instance object of the TV class
tv = TV()

# Part 1:
print("Turning the TV on")
tv.turn_on()

print("Setting the channel to 3")
tv.set_channel(3)

print("Setting the volume to 7")
tv.volume_level = 7

print("Turning the TV off for a food break")
tv.turn_off()

# Part 2:
print("Turning the TV on")
tv.turn_on()

print("Setting the channel to 95")
tv.set_channel(95)

print("Setting the volume to 5")
tv.volume_level = 5
