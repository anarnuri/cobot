import time
import csv
from pymycobot.mycobot import MyCobot

# Initialize the myCobot with the appropriate port
# Replace '/dev/ttyUSB0' with the correct port for your setup
mc = MyCobot('/dev/ttyAMA0', 1000000)

# File with the recorded joint values
input_file = 'joint_values.csv'

# Function to move the robot through each recorded position
def move_through_positions():
    # Open the CSV file containing the recorded joint values
    with open(input_file, mode='r') as file:
        reader = csv.reader(file)
        # Skip the header
        next(reader)

        print("Moving through recorded positions...")

        for row in reader:
            # Convert each joint value from the CSV (strings) to float
            joint_values = [float(value) for value in row]

            # Print the joint values being used for each movement
            print("Moving to Joint Values: ", joint_values)

            # Move the robot to the given joint values
            mc.send_angles(joint_values, 50)  # 50 is the speed; adjust if necessary

            # Pause to allow the robot to reach the position before moving to the next one
            time.sleep(2)  # Adjust sleep time as needed based on movement speed

# Run the function to move through recorded positions
move_through_positions()

print("Finished moving through all recorded positions.")