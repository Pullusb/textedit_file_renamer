# Textedit File Renamer 

A very basic file renamer using any text editors

Made in Python :snake:

**[Download Latest](https://github.com/Pullusb/textedit_file_renamer/archive/refs/heads/main.zip)**

---

### Description

Drop the files you want to rename on `textedit_file_rename.py`

It will open a console describing the step to follow then create a `dest.txt` with current names in a text editor.

Steps:

    - Once edited and satisfied with the names, save `dest.txt` and go back to console.  
    - Press enter to check for error and see a preview of renaming  
    - Press enter again to launch the rename

#### Choose editor:

Set text editor executable (or existing command name) in first line of `editor.txt`  

If `editor.txt` not exists or first line is empty, it will open with default system text editor.


### Set up for Linux:

On windows drag and drop works directly on the `.py` file  
On linux (at least ubuntu) you have to setup a launcher (right-click add launcher)  

This will receive the dropped file and call the script with file as argument (using `%F` keyword for multiple args).  
Set Command : `python3 /path/to/textedit_file_rename.py %F`  
Tick `Launch In Terminal`  

Your launcher should look like this (once opened in a text editor):

```
[Desktop Entry]
Name=texted_file_renamer
Exec=python3 /home/user/Documents/softs/textedit_file_renamer/textedit_file_rename.py %F
Comment=Drop file selection to start rename
Terminal=true
Icon=cinnamon-panel-launcher
Type=Application
```

<!-- If needed, add execution rights to the script :  `chmod +x textedit_file_rename.py` -->

### Why ?

I used several renamer software, and those are a blast for precise batch rename.  
But there are cases where you have to rename files that have  some non-scriptable variations.  
I encountered the situation again and this were my thoughts:  
"Rhaaa! It would be so easy if filenames were editable like in a multi-cursor modern text editor..."  
"..."  
"Wait!"  
:grin:

<!-- So here it is: rename in editor, then trigger the action. :grin: -->

---

MIT license
Disclosure: Not heavily tested. I am Not responsible if this mess up your file names

If you want to support my work:

- my [gumroad](https://pullusb.gumroad.com) store.
- my [blender market](https://blendermarket.com/creators/pullup) page
- other mean of support [here](http://www.samuelbernou.fr/donate).
