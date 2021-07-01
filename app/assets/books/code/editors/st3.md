# SUBLIME TEXT

https://www.sublimetext.com/docs/3/


download.page(code/editors/st3_set_build_system.md)

## PATHS

C:\Users\nguin\AppData\Roaming\Sublime Text 3\Installed Packages Downloaded / user packages binaries
C:\Users\nguin\AppData\Roaming\Sublime Text 3\Packages           Downloaded / user packages code
C:\Users\nguin\AppData\Roaming\Sublime Text 3\Packages\User      Build system files, ex C#.sublime-build 

## SUBLIME REGEX

- Find: (?<item>……)
- Replace: $1

Input
    "header": [ "gmail[]=https://gmail.com", "class":"fas fa-envelope", "linkedin[]=https://www.linkedin.com", "class":"fab fa-linkedin" ]

Find: (?<bra>\[\])(?<other>.*)"class": ?"(?<class>[^"]*)"
Replace: [$3]$2
    
Output
    "gmail[fas fa-envelope]=https://gmail.com", ,
    "linkedin[fab fa-linkedin]=https://www.linkedin.com", ,      


## Settings
Preferences.sublime-settings

* Sublime Text´s default font face?
"font_face": "Courier New"   consolas → default on Windows
"font_size": 10

* caret style
"caret_style": "solid"
Other available options include “smooth”, “phase”, “blink”, “wide” and “solid”

* Highlight current Line
"highlight_line": true
    
* Change active tab title color
"highlight_modified_tabs": true,

* Allow double space for markown syntax after save
"trim_trailing_white_space_on_save": false,   

* Exclude a directory from searching in Sublime Text
"folder_exclude_patterns": ["node_module","dist", ".git"]

SEARCH TAB
    -*/name_of_dir/*                                                    skip 'name_of_dir' folders
    */*backend*/*.js, */*backend*/*.json,*/*backend*/*.ts               only in *backend* folder
    */*backend*/*.js, */*backend*/*.json,*/*backend*/*.ts, -*/docs*/    remove /docs folder



## ESSENTIAL

CTRL + /                Comment/UnComment with //
CTRL + SHIFT + /        Comment/UnComment with /* … */

CTRL + D                Select Word / select next occurrence (Multiple Selections → rename variables quickly)
Ctrl + K, Ctrl + D      To skip the current instance
Alt+F3                  Found all occurences of the current selection for multiple editing
CTRL + L                Select line
CTRL + CLICK            Create multiple cursors for multi-editing
CTRL + SHIFT + M        Expand to brackets
CTRL + SHIFT + J        Expand to indentation
CTRL + SHIFT + SPACE    Expand selection to scope (in file code). Repeating keeps expanding
CTRL + M                Go to matching bracket

CTRL + ENTER            Insert line after
CTRL + SHIFT + K        Delete line
CTRL + J                Join Line
CTRL + SHIFT + D        Duplicate line
CTRL + F + ALT + ENTER  Find a certain term then select them all for multi-editing

CTRL + W                Close Tab
CTRL + SHIFT + N        New Window
CTRL + N                New Tab

CTRL + F2               Create Bookmark
F2                      Next Bookmark
SHIFT + F2              Previous Bookmark

Ctrl + P                File Switching + @codesymbol #word or #ptial :99
                                            isl#trsr find tresor in island file

## COLUMN SELECTION

Shift + Right Mouse Button
OR: Middle Mouse Button
Add to selection: Ctrl

## BASIC

F11                     Full Screen
SHIFT + F11             Distraction Free Mode
CTRL + SHIFT + P        Command Palette
CTRL + K + B            Toggle Sidebar
CTRL + /                Comment
CTRL + SHIFT + /        Block Comment
CTRL + K + U            Uppercase
CTRL + K + L            Lowercase

## GO TO

CTRL + M                Go to matching bracket
CTRL + G                Go to line number
CTRL + R                Browse to a specific function or method (in code file)
CTRL + P                Open file based on name/File Switching
                        Instantly see a tree of your html document
                        Type @ to jump to symbols, Open file based on name and search for symbol
                                # to search within the file
                                isl#trsr    fuzzy search for trsr in files whose name loosely matches isl.
                                            could find the word treasure inside a file named island.txt
                                : to go to a line number

## SELECTIONS

CTRL + D                Select Word
CTRL + D                Use multiple times to select next instance of the selected word
CTRL + CLICK            Create multiple cursors for multi-editing
CTRL + SHIFT + SPACE    Expand selection to scope (in file code). Repeating keeps expanding
CTRL + SHIFT + M        Expand selection to brackets
CTRL + SHIFT + J        Expand selection to indentation

## LINES

CTRL + L                Select line
CTRL + SHIFT + K        Delete line
CTRL + ]                Indent
CTRL + [                Unindent
CTRL + ENTER            Insert line after
CTRL + SHIFT + ENTER    Insert line before
Ctrl + Shift + Up/Dn    Move the line up/Down
                        CTRL + SHIFT + ↑        Swap line up
                        CTRL + SHIFT + ↓        Swap line down
CTRL + SHIFT + D        Duplicate line
CTRL + J                Join Line

## SEARCH / FIND / REPLACE

CTRL + F                Find. use Regex:   [1-9]+
F3                      Find next
SHIFT + F3              Find previous
CTRL + SHIFT + F        Search all files in a folder
CTRL + H                Replace
CTRL + F + ALT + ENTER  Find a certain term then select them all for multi-editing
Alt+F3                  Found all occurences of the current selection
                        escape to a single selection

(\d) → ${0}

## TABS AND WINDOW PANES

CTRL + SHIFT + N        New Window
CTRL + N                New Tab
CTRL + W                Close Tab
ALT + 1…234             Focus a Tab (Alt + 3)
CTRL + SHIFT + #        Move tab to a Pane (ie ctrl + shift + 2)

ALT + SHIFT + 1 restore columns/rows views to a single view
COLUMNS…
ALT + SHIFT + 1         One Column
ALT + SHIFT + 2         Two Columns
ALT + SHIFT + 3         Three Columns
ALT + SHIFT + 4         Four Columns

ROWS…
ALT + SHIFT + 8         Two Rows
ALT + SHIFT + 9         Three Rows
ALT + SHIFT + 5         Two x Two Grid

2 views a the same file: ALT + SHIFT + 8 then File → New View into File → Move the file into the GROUP2


## BOOKMARKS F2 (not saved)

CTRL + F2               Create Bookmark
F2                      Next Bookmark
SHIFT + F2              Previous Bookmark
CTRL + SHIFT + F2       Clear Bookmarks