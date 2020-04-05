# Showing a meesage in popup

```
$wshell = New-Object -ComObject Wscript.Shell
$Output = $wshell.Popup("The report generation script is successfully completed!")
```

# Get all env variables

gci env:* | sort-object name

# Get a single env value

$env:ENV_VARIABLE_NAME
