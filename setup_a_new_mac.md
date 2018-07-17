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


# ** OR **
 
```
export PATH=$PATH:~/bin:~/Library/Python/3.6/bin
export CLICOLOR=1
#export LSCOLORS=GxFxCxDxBxegedabagaced
alias l='ls -lah'
alias r='sudo su'
alias test='sh ~/bin/test'
alias kuber='sh ~/bin/kuber'
alias website='sh ~/bin/website'
alias mci="mvn clean install -DskipTests=true"
alias mee="mvn eclipse:eclipse"
alias mbr="mvn spring-boot:run"
alias prod='sh ~/bin/prod'
alias jump="sshpass -p 'bhS;<=sL)+g3-2Ee' ssh -gL 5555:localhost:3306  -gL 7030:localhost:8030 deepak@jumpserver.fabhotels.com"
alias cassjump="sshpass -p 'bhS;<=sL)+g3-2Ee' ssh -gL 8081:localhost:8080  deepak@13.127.109.95"
#alias prod="sshpass -p '=ajW,dj}L2qU9="B' ssh dkumar@ec2-35-154-208-175.ap-south-1.compute.amazonaws.com"
alias doctool="ssh -i ~/ssh/i27^poriginal_distr.pem ubuntu@35.154.206.110"
# Show always fullpath on terminal
#export PS1='\u [\w]$ '
alias c='clear'
export PS1="\[\033[36m\]\u\[\033[m\]:\[\033[33;1m\]\w\[\033[m\]\$ "
export LSCOLORS=ExFxBxDxCxegedabagacad
alias tomcat='cd /Users/deepak/softwares/tomcat/bin/'
alias log='cd /var/log/casa'
alias script='cd /Users/deepak/projects/scripts/'
alias code='cd /Users/deepak/projects'
alias prop='cd /usr/local/casa/properties/'
alias jmeter="sh ~/softwares/jmeter/bin/jmeter"
alias tree="find . -print | sed -e 's;[^/]*/;|____;g;s;____|; |;g'"
alias python=python3
alias gpa="git-pull-all"
source ~/.profile
[[ -s "$HOME/.rvm/scripts/rvm" ]] && source "$HOME/.rvm/scripts/rvm" # Load RVM into a shell session *as a function*
export JAVA_HOME=`/usr/libexec/java_home -v 1.8.0_144, x86_64`
export JAVA_HOME=`/usr/libexec/java_home -v 1.8.0_144, x86_64`
```

Use monokai theme https://github.com/stephenway/monokai.terminal

###### **Reference**
 
* http://osxdaily.com/2013/02/05/improve-terminal-appearance-mac-os-x/
* https://draculatheme.com/terminal/
* https://ravingroo.com/1282/how-to-transparent-terminal-window-profile-mac-os-x/
