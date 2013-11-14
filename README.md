#Sublime Plugins - Working

##Gist Dex Plugin Usage

###Commands Added

Super+Ctrl+V : Paste the current contents of the clipboard as though they were a snippet, setting selection to the first placeholder


##Gist Dex Plugin Installation

To install, open a terminal and type 

    bash <(curl https://raw.github.com/Oblongmana/Sublime-Plugins-Working/master/Gist%20Dex/install.sh)


Note that this will probably only work on OSX, with a standard looking ST2 install.

Alternatively, clone the repo, and copy the Gist Dex folder into your ST2 packages folder.

## SublimeConcat

Forked from from https://github.com/marcneuwirth/SublimeConcat

Build an output file containing a list of dependencies

### Usage:

Define the dependencies using the @import syntax. Works on any type of file, on Windows and OSX, and in ST3. 

**Importing Files:** Use `@import url('path/to/file.ext')` to import a file

**Output Filename:** Use `@set filename('filename.ext')` to set the output filename

**Relative Path:** Use `set relapth('relative/path')` to set the path to import `@import`s from, relative to the build file you are executing SublimeConcat on

### Setup

TODO: Make this less specific to me? :)

**WINDOWS**: With the Sublime Text 3/Packages directory as your working directory, run the following in cmd with admin privileges to set up a symbolic link to the SublimeConcat plugin files for this repo. Could probs do as hard link too?
```
mklink /D SublimeConcat Drive:\path\to\repo\SublimeConcat\Plugin
```

**Mac OSX**: With the Sublime Text 3/Packages directory as your working directory, run the following in terminal to set up a hard link to the SublimeConcat plugin files for this repo
```
ln -n /path/to/repo/SublimeConcat/Plugin SublimeConcat
```
