# Introduction

These are some test scripts to investigate the CMU pronunciation dictionary.

See: http://www.speech.cs.cmu.edu/cgi-bin/cmudict

To obtain the dictionary file `cmudict-0.7b`, use for example:
```
wget http://svn.code.sf.net/p/cmusphinx/code/trunk/cmudict/cmudict-0.7b
```

# Rhyming Dictionary

By running `python main.py`, one can create a list of words,
`cmudict-0.7b.end_rhyme`, sorted in rhyming order.  This takes the individual
sounds in the word, reverses them, and sorts them.  Nearby words are more likely
to end in the same sequence of sounds (and possibly rhyme), and words farther
away in the list are less likely to rhyme.
