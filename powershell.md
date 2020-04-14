## Showing a meesage in popup

```
$wshell = New-Object -ComObject Wscript.Shell
$Output = $wshell.Popup("The report generation script is successfully completed!")
```

## Get all env variables

```
gci env:* | sort-object name
```

## Get a single env value

```
$env:ENV_VARIABLE_NAME
```

## Robocopy in powershell

```
robocopy.exe /MT:64 /MIR E:\source_dir D:\destination_dir *.*
```

## Find Remove all content except the matching pattern line and find the unique

Below command will remove all lines which doesn't contain `ContentClass`

```
$SourceFile = 'response_all_items.json'
$Pattern = 'ContentClass'
(Get-Content $SourceFile) | Where-Object { $_ -match $Pattern } | Sort-Object | Get-Unique | Set-Content $SourceFile
```
