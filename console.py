#!/usr/bin/env python3

import cmd
import sys

class Simple_shell(cmd.Cmd):
    prompt = "(hbnb) "
    def __init__(self):
        super().__init__()
        self.line = None

    def parseline(self, line):
        ret = cmd.Cmd.parseline(self, line)
        return ret

    def emptyline(self):

        if self.lastcmd:
            self.lastcmd = ""
        return cmd.Cmd.emptyline(self)

    def default(self, line):
        print('default(%s)' % line)
        return cmd.Cmd.default(self, line)

#    def preloop(self):

    def precmd(self, line):
        print()
        return cmd.Cmd.precmd(self, line)

    def postloop(self):
        if not sys.stdin.isatty():
            self.line = sys.stdin.readline()
        self.cmdqueue.append(self.line)

    def do_greet(self, line):
        if line:
            print('hello,', line)
        else:
            print('hello')

    def help_greet(self):
        print("Usage: greet [person]")

    def do_EOF(self, line):
        return True

    def help_EOF(self):
        print("Usage: ^D")

    def do_quit(self, line):
        sys.exit()

    def help_quit(self):
        print("Usage: quit")

if __name__ == "__main__":
    Simple_shell().cmdloop()
