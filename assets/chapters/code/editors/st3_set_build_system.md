 ## Sublime Text 3: Set C# Compiler
 Tools → Build System → new Build System 
 {   
	"cmd": ["C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\MSBuild\\Current\\Bin\\Roslyn\\csc.exe", "$file"]
}
Save as "C:\Users\[you]\AppData\Roaming\Sublime Text 3\Packages\User\C#.sublime-build"

Then open a .cs file, Select Tools → Build System → C# → CTRL-B to build it