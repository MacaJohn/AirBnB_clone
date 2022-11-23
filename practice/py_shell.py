#!/usr/bin/env python3

import cmd
import sys

class Simple_shell(cmd.Cmd):
    def parseline(self, line):
        ret = cmd.Cmd.parseline(self, line)
        return ret
    def emptyline(self):
        return cmd.Cmd.emptyline(self)
    def default(self, line):
        print('default(%s)' % line)
        return cmd.Cmd.default(self, line)
    def preloop(self):
        if not sys.stdin.isatty():
            line = sys.stdin.readline()
            self.cmdqueue.append(line)
#            sys.exit()
    def postloop(self):
        print()
    def do_greet(self, line):
        if line:
            print('hello,', line)
        else:
            print('hello')
    def do_EOF(self, line):
        return True
    def do_quit(self, line):
        sys.exit()

if __name__ == "__main__":
    Simple_shell().cmdloop('Playing with python cmd tool')
