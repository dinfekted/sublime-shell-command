import sublime
import sublime_plugin

import os
import subprocess

class RunShellScript(sublime_plugin.TextCommand):
  def run(self, edit, command, args = []):
    path = os.path.dirname(self.view.file_name())
    for index, arg in enumerate(args):
      args[index] = arg.replace('$filename', self.view.file_name())

    subprocess.Popen([command] + args, stdout=subprocess.PIPE,
      stderr=subprocess.PIPE, cwd=path)