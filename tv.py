"""t's time to make a TV party! You invited your friends over on a Saturday night to watch some movies on Netflix. The popcorn is ready, so let's set the TV to work!

The TV class is already created for you and will have regular TV operations such as Turn On, Turn Off, Volume Up, Volume Down, Channel Up, Channel Down, Set Channel and Set Volume.

These operations are defined in the TV class, and therefore, are common operations to any TV. But knowing what a TV does doesn't mean you have a TV, and that's why you need to have an instance object of the TV class.

Overview of tv.py:
Initialize the channel variable and set it to 1;
Initialize the volume_level variable and set it to 1;
Set the turned_on variable to False so that the TV is in the default off position;
turn_on() method should turn the TV on;
turn_off() method should turn the TV off;
channel_up() should increment the channel by 1. Note that the TV must be on;
channel_down() should decrement the channel by 1. Note that the TV must be on;
set_channel() method to set the TV to a specific channel. Note that the TV must be on;
volume_up() should increment the volume by 1. Note that the TV must be on;
volume_down() should decrement the volume by 1. Note that the TV must be on;
The channel's range should be between 1 and 100. The methods channel_up(), channel_down() and set_channel() should take this range into account;
The volume's range should be between 1 and 10. The methods volume_up() and volume_down() should take this range into account."""

# Solution Overview of tv.py

class TV:
    def __init__(self):
        self.channel = 1
        self.volume_level = 1
        self.turned_on = False

    def turn_on(self):
        # turn_on() method should turn the TV on
        self.turned_on = True

    def turn_off(self):
        # turn_off() method should turn the TV off
        self.turned_on = False

    def channel_up(self):
        if self.turned_on:
            # channel_up() should increment the channel by 1. Note that the TV must be on
            self.channel = min(self.channel + 1, 100)  # Ensure the channel remains within the range 1-100

    def channel_down(self):
        if self.turned_on:
            # channel_down() should decrement the channel by 1. Note that the TV must be on
            self.channel = max(self.channel - 1, 1)  # Ensure the channel remains within the range 1-100

    def set_channel(self, channel):
        if self.turned_on:
            # set_channel() method to set the TV to a specific channel. Note that the TV must be on
            self.channel = max(1, min(channel, 100))  # Ensure the channel remains within the range 1-100

    def volume_up(self):
        if self.turned_on:
            # volume_up() should increment the volume by 1. Note that the TV must be on
            self.volume_level = min(self.volume_level + 1, 10)  # Ensure the volume_level remains within the range 1-10

    def volume_down(self):
        if self.turned_on:
            # volume_down() should decrement the volume by 1. Note that the TV must be on
            self.volume_level = max(self.volume_level - 1, 1)  # Ensure the volume_level remains within the range 1-10

################################################################

