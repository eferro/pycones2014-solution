# -*- coding: utf-8 -*-

import os
import readline
import atexit
import boscli


import logging
LOG_FILENAME = '/tmp/completer2.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG,)




class ReadlineCli(object):

    def __init__(self, interpreter):
        self.interpreter = interpreter
        self.init_history()
        self.init_readline()

    def init_readline(self):
        readline.parse_and_bind("tab: complete")
        readline.set_completer(self.complete)
        readline.parse_and_bind("set bell-style none")
        readline.parse_and_bind("set show-all-if-ambiguous")
        readline.parse_and_bind("set completion-query-items -1")
        readline.set_completer_delims(' \t\n')

    def init_history(self):
        histfile=os.path.expanduser("~/.aleacli_history")
        try:
            readline.read_history_file(histfile)
        except IOError:
            pass
        atexit.register(self._save_history, histfile)

    def _save_history(self, histfile):
        readline.write_history_file(histfile)

    def completions_without_duplicates(self, line):
        completions = self.interpreter.complete(line)
        completions_with_spaces = [completion for completion in completions if completion.endswith(' ')]
        completions_without_spaces = [completion for completion in completions if not completion.endswith(' ')]

        results = completions_without_spaces
        for completion in completions_with_spaces:
            if completion.strip() not in results:
                results.append(completion)
        return results

    def complete(self, prefix, index):
        try:
            line = readline.get_line_buffer()

            response = None
            if index == 0:
                # This is the first time for this text, so build a match list.
                self.completions = self.completions_without_duplicates(line)
                logging.debug('{} matches: {}'.format(line, self.completions))

            # Return the state'th item from the match list,
            # if we have that many.
            try:
                response = self.completions[index]
            except IndexError:
                response = None
            logging.debug('complete(%s, %s) => %s', repr(prefix), index, repr(response))
            return response
        except Exception as exc:
            import traceback
            traceback.print_exc()
            print "ERROR", exc


    def interact(self):
        while True:
            try:
                line = raw_input(self.interpreter.prompt + '>')
                if line.endswith('?'):
                    line = line[:-1]
                    commands_help = self.interpreter.help(line.strip())
                    for command_str in sorted(commands_help.keys()):
                        print str(command_str), ' ==> ', commands_help[command_str]
                else:
                    val = self.interpreter.eval(line)
                    if val is not None:
                        print str(val)
            except boscli.exceptions.NotMatchingCommandFoundError:
                print "Not matching command found"
            except boscli.exceptions.AmbiguousCommandError as exc:
                print "Ambigous command"
                for command in exc.matching_commands:
                    print "\t", command
            except (boscli.exceptions.EndOfProgram, EOFError, KeyboardInterrupt):
                print "Exit"
                break
