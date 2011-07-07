#! /usr/bin/env python

import functions

s = "he" # raw_input("Subject: ")
v = "write" # raw_input("Base verb: ")
o = "script" # raw_input("Object: ")

print "present simple:", functions.present_simple(s, v, o)
print "past simple:", functions.past_simple(s, v, o)
print "future simple:", functions.future_simple(s, v, o)

print "present continuous:", functions.present_continuous(s, v, o)
print "past continuous:", functions.past_continuous(s, v, o)
print "future continuous:", functions.future_continuous(s, v, o)

print "present prefect:", functions.present_prefect(s, v, o)
print "past prefect:", functions.past_prefect(s, v, o)
print "future prefect:", functions.future_prefect(s, v, o)

print "present perfect continuous:", functions.present_perfect_continuous(s, v, o)
print "past perfect continuous:", functions.past_perfect_continuous(s, v, o)
print "future perfect continuous:", functions.future_perfect_continuous(s, v, o)

#sentense = functions.SimplePast(s, v, o)

#sentense.print_all()

