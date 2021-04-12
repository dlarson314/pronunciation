import collections
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

def group_word(word, vowels={'a', 'e', 'i', 'o', 'u'}):
  endIndices = []
  vowels = {v.lower() for v in vowels}
  for i in range(len(word) - 1):
    isVowel0 = (word[i].lower() in vowels)
    isVowel1 = (word[i+1].lower() in vowels)
    if isVowel0 != isVowel1:
      endIndices.append(i+1)
  startIndices = [0] + endIndices
  endIndices.append(len(word))
  #print(startIndices)
  #print(endIndices)
  return [word[start:end] for start, end in zip(startIndices, endIndices)]

def foo5():
  print(group_word('scrabble'))
  print(group_word('supercalafragilisticexpialidocious'))

  word = re.sub('\d', '', 'EH0 M B AA1 R K').split()
  print(word)
  print(group_word(word, vowels={'EH', 'AA'}))

def foo6():
  cmulist = cmu.load_cmudict()
  cmudict = {word.upper(): (sounds, ipa) for word, sounds, ipa in cmulist}

  found = []
  missing = []
  with open('2of12.txt') as f:
    for line in f:
      word = line.strip().upper()
      if word not in cmudict:
        missing.append(word)
      else:
        found.append(word)
  print(len(missing), len(found))

  matched = []

  hist = collections.Counter()

  with open('2of12_found.txt', 'w') as f:
    for word in found:
      sounds, ipa = cmudict[word]
      f.write('%s\t%s\t/%s/\n' % (word,  ' '.join(sounds), ''.join(ipa)))

      word2 = re.sub('\W', '', word)
      groups0 = group_word(word2)
      sounds = [re.sub('\d', '', sound) for sound in sounds]
      groups1 = group_word(sounds, vowels=vowels)
      if len(groups0) != len(groups1):
        #print(word, groups0, groups1)
        pass
      else:
        matched.append(word)
        for english, sound in zip(groups0, groups1):
          hist[(english, tuple(sound))] += 1
  first = {key[0] for key in hist.keys()}
  second = {key[1] for key in hist.keys()}
  print('number of english groups: ', len(first))
  print('number of sound groups: ' , len(second))
  print('number of pairs: ' , len(hist))

  to_ipa = cmu.load_key()

  with open('sound_hist.txt', 'w') as f:
    pairs = list(hist.keys())
    pairs.sort()
    for word, sounds in pairs:
      ipa = [to_ipa[re.sub('\d', '', s)] for s in sounds]
      f.write('%5d\t%s\t/%s/\t%s\n' % (hist[(word, sounds)], word, ''.join(ipa), sounds))

  print(len(matched))





if __name__ == "__main__":
  #foo()
  #foo2()
  #foo3()
  #foo4()
  #foo5()
  foo6()


