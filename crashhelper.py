"""
 Written by Daniel Sungju Kwon
"""

from __future__ import print_function
from __future__ import division

from pykdump.API import *
from os.path import expanduser
import os
import sys


def run_gdb_command_with_file(command, file_content):
    """exec_gdb_command() is failing to capture the output
    if the command is with '!' which is important to execute
    shell commands. Below will capture it properly."""
    try:
        temp_output_name = expanduser("~") + "/" + time.strftime("%Y%m%d-%H%M%S-pycrashext-output-tmp")
        temp_input_name = expanduser("~") + "/" + time.strftime("%Y%m%d-%H%M%S-pycrashext-input-tmp")
        command = command + " > " + temp_output_name
        if file_content != "":
            with open(temp_input_name, 'w') as f:
                f.write(file_content)
            command = command + " < " + temp_input_name

        exec_gdb_command(command)
        lines = ""
        if os.path.exists(temp_output_name):
            with open(temp_output_name, 'r') as f:
                try:
                    lines = "".join(f.readlines())
                except:
                    lines = "Failed to read " + temp_output_name

        try:
            os.remove(temp_output_name)
            os.remove(temp_input_name)
        except:
            pass
    except Exception as e:
        lines = str(e)

    return lines


def run_gdb_command(command):
    return run_gdb_command_with_file(command, "")