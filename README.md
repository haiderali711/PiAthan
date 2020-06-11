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

1.  Create a new .service file in the systemd directory 
    ```bash
    sudo nano /lib/systemd/system/athan.service
    ```
2.  Write the following in the file and save it
    ```bash
    [Unit]
    Description=Athan Service
    After=multi-user.target

    [Service]
    ExecStart=/usr/bin/python3 /home/pi/PiAthan/Athan.py

    [Install]
    WantedBy=multi-user.target
    ```
3.  Save and close the file by choosing ctrl + x, and then y.

4.  Let the Systemmd recognize the Athan service
    ```bash
    sudo systemctl daemon-reload
    ```
5.  Enable the service to be loaded by Systemmd on Boot

    ```bash
    sudo systemctl enable athan.service
    ```

6. ```bash
    #Access the program folder at do the following step by step in the terminal
    cd /home/pi/PiAthan/pre_exec/

    chmod +x pre.sh

    ./pre.sh

    ```

