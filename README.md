Setting Up a Cron Job to Automatically Run a Script on Linux Server Reboot
Introduction
This guide provides detailed steps to set up a cron job on a Linux server. The cron job is configured to automatically execute a specific `.sh` script located in a directory whenever the server reboots or recovers from a shutdown.
Prerequisites
- Access to the Linux server (via SSH or direct terminal access).
- Basic understanding of Linux command line.
- The script (`your_script.sh`) that needs to be executed, placed in a known directory.
Step-by-Step Guide
Step 1: Connect to Your Linux Server
Log into your Linux server via SSH or open the terminal if you have direct access.
Step 2: Open the Crontab Configuration
Type the command `crontab -e` in the terminal. This will open the crontab file in the default text editor.
Step 3: Add the Cron Job
At the end of the crontab file, add the line:
`@reboot /path/to/your/script.sh`
Replace `/path/to/your/script.sh` with the actual path to your script.
This line tells the cron daemon to run your script at every system startup.
Step 4: Save and Exit
Save the changes to the crontab file:
- In `nano`, use `Ctrl + O` to save, followed by `Ctrl + X` to exit.
- In `vi`, press `Esc`, type `:wq`, and press `Enter`.
The cron job is now set and will activate at the next reboot.
Step 5: Verify the Cron Job
To confirm the cron job is scheduled, use `crontab -l`.
This lists all cron jobs for your user, including the new `@reboot` job.
Conclusion
Your Linux server is now configured to execute a script automatically after each reboot. This is particularly useful for initialization scripts or recovery tasks.
Additional Notes
- **Permissions**: Ensure the script is executable (`chmod +x /path/to/your/script.sh`).
- **User Context**: The script will run under the user whose crontab you edited. Make sure this user has the necessary script permissions.
- **Logging**: For debugging, consider redirecting script output to a file in your cron job: `@reboot /path/to/your/script.sh >> /path/to/logfile 2>&1`.
