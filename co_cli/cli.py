#!/usr/bin/env python
# -*- coding: utf-8 -*-

from boscli import interpreter as interpreter_module, basic_types
from boscli.command import Command
import readlinecli
from co import factory, errors

class CliUseCases(object):
	def __init__(self, user_service):
		self.user_service = user_service

	def register(self, nickname):
		print "Register", nickname
		try:
			self.user_service.register(nickname)
		except errors.UserAlreadyRegisteredError:
			print "Already registered"

	def followers_for(self, nickname):
		print nickname
		followers = self.user_service.followers_for(nickname)
		if len(followers) > 0:
			print "followers:"
			for follower in followers:
				print "\t", follower
		else:
			print "No followers"

	def add_follower(self, nickname, follower):
		print "Adding {} as follower of {}".format(follower, nickname)
		self.user_service.add_follower(nickname, follower)

	def add_co(self, nickname, co):
		print "Adding co"
		self.user_service.add_co(nickname, co)

	def cos_for(self, nickname):
		print nickname
		cos = self.user_service.cos_for(nickname)
		if len(cos) > 0:
			print "cos:"
			for co in cos:
				print "\t", co
		else:
			print "No cos"



def main():
	interpreter = interpreter_module.Interpreter(prompt="co_cli")
	use_cases = CliUseCases(factory.create_user_service())

	interpreter.add_command(
		Command(['register', basic_types.StringType(name='nickname')],
				lambda *args, **kwargs: use_cases.register(*args),
				help="register a new user"))

	interpreter.add_command(
		Command(['add', 'follower', basic_types.StringType(name='follower'), 'to', basic_types.StringType(name='nickname')],
				lambda follower, nickname, *args, **kwargs: use_cases.add_follower(nickname, follower),
				help="add a follower to a registered user"))

	interpreter.add_command(
		Command(['show', 'followers', 'for', basic_types.StringType(name='nickname')],
				lambda nickname, *args, **kwargs: use_cases.followers_for(nickname),
				help="show follwers"))

	interpreter.add_command(
		Command(['show', 'cos', 'for', basic_types.StringType(name='nickname')],
				lambda nickname, *args, **kwargs: use_cases.cos_for(nickname),
				help="show cos"))

	interpreter.add_command(
		Command(['add', 'co', basic_types.StringType(name='co'), 'to', basic_types.StringType(name='nickname')],
				lambda co, nickname, *args, **kwargs: use_cases.add_co(nickname, co),
				help="add a co to a registered user"))

	readlinecli.ReadlineCli(interpreter).interact()

if __name__ == '__main__':
	main()
