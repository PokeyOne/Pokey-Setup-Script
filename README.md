# Pokey-Setup-Script
A programming language to help you setup a default workspace creation script

## How to run script
Once you have your script ready, just run the following command:
```
python /path/to/interpreter/PSSRunner.py /path/to/script.pss /path/to/workspace/
```

## Syntax of code
The syntax of the script is very simple. Each line is a seperate action, and each line has a command as the first word and the rest are arguments. 

### Basic commands

|Command|Description|Usage|
|---|---|---|
|`create`|creates a file|`create [path relative to workspace]`|
|`create`|creates a file with content|`create [path relative to workspace] with [text content]`|
|`createdir`|creates a directory|`createdir [path relative to workspace]`|
|`print`|print text to the console|`print [text message]`|
|`variable`|create a variable|`variable [name] [value]`|

### Example

```
# this line is commented
#this line is also commented
print starting setup for default web workspace
create emptyfile.txt
create index.html with <html>\n\t<p>\n\t\tthis is a cool file\n\t</p>\n</html>
createdir images
createdir scripts
createdir styles
print done seting-up your default web workspace
```
