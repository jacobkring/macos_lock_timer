To use - first update the idle_lock_tracker.plist file to point to the path that contains the idle_lock_tracker.py file

default set time limit is 600 s (10 minutes), you can tweak idle_lock_tracker to make it however long is needed

move idle_lock_tracker.plist to ~/Library/LaunchAgents

then call 'launchctl load ~/Library/LaunchAgents/local.tf.idle_lock_tracker.plist' from any terminal window

You will probably have to grant python permissions to control your system
