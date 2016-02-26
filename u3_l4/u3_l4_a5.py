#!/usr/bin/python2
# -*- coding: utf-8 -*-

print 'i'.capitalize() # works
print 'i'.endswith('h')
print 'aba'.index('a')
print 'a2c'.isalpha()
print 'hey you'.find('y')
print 'hey you'.index('y')
print 'hey you'.islower()
print 'Hey you'.islower()
print '1'.isdigit()
print 'a'.isdigit()
print ' '.isspace()
print '_'.isspace()
print ' _'.isspace()
print '  '.isspace()
print 'What is Mathematics?'.istitle()
print 'What Is Mathematics?'.istitle()
print "UPPER CRUST".isupper()
print "UPPER CRUST".lower()
print "UPPER CRUST".lower().upper()
print "Too much right space     ".rstrip() +"|"
print "conjoined twins".split()
print "     left space".lstrip()
print "     left space    ".rstrip()+"|"
print "     left space    ".strip()+"|"
print "abracadabra".startswith("a")
print "foofoo".replace("f", "g")
print 'a\nb\nc\n'.split()
print 'a\nb\nc\n'.splitlines()
print 'aBcD'.swapcase()
print 'Hey {}, you {}'.format('you', 'fool')
print 'a tale of two cities'.title()

from string import maketrans
table = maketrans('cs', 'kz')
print 'this is an incredible test'.translate(table)
print 'it was many and many a year ago'.zfill(50)
print 'foofoo'.count('foo')
print 'expand\t'.expandtabs()+'|'
print 'test'.ljust(10)+'|'
print ''.join(['|', 'test'.rjust(10)])
print 'many and many a year ago'.partition(' ')
print 'many and many a year ago'.rpartition(' ')
print 'many and many'.rfind('y')
print 'many and many'.rindex('many')
print 'Albany and many'.rsplit('a', 1)
print '~'.center(20)