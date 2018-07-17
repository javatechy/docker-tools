# Setup a new MAC

- https://stackoverflow.com/questions/24342886/how-to-install-java-8-on-mac

### Text Editor Setup - Textmate

https://macromates.com/download


### Node Installation


```
brew install node
npm install -g sboot
npm install -g git-pull-all
```


### Terminal Setup

Add Following code in ~/.bash_profile

```
export PATH=$PATH:~/bin:~/Library/Python/3.6/bin
export PS1="\[\033[36m\]\u\[\033[m\]\[\033[33;1m\]\w\[\033[m\]\$ "
export CLICOLOR=1
export LSCOLORS=ExFxBxDxCxegedabagacad
alias ls='ls -GFh'
alias l='ls -lah'
alias r='sudo su'
alias test='sh ~/bin/test'
alias kuber='sh ~/bin/kuber'
alias prod='sh ~/bin/prod'
alias website='sh ~/bin/website'
alias c='clear'

```

###### **Reference**
 
* http://osxdaily.com/2013/02/05/improve-terminal-appearance-mac-os-x/
* https://draculatheme.com/terminal/
* https://ravingroo.com/1282/how-to-transparent-terminal-window-profile-mac-os-x/
