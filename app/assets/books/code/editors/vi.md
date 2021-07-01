# VI (VISUAL EDITOR)

VIM (VISUAL EDITOR IMPROVED)
http://vimdoc.sourceforge.net/

https://www.liquidweb.com/kb/overview-of-vim-text-editor/
vim example.conf

## install

sudo apt-get update
sudo apt-get install vim

## Concept: modes

### Séparation de l'écran

vim -o fichier1 fichier2        split screen horizontaly
vim -O fichier1 fichier2        split screen vertically
Ctrl-W Ctrl-W      switch betweens screens
Ctrl+w followed by “s” splits the window horizontally.
Ctrl+w followed by “v” splits the window vertically.
Ctrl+w and any of the navigation keys (hjkl) can be used to move between the windows.


### MOTIONS: TEXT NAVIGATION

h j k l
← ↓ ↑ →

w       beginning of next word
b       beginning of previous word
e       ending of current word

0       beginning of line
$       end of line
^       first non-space character in the line
G       end of file
gg      beginning of file
CTRL DU Page Up/DN 

nG      jump to line number n
)       jump forward a sentence
}       jump forward a paragraph

this may seem odd at first, switching from mode to mode actually speeds typing up, as you do not have to move your right hand over to the arrow keys and back every time you wish to reposition the cursor.

workspace view: zz, zt, zb instead of scrolling with the mouse.

# INSERT MODE
i    leave normal mode → enter insert mode → start typing text
a    leave normal mode → enter append mode

i   Inserts text before current cursor location.
I   Inserts text at beginning of current line.
a   Inserts text after current cursor location.
A   Inserts text at end of current line.
o   Creates a new line for text entry below cursor location.
O   Creates a new line for text entry above cursor location.

ciw  “change in word”: edit the whole current word
dw    delete word” 
cw    change word
x  r  Single-character edits

gUiw    UpperCase
guiw    lowercase


COPY-PASTE
d    delete the line the cursor is on
y    yank/copy the line
p    put/paste
x    cut

v + [hjkl $0]  copy word/line

u    undo
Ctrl+r   redo

ESC  to get back to normal mode

ACTIONS ON THE ENTIRE LINE 
No motion needed

dd      To delete the current line
yy      To copy the current line



### SEARCH IN VI

/   search. / will pulling up the search prompt
type mysearch + [ENTER]
n for next
N for previous

%       parentheses matching
:s      substitute. Find-replace on steroids

edit/recall your search history: 
pulling up the search prompt with /
cycle with C-p/C-n
q/, which takes you to a window where you can navigate the search history.


Most useful shortcut in vim is the * key
Put the cursor on a word and hit the * key and you will jump to the next instance of that word.
The # key does the same but jumps to the previous instance of the word.

To go to a specific character in the current line, use “f” followed by the character. Use “F” to do the search backward. You can also use “t” or “T” the same way to go to the position just before the character you are searching for. F is short for “find” and T is short for “till.”
To go to the next search in the same line, press “;” and “,” for previous depending on whether you searched forward or backward.
To search the current word under the cursor, use “*.”

### REPLACE

1. open a file in Vim
2. interactively search and replace with
:%s/\<word\>/newword/gc

%           look in all lines of the current file
s           for "substitute"
\<word\>    matches the whole word
g           for “global” is for every occurrence
c           let you view and confirm each change before it’s made (faster without c)

### COMMAND-LINE MODE

perform a range of commands
":" (the colon) in normal mode, this will drop the cursor to the bottom of the terminal


:w              Save your changes (write)
:w filename
:wq             Save & Exit
:x              Save & Exit
:f filename     Renames current file to filename.
:wq / ZZ        Exit and save changes if any have been made

:q      Exit when no changes
:q!     Exit without saving changes            
:!q     Cause error "/bin/bash: q: command not found"

After you have run a command, vim will place you back in normal mode.







# ENCRYPTING A FILE USING VIM
You can encrypt a file using vim, just type :X



https://www.learnenough.com/text-editor-tutorial#sec-vim
https://www.liquidweb.com/kb/overview-of-vim-text-editor/
https://docs.oracle.com/cd/E19683-01/806-7612/editorvi-43/index.html

http://www.tutorialspoint.com/unix/unix-vi-editor.htm
https://www.cs.colostate.edu/helpdocs/vi.html
http://www.lagmonster.org/docs/vi.html

# Default editor that comes with the UNIX operating system
# Alternate editors for UNIX environments include pico and emacs, a product of GNU

# VIM (Vi IMproved)   improved version of vi editor

vi filename         Creates a new file if it already does not exist, otherwise opens existing file.
vi -R filename      Opens an existing file in read only mode.
view filename       Opens an existing file in read only mode.

~ represents an unused line on the editor


Command mode         Insert mode 
# ESC / Esc twice  ← →        i


# Command mode 
Whatever you type is interpreted as a command. Starts mode
Administrative tasks: save, find, replace, executing commands, moving the cursor, cutting (yanking) and pasting lines or words

x   Deletes the character under the cursor location.
X   Deletes the character before the cursor location.
dw  Deletes from the current cursor location to the next word.
d^  Deletes from current cursor position to the beginning of the line.
d$  Deletes from current cursor position to the end of the line.
D   Deletes from the cursor position to the end of the current line.

dd  Deletes the line the cursor is on.
p paste the deleted line

yy copy line




vi [filename] - opens VI text editor, if the file doesn’t exist, it’ll be created on saving.
using i inserts
pressing escape and then : goes back to command mode.
/searchstring searchs for searchstring using regular expressions.
: followed by w writes
: followed by qw writes then quits
: followed by q quits.
: followed by q! quits regardless of whether changes are made.
: followed by z undos.









