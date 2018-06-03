# Remove old logs

```
find . -type f -name '*' -mtime +1 -exec rm {} \;
```

# Check disk space
```
df -H
```


# top 10 dirs in linux 
```
du -hs / | sort -n -r | head -n 10
```


# Checkout develop branch recurisvly

```
for d in ./*/ ; do (cd "$d" && git checkout develop); done

for d in ./*/ ; do (cd "$d" && git pull --all); done
```

# Delete old logs - older than one day

```
for d in ./*/ ; do (cd "$d/logs" && find . -type f -name '*' -mtime +1 -exec rm {} \; ); done
```

# Recently updated files

```
find . -type f -printf '%TY-%Tm-%Td %TT %p\n' | sort -r
```

# Check who created a branch

```
git for-each-ref --format='%(color:cyan)%(authordate:format:%m/%d/%Y %I:%M %p)    %(align:25,left)%(color:yellow)%(authorname)%(end) %(color:reset)%(refname:strip=3)' --sort=authordate refs/remotes
```