
### Git checkout remote branch

```
git fetch --all
git checkout --track origin/users/branch_name
```
### Git checkout a folder/dir

```
git checkout master -- dirname
```

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

### How to delete all your local branches but keep master
```
git branch | Select-String -NotMatch -Pattern "master" | %{ git branch -D $_.ToString().Trim() }
```
### Git take master to the some old date

SHA will be output of the first command
``
git rev-list -1 --before="2020-04-07 12:00" master
git checkout SHA
``

### Apply a Git patch(.diff/.patch file)

```
git apply --reject --whitespace=fix "C:\Users\path\Downloads\Sample.diff"
```

### Merge only few files from one branch into another

In this example we are taking changes from twitter_integration to master branch
```
$ git branch
* master
  twitter_integration

$ git checkout twitter_integration app/models/avatar.rb db/migrate/20090223104419_create_avatars.rb test/unit/models/avatar_test.rb test/functional/models/avatar_test.rb
```
https://jasonrudolph.com/blog/2009/02/25/git-tip-how-to-merge-specific-files-from-another-branch/
