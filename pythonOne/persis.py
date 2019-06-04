"""
created on 5/28/19
"""
### Imports
from . import program as p
### Functions
def save_setting(key, value):
    if p.current_program.lang == "py":
        p.current_program.add("settings = {}")
        p.current_program.add("try:")
        p.current_program.indent += 1
        p.current_program.add("with open('settings.pkl', 'rb') as settings_file:")
        p.current_program.indent += 1
        p.current_program.add("settings = pickle.load(settings_file)")
        p.current_program.indent -= 2
        p.current_program.add("except Exception:")
        p.current_program.indent += 1
        p.current_program.add("settings = {}")
        p.current_program.indent -= 1
        p.current_program.add("settings[" + key + "] = " + value)
        p.current_program.add("with open('settings.pkl', 'wb') as settings_file:")
        p.current_program.indent += 1
        p.current_program.add("pickle.dump(settings, settings_file)")
        p.current_program.indent -= 1
    if p.current_program.lang == "cs":
        if not ("ui" in p.current_program.options):
            raise ValueError("'ui' must be in options")
        p.current_program.add("ApplicationDataContainer localSettings = Windows.Storage.ApplicationData.Current.LocalSettings;")
        p.current_program.add("localSettings.Values[" + key + "] = " + value + ";")
def load_setting(key, var, default_value='""'):
    if p.current_program.lang == "py":
        p.current_program.add("try:")
        p.current_program.indent += 1
        p.current_program.add("with open('settings.pkl', 'rb') as settings_file:")
        p.current_program.indent += 1
        p.current_program.add(var + " = pickle.load(settings_file)[" + key + "]")
        p.current_program.indent -= 2
        p.current_program.add("except Exception:")
        p.current_program.indent += 1
        p.current_program.add(var + " = " + default_value)
        p.current_program.indent -= 1
    if p.current_program.lang == "cs":
        p.current_program.add("try {")
        p.current_program.indent += 1
        p.current_program.add("ApplicationDataContainer localSettings = Windows.Storage.ApplicationData.Current.LocalSettings;")
        p.current_program.add(var + " = localSettings.Values[" + key + "] as string;")
        p.current_program.indent -= 1
        p.current_program.add("catch (Exception e) {")
        p.current_program.indent += 1
        p.current_program.add(var + " = " + default_value)
        p.current_program.indent -= 1
        p.current_program.add("}")