"""from tv import TV


 # Let's make a TV party!!

class TVParty:

    def __init__(self):
        # TODO: Instantiate the TV object
        tv = None

        # TODO: Your first code goes here

        print(
            "Let's watch the Alien Movie. The TV is currently [" + tv.is_on() + "] and it should be [on]."
            + " It's being shown on channel [3], and we're currently on channel [" + str(tv.channel) + "]. "
            + "Your friend Lisa also would like to have the volume set to [7], and we're currently on volume ["
            + str(tv.volume_level) + "]."
        )

        # TODO: Food break! turn the tv off.

        print("Food break! The TV should be [off], and it's currently [" + tv.is_on() + "].")

        # TODO: Your second code goes here.

        print(
            "Now let's watch the last season of Game of Thrones. The TV is currently [" + tv.is_on()
            + "] and it should be [on]. "
            + "It's being shown on channel [95], and we're currently on channel [" + str(tv.channel) + "]. "
            + "Your friend Gabriel also would like to have the volume set to [5], and we're currently on volume ["
            + str(tv.volume_level) + "]."
        )"""
##########################################################
from tv import TV

class TVParty:
    def __init__(self):
        tv = TV()  # Instantiate the TV object

        # Part 1
        tv.turn_on()  # Turn the TV on
        tv.set_channel(3)  # Set the channel to 3
        for _ in range(7):  # Increase the volume to 7
            tv.volume_up()

        print(
            f"Let's watch the Alien Movie. The TV is currently [ {'off' if  str(tv.turned_on) else 'off'}] and it should be [on]."
            + " It's being shown on channel [3], and we're currently on channel [" + str(tv.channel) + "]. "
            + "Your friend Lisa also would like to have the volume set to [7], and we're currently on volume ["
            + str(tv.volume_level) + "]."
        )

        # Food break! Turn the TV off
        tv.turn_off()

        print(f"Food break! The TV should be [off], and it's currently [ {'on' if str(tv.turned_on) else 'off'}].")

        # Part 2
        tv.turn_on()  # Turn the TV back on
        tv.set_channel(95)  # Set the channel to 95
        tv.volume_down()  # Decrease the volume to 5

        print(
            f"Now let's watch the last season of Game of Thrones. The TV is currently [{'off' if  str(tv.turned_on) else 'on'}] and it should be [on]. "
            + "It's being shown on channel [95], and we're currently on channel [" + str(tv.channel) + "]. "
            + "Your friend Gabriel also would like to have the volume set to [5], and we're currently on volume ["
            + str(tv.volume_level) + "]."
        )

# Create an instance of the TVParty class and run the TV party
party = TVParty()

