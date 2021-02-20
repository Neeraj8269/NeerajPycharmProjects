#!/usr/lib/python3
"""Module to read out.log files formatted from LuxAtrumStudio/Pessum"""

import os
import sys
import re
import logreader.console as out

__time__ = False
__full__ = False

__type_width__ = 6
__msg_width__ = 9
__src_width__ = 8
__time_width__ = 6


class Entry:

    def __init__(self, type='NONE', msg='none', source='(none)', time=''):
        self.type = type
        self.msg = msg
        self.source = source
        self.time = time


def set_color(type):
    if type == 'FATAL':
        out.red_start()
        out.bold_start()
    elif type == 'ERROR':
        out.red_start()
    elif type == 'WARNING':
        out.yellow_start()
    elif type == 'TRACE':
        out.magenta_start()
    elif type == 'DEBUG':
        out.cyan_start()
    elif type == 'SUCCESS':
        out.green_start()
        out.bold_start()
    elif type == 'INFO':
        out.bold_start()
    elif type == 'DATA':
        out.blue_start()
    elif type == 'VERSION':
        out.yellow_start()
    elif type == 'NONE':
        out.grey_start()


def print_entry(entry):
    print('\u2502', end='')
    set_color(entry.type)
    print(
        ' {:^{type_width}s} '.format(entry.type, type_width=__type_width__),
        end='')
    out.reset()
    print('\u2502', end='')
    set_color(entry.type)
    print(
        ' {:^{msg_width}s} '.format(entry.msg, msg_width=__msg_width__), end='')
    out.reset()
    print('\u2502', end='')
    set_color(entry.type)
    print(
        ' {:^{src_width}s} '.format(entry.source, src_width=__src_width__),
        end='')
    out.reset()
    if __time__ is True:
        print('\u2502', end='')
        set_color(entry.type)
        print(
            ' {:^{time_width}s} '.format(entry.time, time_width=__time_width__),
            end='')
        out.reset()
    print('\u2502')


def print_top():
    print('\u2502', end='')
    print(
        out.bold(' {:^{width}s} '.format('Type', width=__type_width__)), end='')
    print('\u2502', end='')
    print(
        out.bold(' {:^{width}s} '.format('Message', width=__msg_width__)),
        end='')
    print('\u2502', end='')
    print(
        out.bold(' {:^{width}s} '.format('Source', width=__src_width__)),
        end='')
    if __time__ is True:
        print('\u2502', end='')
        print(
            out.bold(' {:^{width}s} '.format('Time', width=__time_width__)),
            end='')
    print('\u2502')
    print('\u251c', end='')
    print('\u2500' * (__type_width__ + 2), end='')
    print('\u253c', end='')
    print('\u2500' * (__msg_width__ + 2), end='')
    print('\u253c', end='')
    print('\u2500' * (__src_width__ + 2), end='')
    if __time__ is True:
        print('\u253c', end='')
        print('\u2500' * (__time_width__ + 2), end='')
    print('\u2524')


def set_size(entries):
    global __time__
    global __type_width__
    global __msg_width__
    global __src_width__
    global __time_width__
    for entry in entries:
        if len(entry.type) > __type_width__:
            __type_width__ = len(entry.type)
        if len(entry.msg) > __msg_width__:
            __msg_width__ = len(entry.msg)
        if len(entry.source) > __src_width__:
            __src_width__ = len(entry.source)
        if __time__ is True:
            if len(entry.time) > __time_width__:
                __time_width__ = len(entry.time)

    if __full__ is True:
        rows, cols = os.popen('stty size', 'r').read().split()
        cols = int(cols)
        total = __type_width__ + __msg_width__ + __src_width__ + 4
        if __time__ is True:
            total += __time_width__ + 1
        __type_width__ /= total
        __type_width__ = int(__type_width__ * cols)
        __msg_width__ /= total
        __msg_width__ = int(__msg_width__ * cols)
        __src_width__ /= total
        __src_width__ = int(__src_width__ * cols)
        if __time__ is True:
            __time_width__ /= total
            __time_width__ = int(__time_width__ * cols)


def print_entries(entries):
    if len(entries) == 0:
        print(out.bold(out.green("No Log Entries")))
    else:
        set_size(entries)
        print_top()
        for entry in entries:
            print_entry(entry)


def load_entries(file_name):
    lines = []
    if os.path.isfile(file_name) is False:
        print(out.bold(out.red("No file exsits at \"{}\"".format(file_name))))
    else:
        file = open(file_name, 'r')
        lines = file.readlines()
    entries = []
    global __time__
    for line in lines:
        segments = re.findall(r'(?<=\[)[^\]]*(?=\])', line)
        ent = Entry()
        if len(segments) == 0:
            ent = Entry()
        elif len(segments) == 1:
            ent = Entry(segments[0])
        elif len(segments) == 2:
            ent = Entry(segments[0], segments[1])
        elif len(segments) == 3:
            ent = Entry(segments[0], segments[1], segments[2])
        elif len(segments) == 4:
            __time__ = True
            ent = Entry(segments[0], segments[2], segments[3], segments[1])
        entries.append(ent)
    return entries


def main():
    global __full__
    file_name = "out.log"
    if len(sys.argv) > 1:
        if sys.argv[1] == '--full':
            __full__ = True
        else:
            file_name = sys.argv[1]
    if len(sys.argv) > 2:
        if sys.argv[2] == '--full':
            __full__ = True
    entries = load_entries(file_name)
    print_entries(entries)


if __name__ == "__main__":
    main()
