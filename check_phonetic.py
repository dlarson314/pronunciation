import re

import main as cmu

vowels = set(('AA', 'AE', 'AH', 'AO', 'AW', 'AY', 'EH', 'ER', 'EY', 'IH', 'IY', 'OW', 'OY', 'UH', 'UW'))

def foo():
  cmulist = cmu.load_cmudict()
  for i in range(10):
    print(cmulist[i])

def remove_vowels(string):
  if type(string) == str:
    return re.sub('[AEIOU\W\d]', '', string)
  elif type(string) == list:
    newlist = [re.sub('\d', '', s) for s in string]
    newlist = [s for s in newlist if s not in vowels]
    return tuple(newlist)
  else:
    assert(False)


def consontants1(sounds):
  mymap = {'B': 'B', 'CH': 'CH', 'D': 'D',
           'DH': 'TH',
           'ER': 'R',   # ɝ  hurt
           'F': 'F', 'G': 'G', 'HH': 'H',
           'JH': 'J',
           'K': 'C', 'L': 'L', 'M': 'M', 'N': 'N',
           'NG': 'NG',
           'P': 'P', 'R': 'R', 'S': 'S', 'SH': 'SH',
           'T': 'T', 'TH': 'TH', 'V': 'V', 'W': 'W',
           'Y': 'Y', 'Z': 'Z', 'ZH': 'Z'}
  out = []
  for sound in sounds:
    if sound in mymap:
      out.append(mymap[sound])
    newlist = [re.sub('\d', '', s) for s in string]

  return out

def foo2():
  correct = 0
  wrong = 0
  cmulist = cmu.load_cmudict()
  #for i in range(100,200):
  for i in range(len(cmulist)):
    word, pronunciation, ipa = cmulist[i]
    #print(word, pronunciation)
    simple_word = remove_vowels(word)
    sounds = remove_vowels(pronunciation)
    guess = ''.join(consontants1(sounds))
    if guess == simple_word:
      correct += 1
    else:
      wrong += 1
      print(word, simple_word, guess, sounds)
  print('number correct: ', correct)
  print('number wrong:   ', wrong)


def foo3():
  cmulist = cmu.load_cmudict()
  vowel_counter = {}

  for i in range(len(cmulist)):
    word, pronunciation, ipa = cmulist[i]
    newlist = [re.sub('\d', '', s) for s in pronunciation]
    if (len(newlist) == 3) and (newlist[1] in vowels):
      middle = newlist[1]
      key = (newlist[0], newlist[2])
      if key in vowel_counter:
        vowel_counter[key].add(middle)
      else:
        vowel_counter[key] = set([middle])
      if key == ('K', 'L'):
        print(word, pronunciation, ipa)

  pairs = [(len(vowel_counter[key]), key) for key in vowel_counter.keys()]
  pairs.sort(reverse=True)
  for i in range(10):
    print(pairs[i])


def foo4():
  cmulist = cmu.load_cmudict()
  vowel_counter = {}
  for i in range(len(cmulist)):
    word, pronunciation, ipa = cmulist[i]
    newlist = [re.sub('\d', '', s) for s in pronunciation]
    key = tuple([re.sub('\w+\d', 'vowel', s) for s in pronunciation])
    #key = remove_vowels(pronunciation)
    vowels = set(newlist) - set(key)
    if key in vowel_counter:
      vowel_counter[key].update(vowels)
    else:
      vowel_counter[key] = set(vowels)
    #if key == ('P', 'vowel', 'L', 'vowel'):
    #if key == ('T', 'vowel', 'K', 'vowel'):
    #if key == ('K', 'vowel', 'N', 'Z'):
    if key == ('vowel', 'L'):
    #if key == ('T', 'R', 'N'):
    #if key == ('T', 'R'):
      print(word, pronunciation, ipa)


  pairs = [(len(vowel_counter[key]), key) for key in vowel_counter.keys()]
  pairs.sort(reverse=True)
  for i in range(100):
    print(pairs[i])



if __name__ == "__main__":
  #foo()
  #foo2()
  #foo3()
  foo4()


