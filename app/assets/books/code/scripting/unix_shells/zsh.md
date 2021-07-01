# ZSH - Z shell (UNIX SHELL)

Extends functionality of the Bourne Shell (sh): new features, plugins support, themes
Starting with MacOS Catalina in 2019, Zsh became the default login and interactive shell in Mac machines.
Makes everything a bit easier from auto suggestions, completing tasks you do regularly considerably faster.
A shell designed for interactive use, although it is also a powerful scripting language

>sudo apt-get install zsh
>zsh

- https://www.zsh.org/
- https://www.howtogeek.com/362409/what-is-zsh-and-why-should-you-use-it-instead-of-bash/
- https://www.howtogeek.com/258518/how-to-use-zsh-or-another-shell-in-windows-10/

## Oh-My-Zsh 

most popular plugin framework for ZSH, and it comes with many built-in plugins and themes as well
- https://ohmyz.sh/   framework for managing your Zsh configuration
- https://www.howtogeek.com/362409/what-is-zsh-and-why-should-you-use-it-instead-of-bash/
>sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
>vi ~/.zshrc
> zsh --version


### Plugins
Enable a plugin by adding its name to the plugins array in your .zshrc file (found in the $HOME directory).
plugins=(rails git ruby)
Elements in zsh arrays are separated by whitespace (spaces, tabs, newlines...). DO NOT use commas.

ohmyzsh/plugins/npm/npm.plugin.zsh
```sh
(( $+commands[npm] )) && {
  rm -f "${ZSH_CACHE_DIR:-$ZSH/cache}/npm_completion"

  _npm_completion() {
    local si=$IFS
    compadd -- $(COMP_CWORD=$((CURRENT-1)) \
                 COMP_LINE=$BUFFER \
                 COMP_POINT=0 \
                 npm completion -- "${words[@]}" \
                 2>/dev/null)
    IFS=$si
  }
  compdef _npm_completion npm
}

# Install dependencies globally
alias npmg="npm i -g "
...

# Run npm start
alias npmst="npm start"

# Run npm test
alias npmt="npm test"

# Run npm scripts
alias npmR="npm run"

# Run npm publish 
alias npmP="npm publish"

# Run npm init
alias npmI="npm init"
```

 ### THEMES
https://github.com/ohmyzsh/ohmyzsh/wiki/Themes