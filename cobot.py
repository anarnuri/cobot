# import random
# import time
# from pymycobot.mycobot import MyCobot

# mc = MyCobot('/dev/ttyAMA0', 1000000)

# # Initial angles that should not change by more than 10 degrees
# initial_angles = [-150, -90, 0, 0, 0, 0]

# def move_joints_within_range(mc, initial_angles, max_change=10):
#     """
#     Move the myCobot joints to new angles within a small range around the initial values.
    
#     :param mc: MyCobot object
#     :param initial_angles: The initial angles to use as reference
#     :param max_change: Maximum allowed deviation in degrees from initial angles
#     """
#     # Randomly adjust each joint angle within the specified max_change range
#     new_angles = [
#         initial_angles[i] + random.uniform(-max_change, max_change) for i in range(6)
#     ]
    
#     # Ensure new angles stay within the limits for each joint (example limits)
#     joint_limits = [(-155, 155), (-120, 120), (-140, 140), (-130, 130), (-160, 160), (-170, 170)]
#     new_angles = [
#         max(joint_limits[i][0], min(joint_limits[i][1], new_angles[i])) for i in range(6)
#     ]
    
#     # Send the new angles to the myCobot
#     mc.send_angles(new_angles, 10)  # 10 is the movement speed, adjust as needed
#     print(f"Moved to new joint angles: {new_angles}")

# # Set the initial angles
# mc.send_angles(initial_angles, 10)
# print(f"Initial joint angles set to: {initial_angles}")

# # Move the joints 10 times randomly within a ±10 degree range from initial angles
# for _ in range(10):
#     move_joints_within_range(mc, initial_angles, max_change=10)
#     time.sleep(2)  # Add delay between moves

import time
from pymycobot.mycobot import MyCobot
import csv

# Initialize the myCobot with the appropriate port (adjust the port if necessary)
# Replace 'COM3' with the correct port for Windows or '/dev/ttyUSB0' for Linux
mc = MyCobot('/dev/ttyAMA0', 1000000)

# File to save joint values
output_file = 'joint_values.csv'

# Release servos so that you can manually move the robot
mc.release_all_servos()

print("Servos released. You can now move the robot manually.")

# Open CSV file to store joint values
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write header
    writer.writerow(["Joint 1", "Joint 2", "Joint 3", "Joint 4", "Joint 5", "Joint 6"])

    try:
        print("Move the robotic arm through positions manually. Press Ctrl+C to stop recording.")
        
        # Infinite loop to continuously record joint values
        while True:
            # Get current joint angles
            joint_values = mc.get_angles()

            # Print joint values to the console
            print("Current Joint Values: ", joint_values)

            # Write joint values to CSV file
            writer.writerow(joint_values)

            # Pause for a short time (e.g., 0.5 seconds) before recording the next set of joint values
            time.sleep(0.5)

    except KeyboardInterrupt:
        # Handle the user interruption (Ctrl+C)
        print("Recording stopped.")

print("Program ended. Servos are already released.")
