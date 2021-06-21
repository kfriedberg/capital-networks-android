# capital-networks-android
Bulk actions on Capital Networks Android based signage players.  Current actions are
* `checknightly.py` Get nightly restart/reboot behaviour
*  `setnightly.py` Set a nightly reboot

## Windows Setup
* (In command prompt) run `python`  
If you don't already have python installed, you'll be taken to the Windows Store to install it  
If you do have python installed you'll get the `>>>` python prompt.  `quit()` back to the command prompt

* Run `pip install -U selenium`

* Download the ChromeDriver that matches the version of Chrome installed on your computer from  
https://sites.google.com/a/chromium.org/chromedriver/downloads  
and copy it to this folder.  You will likely need a new version of this file every time Chrome updates.

* Create a file called `credentials.txt`
  * Put the username as the first line of the file
  * Put the password as the second line of the file

* Create a file called `sites.txt`
  * Put the FQDN or IP of each player you want to set/check, one per line

* Run `python checknightly.py` to check the nightly restart status of each player in the sites.txt file.
  * Results will be written to the file `checklog-(date and time).txt` and output to the console

* Run `python setnightly.py` to set the nightly restart status of each player in the sites.txt file.
  * Results will be written to the file `setlog-(date and time).txt` and output to the console
