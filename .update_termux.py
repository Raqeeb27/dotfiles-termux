import os
from datetime import datetime

# File to store the date of the last update
UPDATE_LOG = "/data/data/com.termux/files/home/.last_update"

# Get today's date in DD-MM-YYYY format
TODAY = datetime.now().strftime("%d-%m-%Y")


# Function to update the system using pkg or apt
def update_system(manager):
    print(f"Updating the system using {manager} ...")

    # Run the update in a subshell, chained with &&
    ret = os.system(
        f"( DEBIAN_FRONTEND=noninteractive {manager} update --fix-missing > /dev/null 2>&1 && "
        f"DEBIAN_FRONTEND=noninteractive {manager} update > /dev/null 2>&1 && "
        f"DEBIAN_FRONTEND=noninteractive {manager} upgrade -y > /dev/null 2>&1 && "
        f"DEBIAN_FRONTEND=noninteractive {manager} -y autoremove > /dev/null 2>&1 )"
    )

    if ret == 0:
        # Update the log with today's date
        with open(UPDATE_LOG, "w") as f:
            f.write(TODAY)
        print(f"System updated successfully using {manager}.")
    else:
        print(f"System update failed using {manager}.")


# Default to yes if the user just presses Enter
def confirm(prompt=""):
    # choice = input(f"{prompt} (y/n) [default: y]: ")
    choice = "y"
    choice = choice if choice else "y"
    return choice

# Function to handle the update process
def perform_update(choice):
    if choice == "y":
        # faster_choice = confirm("Do you want the update to be faster?")
        faster_choice = "y"
        if faster_choice == "y":
            update_system("apt-get")
        else:
            update_system("pkg")
    else:
        print("System update skipped.")


# Main logic
if os.path.exists(UPDATE_LOG):
    with open(UPDATE_LOG, "r") as f:
        LAST_UPDATE = f.read().strip()
    if LAST_UPDATE == TODAY:
        print("The system is already up-to-date.")
    else:
        # choice = confirm("The system has not been updated today. Do you want to update now?")
        choice = "y"
        perform_update(choice)
else:
    # choice = confirm("No update record found. Do you want to update the system now?")
    choice = "y"
    perform_update(choice)

