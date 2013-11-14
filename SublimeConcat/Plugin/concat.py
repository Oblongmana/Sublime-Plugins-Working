import sublime_plugin
import sublime
import re
import os
from .Edit import Edit as Edit


class InsertCommand(sublime_plugin.TextCommand):
    def run(self, edit, pos, text):
        self.view.insert(edit, pos, text)

class ReplaceCommand(sublime_plugin.TextCommand):
    def run(self, edit, pos, text):
        self.view.replace(edit, pos, text)

class ConcatCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        window = view.window()
        region = sublime.Region(0, view.size())

        # path = '/'.join(self.view.file_name().split('/')[0:-1])
        path = os.path.dirname(self.view.file_name())
        # full_name = self.view.file_name().split('/')[-1]
        # filename = full_name.split('.')[-1]
        # file_name = '.'.join(full_name.split('.')[0:-1])
        # print(">>>>>> full_name= "+full_name)
        # print(">>>>>> EXT= "+filename)
        # print(">>>>>> sdfs= " + os.path.dirname(self.view.file_name()))

        print(">>>>>> import regex") 
        import_statement = '/{0,2}@import url\(\'(.+)\'\);'
        import_statement_loc = self.view.find(import_statement, 0)

        print(">>>>>> relpath regex") 
        relpath_regex = '/{0,2}@set relpath\(\'(.*)\'\);'
        relpath_loc = self.view.find(relpath_regex, 0)
        relpath_content = view.substr(relpath_loc)
        relpath_matches = re.search(relpath_regex, relpath_content)

        print(">>>>>> ext regex") 
        filename_regex = '/{0,2}@set filename\(\'(.+)\'\);'
        filename_loc = self.view.find(filename_regex, 0)
        content = view.substr(filename_loc)
        ext_matches = re.search(filename_regex, content)

        if ext_matches:
            filename = ext_matches.group(1)
        else:
            filename = 'output'

        if relpath_matches:
            relpath = relpath_matches.group(1)
        else:
            relpath = ''
        # print filename

        # print(">>>>>> import_statement_loc= " + import_statement_loc) 
        print(">>>>>> filename= " + filename)
        print(">>>>>> relpath= " + relpath)

        if import_statement_loc and filename and relpath:
            new_view = window.new_file()
            new_view.set_name(filename)
            region = sublime.Region(0, view.size())
            content = view.substr(region)

            try:
                syntax_file = self.view.settings().get('syntax')
                new_view.set_syntax_file(syntax_file)
            except KeyError:
                # print 'no syntax'
                pass

            # edit = new_view.begin_edit(new_view.view_id,'',None)
            # new_view.run_command('insert', {'pos': 0, 'text': content})
            with Edit(new_view) as edit:
                edit.insert(0, content);
            # new_view.insert(edit, 0, content)
            print(">>>>>>> "+new_view.name())
            # new_view.run_command('replace', {'pos': filename_loc, 'text': ''})
            
            with Edit(new_view) as edit:
                edit.replace(relpath_loc, '');

            with Edit(new_view) as edit:
                edit.replace(filename_loc, '');

            
            # new_view.replace(edit, filename_loc, '')

            import_statement_loc = new_view.find(import_statement, 0)
            while import_statement_loc:
                content = new_view.substr(import_statement_loc)
                m = re.search(import_statement, content)

                if m:
                    print(">>>>>> YO: "+m.group(1))
                    included = m.group(1)

                    try:
                        print(">>>>>> OPENING: " + os.path.join(path,relpath,included))
                        f = open(os.path.join(path,relpath,included),'rb')
                        file_content = f.read()
                        print(file_content)
                        decoded_content = file_content.decode("utf-8","replace") #unicode()
                        # encoded_content = file_content.encode("utf-8")
                        # new_view.run_command('replace', {'pos': import_statement_loc, 'text': encoded_content})
                        with Edit(new_view) as edit:
                            edit.replace(import_statement_loc, decoded_content);
                        # new_view.replace(edit, import_statement_loc, encoded_content)
                        f.close()
                    except IOError:
                        # print 'cannot open', included
                        raise

                import_statement_loc = new_view.find(import_statement, 0)

            # new_view.end_edit(edit)
            window.run_command("save")
