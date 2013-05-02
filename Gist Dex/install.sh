set -e
set -x
cd /Users/$USER/Library/Application\ Support/Sublime\ Text\ 2/Packages
mkdir "Gist Dex"
cd "Gist Dex"
curl -L "https://raw.github.com/Oblongmana/Sublime-Plugins-Working/master/Gist%20Dex/Default%20(Linux).sublime-keymap" -o "Default (Linux).sublime-keymap"
curl -L "https://raw.github.com/Oblongmana/Sublime-Plugins-Working/master/Gist%20Dex/Default%20(OSX).sublime-keymap" -o "Default (OSX).sublime-keymap"
curl -L "https://raw.github.com/Oblongmana/Sublime-Plugins-Working/master/Gist%20Dex/Default%20(Windows).sublime-keymap" -o "Default (Windows).sublime-keymap"
curl -L "https://raw.github.com/Oblongmana/Sublime-Plugins-Working/master/Gist%20Dex/Default.sublime-commands" -o "Default.sublime-commands"
curl -L "https://raw.github.com/Oblongmana/Sublime-Plugins-Working/master/Gist%20Dex/InsertClipboardAsSnippet.py" -o "InsertClipboardAsSnippet.py"

