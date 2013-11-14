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

Define the dependencies using the @import syntax

CSS:
    
        @import url('bootstrap.min.css');
    
        body { background-color: #fff; }

JS:
    
        //@import url('jquery.min.js'); 
    
        $(document).ready(function(){
            console.log('ready');
        });

`Command + Shift + C` will concatenate all of the dependences into a new file: `{{filename}}.cat.{{extension}}`

Use with [YUI Compressor](https://github.com/leon/YUI-Compressor) and [SublimeOnSaveBuild](https://github.com/alexnj/SublimeOnSaveBuild) for automatic concat and minify

### Setup

TODO: Make this less specific to me? :)

WINDOWS: With the Sublime Text 3/Packages directory as your working directory, run the following in cmd with admin privileges to set up a symbolic link to the SublimeConcat plugin files for this repo. Could probs do as hard link too?
```
mklink /D SublimeConcat Drive:\path\to\repo\SublimeConcat\Plugin
```

Mac OSX: With the Sublime Text 3/Packages directory as your working directory, run the following in terminal to set up a hard link to the SublimeConcat plugin files for this repo
```
ln -n /path/to/repo/SublimeConcat/Plugin SublimeConcat
```
