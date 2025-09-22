##  Question 1: YouTube Video Quality Selection
##  Scenario: A user is watching a YouTube video and the platform must select the appropriate video quality
##  based on two conditions: - Internet speed - Whether the user selected "Auto" mode or manual mode.
##   Logic Steps
##  : - Ask if the user selected "Auto" or "Manual" mode. - If "Auto": - If internet speed > 10 Mbps
##  → Play 1080p - Else if speed > 5 Mbps → Play 720p - Else if speed > 2 Mbps → Play 480p - Else → Play 240p 
## If "Manual": - Ask for selected quality (e.g., 240p, 480p, 720p, 1080p) - Play the selected quality
##  Expected Understanding: Learn to handle multiple nested conditions and simulate real-time
##  decision logic.

user = input("select auto or manual   :").lower()
netspeed = int(input("enter net speed in MB: "))

if user == "auto":
    if netspeed >= 10:
        print("Play video quality 1080p")
    elif netspeed >= 5:
        print("Play video quality 720p")
    else:
        print("Play video quality 480p")

elif user == "manual":
    videoquality = input("select video quality you want (480p, 720p, 1080p, 4k): ").lower()
    if videoquality == "480p":
        print("Video playing on 480p quality")
    elif videoquality == "720p":
        print("Video playing on 720p quality")
    elif videoquality == "1080p":
        print("Video playing on 1080p quality")
    elif videoquality == "4k":
        print("Video playing on 4k quality")
    else:
        print("Invalid video quality selected")
else:
    print("Invalid mode selected, please select auto or manual")





