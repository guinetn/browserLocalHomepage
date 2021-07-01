# Windows Terminal

Terminal for users of command-line tools and shells like Command Prompt, PowerShell, and WSL. Its main features include multiple tabs, panes, Unicode and UTF-8 character support, a GPU accelerated text rendering engine, and custom themes, styles, and configurations.


## Customization

Default settings: color schemes, keyboard shortcuts...
To view the default settings file: Alt + click ⚙️ inside the dropdown menu.
Ex: C:\Users\--YOU--\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json

"defaults":
{
    // SETTINGS TO APPLY TO ALL PROFILES
},
"list":
[
    // PROFILE OBJECTS
]


- https://docs.microsoft.com/windows/terminal/customize-settings/profile-settings
- https://docs.microsoft.com/windows/terminal/customize-settings/color-schemes

Ex: https://github.com/DamourYouKnow/windows-terminal-miku
Copy the content of /profile inside C:\Users\--YOU--\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\

## Launch terminal in a specific configuration 
wt -p "PowerShell" -d . ; split-pane -V
set are tab and pane arrangements as well as their starting directories and profiles
save a custom command as a shortcut and pin it to your taskbar to open your desired configuration.

## Panes
Windows Terminal has pane support for profiles. You can open a new pane of a profile by either holding Alt and clicking on the profile in the dropdown, or by using the following keyboard shortcuts:

Alt+Shift+D         Automatic pane split of current profile
Alt+Shift+Minus     Horizontal pane split of default profile
Alt+Shift+Plus      Vertical pane split of default profile

[wt command line arguments ](https://docs.microsoft.com/windows/terminal/command-line-arguments?tabs=windows)

### more
- https://docs.microsoft.com/fr-fr/windows/terminal/
- https://docs.microsoft.com/fr-fr/windows/terminal/get-started
- https://aka.ms/terminal
- https://github.com/microsoft/terminal
- https://docs.microsoft.com/windows/terminal/panes