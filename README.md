# Vaccins

Install chrome and the chromedriver:
1. Check whether you have chrome installed, otherwise install it. Download the .deb file form https://www.google.com/chrome/ (if help needed with installation, please use the guideline below)
2. If installed, open https://www.whatismybrowser.com/detect/what-version-of-chrome-do-i-have. Write down somewhere what chrome version you have. I am having 88 at this moment.
3. Go to https://chromedriver.chromium.org/downloads and select the chromedriver for your chrome version.
4. Download the chromedriver_linux64.zip
5. Open the .zip folder and place the chromedriver in /usr/bin. If you have no idea how to do this, place the chromedriver to the Desktop and use command "sudo mv ~/Desktop/chromedriver /usr/bin"

Google Chrome Installation:
1. Go to the folder where the .deb file was downloaded.
2. Type sudo apt install thedebfilenamehere.deb (replace the name before .deb with the original file name)
3. If encountered an error 13, please use the error guideline below.

Get credentials:
1. Get a telegram account and register yourself.
2. Visit https://telegram.me/botfather on your phone and send him a message: <b>/start</b>.
3. BotFather will give a lot of commands in an overview and will tell you how to create a new bot. Write <b>/newbot</b>.
4. Give your bot a name. This is the name he will have when communicating to you.
5. Choose an username for the bot. This is just where you will find the bot itself. The name must end with "bot" (e.g. CrowdStrikebot).
6. Insert the token in keys.py at variable token.
7. Visit https://telegram.me/myidbot on your phone and send him a message: <b>/start</b>.
8. Write <b>/getid</b>.
9. The IDBot will give you your chatID that the BotFather will use to communicate only to you. Use this chatID in the keys.py file.

First time usage:
1. Install all packages mentioned in requirements.txt
2. Use python3 init.py to start the bot.

<h2>Error solving</h2>
Error: Download is performed unsandboxed as root as file 'ANYDEBFILE.deb' 
couldn't be accessed by user '_apt'. - pkgAcquire::Run (13: Permission denied)
Solution: Execute the following commands below and try the installation of the package again:

sudo chown -Rv _apt:root /var/cache/apt/archives/partial/

sudo chmod -Rv 700 /var/cache/apt/archives/partial/
