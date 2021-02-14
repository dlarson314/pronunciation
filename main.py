import collections
import re


def load_key():
  to_ipa = {}
  with open('key_v2.csv') as f:
    for line in f:
      tokens = line.split()
      to_ipa[tokens[0]] = tokens[1]
  return to_ipa

def foo():
  to_ipa = load_key()
  print(to_ipa)

def foo2():
  pairs = []
  with open('cmudict-0.7b', encoding='latin-1') as f:
    for line in f:
      if re.match(';;;', line):
        continue
      if re.search('  ', line):
        word, phones = line.split('  ')
        phones = phones.split()
        pairs += list(zip(phones[0:-1], phones[1:]))
        #print(phones.strip())

  print(len(pairs))
  hist = collections.Counter(pairs)
  print(len(hist))
  print(hist)



if __name__ == "__main__":
  #foo()
  foo2()
