# VSCode

VS Code is significantly lightweight than Visual Studio, and you fell it because it runs applications in the background and independent from the IDE, making sure the IDE doesn't slow down.
No matter what type of project, VS Code easily helps you set up the IDE. It can also run Azure and Docker and can deploy with confidence and ease when it comes to deploying applications. It supports Git and easy debugging, and it has IntelliSense that helps improve error-free and clean coding.

https://code.visualstudio.com

tasks.json (build instructions, tell VS Code how to build (compile) a program)
launch.json (debugger settings)
Starting VS Code in a folder 
→ that folder becomes your "workspace"
→ that workspace settings are in .vscode/settings.json (separate from user settings stored globally)

### Extensions
https://marketplace.visualstudio.com/items?itemName=Oracle.oracledevtools
https://code.visualstudio.com/api/extension-guides/webview
https://github.com/microsoft/codetour: record and playback guided tours of codebases, directly within the editor.
https://code.visualstudio.com/docs/remote/remote-overview

Ex: https://marketplace.visualstudio.com/items?itemName=rfukuma.background-image  
Download it → rfukuma.background-image-1.0.0.vsix  
Is a ".zip" file  
Rename to .zip to view inside
- extension.vsixmanifest
- [Content_Types].xml
- extension  
-> README.md  
-> package.json  
-> CHANGELOG.md  
-> out/  
    . main.js   
    . config.js  
    . ...

### VS Code themes
- https://themes.vscode.one/

### VS Code Remote Development
https://code.visualstudio.com/docs/remote/remote-overview

process of attaching to a development environment sitting either in a 
- Virtual Machine
- WSL
- on a Docker container

- https://code.visualstudio.com/docs/remote/remote-overview
- https://cloudblogs.microsoft.com/industry-blog/en-gb/cross-industry/2020/12/15/run-blazor-in-a-docker-container-with-visual-studio-code-remote-development/

Remote - SSH 
    Connect to any location by opening folders on a remote machine/VM using SSH.
Remote - Containers
    Work with a separate toolchain or container-based application inside (or mounted into) a container.
Remote - WSL
    Get a Linux-powered development experience in the Windows Subsystem for Linux.


- [VSCode's Python Interactive mode is AMAZING!](https://www.youtube.com/watch?v=lwN4-W1WR84&t=358s)
VS Code:  xxxx.py  # %%   → get a notebook	

Develop in remote containers using VS Code
https://docs.microsoft.com/en-us/windows/wsl/tutorials/wsl-containers

## Remote Repositories 

Browse, search, edit, and commit to any remote GitHub repository directly from within Visual Studio Code. 
- https://www.youtube.com/watch?v=wHsmaXoGIXI

Green indicator left/bottom → "Open remote repository"

## Productivity tips

https://www.youtube.com/watch?v=ifTF3ags0XI


1. VS CODE CLI
code .          # open current directory (Command Palette, Shell command: install 'code' cmd in path)
code file.js    # open file

2. RELEASE THE MOUSE
Check shortcuts

3. COMMAND PALETTE: CTRL+P
files by default

4. RUN COMMANDS
Add '>' to have commands

5. QUOKKA
JavaScript and TypeScript playground in your editor.
>quokka

6. FIND SYMBOLS WITH @
@ show page symbols to quickly navigate to
CTRL+F or.... @searched_symbol

7. FIND SYMBOLS WITH #
># global_symbol_search
Type just the first char of words

8. MOVE AROUND QUICKLY
>:23
Hightlight: Shift + ←/→ 
Hightlight: Ctrl + ←/→      by words

9. MULTILINE EDITING
Find matches: CTRL + D
Set multiple cursors: Alt + click    or    ALT + SHIFT + ↑ / ↓ 

10. AUTO RENAME TAG
Extension to rename tag start/end

11. DELETE OR MOVE A LINE
Alt + X 
Alt + ↑ / ↓

12. HIGHLIGHT & COMMENT LINES
Highlight line: CTRL + L
Comment Lines: CTRL + /

13. JS DOC EXTENSION

14. BETTER COMMENTS

15. INTEGRATED TERMINAL

CTRL + ù
CTRL + `
- powershell
- bash
- cmd
- node
- python

SETTINGS - Change Default Terminal

- Right click a terminal to change its color, icon, rename
- CTRL+P >terminal: Select Default Profile
- File -> Preferences -> Settings
  "terminal.integrated.shell.windows": "C:\\WINDOWS\\System32\\bash.exe"`
  
- File -> Preferences -> Keyboard Shortcuts
    //with this you can select what type of console you want
    {
        "key": "ctrl+shift+t",
        "command": "shellLauncher.launch"
    },

    //and this will help you quickly change console
    { 
        "key": "ctrl+shift+j", 
        "command": "workbench.action.terminal.focusNext" 
    },
    {
        "key": "ctrl+shift+k", 
        "command": "workbench.action.terminal.focusPrevious" 
    }`

16. VS CODE TASKS
json configuration files having command to run in the terminal or from command palette (>run)

17. GIT SOURCE CONTROL

18. GIT LENS EXTENSION

19. REMOTE REPOSITORIES
Normally to work on  a repo on github you need to clone it to your local system
Install the extension then click the bottom left corner to open up a remote repo (log in)

20. REMOTE SSH & CONTAINERS
Open any folder or repository inside a Docker container and take advantage of Visual Studio Code's. Deveop in containers instead of your local system

21. CUSTOM SNIPPETS
your own or...
flutter snippet extensions

22. COMMUNITY SNIPPETS

23. AUTO-CREATE DIRECTORIES

24. PASTE AS JSON EXTENSION
infer type with quicktype tool

25. RENAME SYMBOL

CODE FOLDING
Ctrl+Shift+[ to fold
Ctrl+Shift+] to unfold from the current cursor position

Ctrl+K Ctrl+0 to fold
Ctrl+K Ctrl+J to unfold all sections

 Ctrl+K Ctrl+1 → Ctrl+K Ctrl+5 for indentation folding

Errors and warnings
F8 to sequentially navigate across underlines errors and view the detailed error message

JavaScript type checking
Visual Studio Code has a strong pull towards JavaScript and TypeScript.
//@ts-check comment on top of the file will run a TypeScript type checker 

apply the type check to the complete workspace by using the “javascript.implicitProjectConfig.checkJs” : true to the complete workspace and using //@ts-nocheckor //ts-expect-errorto individual files or lines.

Advice: Keyboard Over Mouse

Don't Use the Sidebar in VS Code
https://www.youtube.com/watch?v=s3H6PmB4SZ4
CTRL+W      Close file
CTRL+P      ...type filename
CTRL+TAB    switch between files
Extension advanced new file → ctrl+p then 'advanced..." then paths propositions


vscode:extension/mushan.vscode-paste-image

https://marketplace.visualstudio.com/items?itemName=mushan.vscode-paste-image

