### git move uncommitted changes to existing branch

```
git stash
git checkout other-branch
git stash pop
```

### Merge a branch into your current branch

```
git merge master
```
And resolve the conflicts one by one shown after above merging command.

### Overwrite single file in my current branch with the same file in the master branch

```
git checkout master path/to/default.aspx.cs

```
So, just `git checkout FROM_BRANCH_NAME path/to/file`

### Git Get the last commits

```
git log
git log --oneline
```
