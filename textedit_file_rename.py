#!/usr/bin/python3
# Basic File Renamer

info = {
    "name": "Text edit file renamer",
    "description": "Rename files by dropping selection on python file",
    "author": "Samuel Bernou",
    "version": (0, 2, 1),
    # "warning": "",
    "doc_url": "https://github.com/Pullusb/textedit_file_renamer",
    "category": "Utils" }

import sys, os
from pathlib import Path
import subprocess

# command or path to editor
editor = Path(__file__).with_name('editor.txt')

src = Path(__file__).with_name('src.txt')
dest = Path(__file__).with_name('dest.txt')
temp = Path(__file__).with_name('temp.txt')


def random_string_chain(length):
    import string, random
    base = string.ascii_lowercase # + string.digits
    return ''.join(random.choices(base, k = length))

def tmp_name(name):
    '''return name with stem randomly suffixed __rn_???????'''
    if '__rn_' in name:
        return name
    stem, ext = os.path.splitext(name)
    stem += '__rn_' + random_string_chain(7)
    return ''.join([stem, ext])

def rename_dropped():
    if len(sys.argv) <= 1:
        print('Need to drop at least one file on py file')
        return

    all_files = [Path(p) for p in sys.argv[1:]]
    all_files.sort() # sort - drop order makes no sense

    print(f'{len(all_files)} items dropped')

    with src.open('w') as fd:
        for fp in all_files:
            fd.write(fp.as_posix() + '\n')
    
    with dest.open('w') as fd:
        for fp in all_files:
            fd.write(fp.name + '\n')
    
    if not src.exists() or not dest.exists():
        print('problem, src.txt or dest.txt could not be created')
        return

    #-# open dest in default editor or the one specified in first line of editor.txt
    cmd = [str(dest)]
    if editor.exists():
        with editor.open('r') as fd:
            bin = fd.readlines(1) # read only first line
            if bin and bin[0].strip():
                # bin[0]
                cmd = [bin[0].strip() , str(dest)]

    subprocess.Popen(cmd, shell=True)
    

    ## PAUSE HERE - user modification - then resume
    print('Edit the names in file "dest.txt" and save the file')
    input('Then press Enter to start\n')

    ## alternatively trigger rename once text editor is closed
    # print('Once "dest.txt" is closed, the process will start')
    # p = subprocess.Popen(cmd, shell=True)
    # p.wait() #works with txt editor but not with vscode/codium (sublime text just needs `-w` in command args)
    

    with dest.open('r') as fd:
        new = fd.read().split('\n')
    last = new.pop()

    ## Run checks
    if last:
        print('Abort: program error. Last item in new list is not empty: {last}')
        return
    
    if len(new) != len(all_files):
        print(f'Abort: file count miss-match {len(all_files)} in source, {len(new)} new names')
        return
    
    double = []
    for n in new:
        if n in double:
            print('Abort: {n} exists twice')
            return
        double.append(n)

    if [s.name for s in all_files] == new:
        print(f'Abort: Identical source and destination !')
        return
    
    ## end cehcks

    print('\n-- Rename preview --')

    # Display preview
    for s, d in zip(all_files, new):
        ## s:path object, d: srt
        if not s.exists():
            print(f'{s.name} not found in source ! (will be skipped)')
            continue

        if s.name == d:
            print(f'{s.name} == {d} (unchanged)') # name
            continue

        print(f'{s.name} >> {d}')

    ## PAUSE for validating preview
    input('\nPress Enter to valid rename (or just close console)\n')
    
    print('\n-- Renaming --')

    ## temporary rename step - rename everything with an uid...
    temp_dest = [n.with_name(tmp_name(n.name)) for n in all_files]
    with temp.open('w') as fd:
        for s, t, d in zip(all_files, temp_dest, new):
            if s.name == d:
                # same names, rewrite source since line must exists
                fd.write(s.as_posix() + '\n') # 
                continue

            fd.write(t.as_posix() + '\n')
            s.rename(t)

    ## Rename from temp uid to final name
    for s, t, d in zip(all_files, temp_dest, new):
        if not t.exists():
            continue

        if s.name == d:
            # print(f'{s.name} == {d}') # print same ?
            continue

        print(f'{s.name} >> {d}') # print with original source name
        t.rename(t.with_name(d))


    ## Direct rename (does not allow rename conflict like name swapping)
    # for s, d in zip(all_files, new):
    #     if not s.exists():
    #         print(f'{s.name} not found in source !')
    #         continue
    #     print(f'{s.name} >> {d}')
    #     s.rename(s.with_name(d))
    return

rename_dropped()
input('\nPress Enter to close')
