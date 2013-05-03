import sublime, sublime_plugin

class InsertClipboardAsSnippetCommand(sublime_plugin.TextCommand):
    def run(self,edit):
        self.view.run_command('insert_snippet', {'contents': sublime.get_clipboard()})

