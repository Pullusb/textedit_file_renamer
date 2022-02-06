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

#### Note:

Set text editor executable (or existing shortcut command) in first line of `editor.txt`  

If `editor.txt` not exists or is empty (as default) it will open with default system text editor.


#### Why ?

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
