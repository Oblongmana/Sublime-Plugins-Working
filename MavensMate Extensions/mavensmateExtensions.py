import sublime,sublime_plugin, sys, os, time
sys.path.append(os.path.join(sublime.packages_path(), "MavensMate"))
import util

class NewApexPageAndControllerCommand(sublime_plugin.TextCommand):

    def run(self, edit): 
        sublime.active_window().show_input_panel("Visualforce Page Name (Controller will be named \"Controller_[VFPageName]\")", "", self.on_input, None, None)
    
    def on_input(self, input): 
        page_api_name = util.parse_new_metadata_input(input)
        page_options = {
            'metadata_type'     : 'ApexPage',
            'metadata_name'     : page_api_name
        }
        controller_api_name = 'Controller_' + page_api_name
        controller_options = {
            'metadata_type'     : 'ApexClass',
            'metadata_name'     : controller_api_name,
            'apex_class_type'   : 'default'
        }

        util.mm_call('new_metadata', params=page_options) 
        time.sleep(0.5) #mm seems to get stuck in an infinite (but unproductive) loop if there isn't a slight pause between commands
        util.mm_call('new_metadata', params=controller_options) 


class NewTestForCurrentFileCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        new_test_name = 'Test_' + os.path.basename(os.path.splitext(self.view.file_name())[0])
        sublime.active_window().show_input_panel("New test class Name", new_test_name, self.on_input, None, None)
    
    def on_input(self, input): 
        test_api_name = util.parse_new_metadata_input(input)
        test_options = {
            'metadata_type'     : 'ApexClass',
            'metadata_name'     : test_api_name,
            'apex_class_type'   : 'test'
        }

        util.mm_call('new_metadata', params=test_options)
