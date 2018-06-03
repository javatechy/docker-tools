
Command+R setting in TEXTMATE
--------------

Bundles -> Edit Bundles -> Java -> Command+R and then change command

```
#!/bin/sh
#"$TM_BUNDLE_SUPPORT/bin/javamate.rb"
#./compile.sh
javac *.java
className="$(echo "$TM_FILEPATH"| rev| cut -d\/ -f1 | rev | cut -f 1 -d '.')"
# echo "=========OUTPUT========="
java $className
classToRemove="echo "$className.class""
rm -rf $classToRemove
```
