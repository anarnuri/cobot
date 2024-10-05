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
