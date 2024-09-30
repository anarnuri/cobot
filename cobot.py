import random
import time
from pymycobot.mycobot import MyCobot

# Replace with the port used for your myCobot
mc = MyCobot('/dev/ttyAMA0', 1000000)

def get_current_position(mc):
    """Get the current end effector position."""
    pos = mc.get_coords()  # Get current coordinates [x, y, z, rx, ry, rz]
    return pos

def move_randomly_within_range(mc, range_limit=20):
    """
    Move the myCobot end effector to a random position within a small range.
    
    :param mc: MyCobot object
    :param range_limit: The maximum deviation in mm from the current position
    """
    # Get current position
    current_pos = get_current_position(mc)
    if current_pos:
        print(f"Current position: {current_pos}")
        
        # Randomly change x, y, z within the specified range
        new_x = current_pos[0] + random.uniform(-range_limit, range_limit)
        new_y = current_pos[1] + random.uniform(-range_limit, range_limit)
        new_z = current_pos[2] + random.uniform(-range_limit, range_limit)
        
        # The rest of the position data (rx, ry, rz) remains unchanged
        new_position = [new_x, new_y, new_z, current_pos[3], current_pos[4], current_pos[5]]
        
        # Move to the new position
        mc.send_coords(new_position, 50)  # 50 is the movement speed, adjust as needed
        print(f"Moved to new position: {new_position}")
    else:
        print("Failed to retrieve current position.")

mc.send_angles([-160, -90, 0, 0, 0, 0], 10)

# Move the end effector 10 times randomly
for _ in range(10):
    move_randomly_within_range(mc, range_limit=10)  # Limit random movements to ±10 mm
    time.sleep(2)  # Add delay between moves
