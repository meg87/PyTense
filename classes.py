#! /usr/bin/env python

import functions

class Tense(object):
	Subject = None
	Auxiliary = None
	Verb = None
	Object = None

	def print_all(self):
		print self.get_positive()
		print self.get_negative()
		print self.get_question()

# ---

class Simple(Tense):

	def set_simple(self):

		self.Auxiliary = "do"


class Continuous(Tense):
	def __init__(self):
		Auxiliary = "be"
		Verb = functions.add_suffix(Verb, "ing")

class Prefect(Tense):
	def __init__(self):
		Auxiliary = "have"
		Verb = functions.get_past_participle(Verb)

class PrefectContinuous(Tense):
	def __init__(self):
		Auxiliary = "have"
		Verb = functions.add_suffix(Verb, "ing")

# ---

class Present(Tense):

	def set_present(self):

		self.Auxiliary = functions.get_present_simple(self.Auxiliary, self.Subject)

		if self.Auxiliary == None:
			self.Verb = functions.get_present_simple(self.Verb, self.Subject)

class Past(Tense):
	def set_past(self):
		self.Auxiliary = functions.get_past_simple(self.Auxiliary)
		if self.Auxiliary == None:
			self.Verb = functions.get_past_simple(self.Verb)

class Future(Tense):
	def __init__(self):
		Auxiliary = "will"

# ---

class SimplePresent(Simple, Present):

	def __init__(self, s, v, o=""):

		self.Subject = s
		self.Verb = v
		self.Object = o
		self.set_simple()
		self.set_present()

	def get_positive(self):
		return "%s %s %s" % (self.Subject.capitalize(), self.Verb, self.Object)

	def get_negative(self):
		return "%s %s not %s %s" % (self.Subject.capitalize(), self.Auxiliary, self.Verb, self.Object)

	def get_question(self):
		return "%s %s %s %s?" % (self.Auxiliary.capitalize(), self.Subject, self.Verb, self.Object)



class SimplePast(Simple, Past):

	def __init__(self, s, v, o=""):

		self.Subject = s
		self.Verb = v
		self.Object = o
		self.set_simple()
		self.set_past()

	def get_positive(self):
		return "%s %s %s" % (self.Subject.capitalize(), self.Verb, self.Object)

	def get_negative(self):
		return "%s %s not %s %s" % (self.Subject.capitalize(), self.Auxiliary, self.Verb, self.Object)

	def get_question(self):
		return "%s %s %s %s?" % (self.Auxiliary.capitalize(), self.Subject, self.Verb, self.Object)
