#! /usr/bin/env python

import string

past_simple_verb = {"do":"did", "have":"had", "is":"was", "am":"was", "are":"were", "write":"wrote"}
past_participle_verb = {"do":"done", "is":"been", "am":"been", "are":"been", "have":"had", "write":"written"}

def present_simple(s, v, o=""):
	return "%s %s %s." % (s.capitalize(), get_present_simple(v, s), o)

def past_simple(s, v, o=""):
	return "%s %s %s." % (s.capitalize(), get_past_simple(v), o)

def future_simple(s, v, o=""):
	return "%s will %s %s." % (s.capitalize(), v, o)

def present_continuous(s, v, o=""):
	return "%s %s %s %s." % (s.capitalize(), get_base_be(s), add_suffix(v, "ing"), o)

def past_continuous(s, v, o=""):
	return "%s %s %s %s." % (s.capitalize(), get_past_be(s), add_suffix(v, "ing"), o)

def future_continuous(s, v, o=""):
	return "%s will be %s %s." % (s.capitalize(), add_suffix(v, "ing"), o)

def present_prefect(s, v, o=""):
	return "%s %s %s %s." % (s.capitalize(), get_base_have(s), get_past_participle(v), o)

def past_prefect(s, v, o=""):
	return "%s had %s %s." % (s.capitalize(), get_past_participle(v), o)

def future_prefect(s, v, o=""):
	return "%s will %s %s %s." % (s.capitalize(), get_base_have(s), get_past_participle(v), o)

def present_perfect_continuous(s, v, o=""):
	return "%s %s been %s %s." % (s.capitalize(), get_base_have(s), add_suffix(v, "ing"), o)

def past_perfect_continuous(s, v, o=""):
	return "%s had been %s %s." % (s.capitalize(), add_suffix(v, "ing"), o)

def future_perfect_continuous(s, v, o=""):
	return "%s will %s been %s %s." % (s.capitalize(), get_base_have(s), add_suffix(v, "ing"), o)


def is_transitive(verb):
	if verb in ("bring", "buy", "cost", "get", "give", "leave", "lend", "make", "offer", "owe", "pass", "pay", "play", "promise", "read", "refuse", "send", "show", "sing", "take", "teach", "tell", "write"): 
		return True
	else:
		False

def is_singular(subject): # rewrite it!
	if subject.lower() in ("i", "you", "he", "she", "it"): 
		return True
	elif subject.lower() in ("we", "they") or subject.endswith("s") or subject.endswith("es"):
		False

def is_plural(subject): # rewrite it!
	if subject.lower() in ("i", "you", "he", "she", "it"): 
		return True
	elif subject.lower() in ("we", "they") or subject.endswith("s") or subject.endswith("es"):
		False

def get_base_be(subject):
	if subject.lower() in ("i"):
		return "am"
	elif subject.lower() in ("he", "she", "it") or is_singular(subject): 
		return "is"
	elif subject.lower() in ("we", "you", "they") or is_plural(subject):
		return "are"

def get_past_be(subject):
	if subject.lower() in ("i", "you", "he", "she", "it") or is_singular(subject): 
		return "was"
	elif subject.lower() in ("we", "they") or is_plural(subject):
		return "were"

def get_base_have(subject):
	if subject.lower() in ("i", "we", "you", "they"):
		return "have"
	elif subject.lower() in ("he", "she", "it") or is_singular(subject): 
		return "has"

def add_suffix(word, suffix):

	if (suffix == "ing" or suffix == "ed" or suffix == "er") and word.endswith("c"):
		return "%sk%s" % (word, suffix)
	elif (suffix == "ing" or suffix == "ed") and is_vowel(word[len(word)-3:len(word)-2]) == False and is_vowel(word[len(word)-2:len(word)-1]) and is_vowel(word[len(word)-1:len(word)]) == False:
		return "%s%s%s" % (word, word[len(word)-1:len(word)], suffix)
	elif suffix == "ing" and word.endswith("ie"):
		return "%sying" % (word[0:len(word)-2])
	elif (suffix == "ing" or suffix == "ed") and word.endswith("e"):
		return "%s%s" % (word[0:len(word)-1], suffix)
	elif suffix == "ed" and word.endswith("ie"):
		return "%sd"
	elif suffix == "s" and (word.endswith("s") or word.endswith("x") or word.endswith("z") or word.endswith("ch") or word.endswith("sh") or word.endswith("o")):
		return "%ses" % word
	elif suffix == "s":
		return "%s%s" % (word, suffix)

def get_end_of(word):
	return string.count(word, 1, len(word)-1)

def is_vowel(char):
	if char.lower() in ('a', 'e', 'i', 'o', 'u'):
		return True
	else:
		return False

def is_irregular(verb):
	if verb.lower() in past_simple_verb:
		return True
	else:
		return False

def get_past_simple(verb):
	if is_irregular(verb):
		return past_simple_verb[verb.lower()]
	else:
		return add_suffix(verb, "ed")

def get_past_participle(verb):
	if is_irregular(verb):
		return past_participle_verb[verb.lower()]
	else:
		return add_suffix(verb, "ed")

def get_present_simple(verb, subject):
	if subject.lower() in ("he", "she", "it"):
		return add_suffix(verb, "s")
	else:
		return verb

# ---

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
		Verb = add_suffix(Verb, "ing")

class Prefect(Tense):
	def __init__(self):
		Auxiliary = "have"
		Verb = get_past_participle(Verb)

class PrefectContinuous(Tense):
	def __init__(self):
		Auxiliary = "have"
		Verb = add_suffix(Verb, "ing")

# ---

class Present(Tense):

	def set_present(self):

		self.Auxiliary = get_present_simple(self.Auxiliary, self.Subject)

		if self.Auxiliary == None:
			self.Verb = get_present_simple(self.Verb, self.Subject)

class Past(Tense):
	def set_past(self):
		self.Auxiliary = get_past_simple(self.Auxiliary)
		if self.Auxiliary == None:
			self.Verb = get_past_simple(self.Verb)

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
