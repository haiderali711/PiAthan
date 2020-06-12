# Content
*   [Steps to clone Repository](#steps-to-clone-repository)
*   [Running the program at startup](#running-the-program-at-startup)



## Steps to clone Repository

1.  Installing **Git** in your Raspberry Pi 
    ```bash
        sudo apt install git-all
    ```
2.  Copy the *Copy with SSH* or *Copy with HTTPS* link for this Repository

3.  Open the Terminal and connect to the Pi through ssh on your local machine

4.  ```bash 
    #access the directory
    cd /home/pi/  
    ```
5.  Run the command 
    ```bash
    git clone <link from Step 2>
    ```
5.  For a more interactive experience with Git, **Github Desktop** can also be used as the tool for working with the Git repository

## Running the program at startup

1. Install the needed Packages
    ```bash
    #Access the program folder at do the following step by step in the terminal
    cd /home/pi/PiAthan/pre_exec/

    chmod +x pre.sh

    ./pre.sh

    #if u are denied the rights, just do 
    sudo su 

    ./pre.sh
    ```
2.  Edit the file rc.local and append the command to start the Program on boot

    ```bash
    #step 1
    sudo nano /etc/rc.local

    #step 2
    #add the following line before 'exit 0'
    python3 /home/pi/PiAthan/Athan.py

    #step 3 (Close file)
    cltr + x 

    #step 4 (Save File)
    press Y to save then Enter to save it to the file name provided
    ```

3.  Reboot ur Raspberry Pi
    ```bash
    sudo reboot
    ```