
###Create a file .bash_profile in /Users/username

```
export PATH=$PATH:~/bin:~/Library/Python/3.6/bin
alias l='ls -lah'
alias r='sudo su'
alias test='sh ~/bin/test'
alias kuber='sh ~/bin/kuber'
alias prod='sh ~/bin/prod'
alias website='sh ~/bin/website'
# Show always fullpath on terminal
export PS1='\u [\w]$ '
alias c='clear'
```


### DB Connection and tunnel
```
ssh -gL 5555:rds.amazonaws.com:5432 -i /Users/deepak/Documents/Keys/pemServer.pem username@129.19.15.111

ssh -g -i /Users/deepak/Documents/Keys/pemKey.pem ubuntu@192.12.2.34
```

### Pushing code to github
```
git push https://javatechy:password@github.com/javatechy/angular2-material --all
https://javatechy@bitbucket.org/javatechy/bws-client
```

## Remove unused mounts
```ls -alth
lsblk
file -s /dev/xvdg
```

