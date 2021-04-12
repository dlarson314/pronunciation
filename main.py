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


def load_cmudict():
  to_ipa = load_key()

  sound_list = []
  with open('cmudict-0.7b', encoding='latin-1') as f:
    for line in f:
      if re.match(';;;', line):
        continue
      if re.search('  ', line):
        word, sounds = line.split('  ')
        sounds = sounds.split()
        ipa = [to_ipa[re.sub('\d', '', s)] for s in sounds]
        sound_list.append((word, sounds, ipa))
  return sound_list


def foo2_rhyme():
  cmulist = load_cmudict()

  # Sort in alphanumeric order of reversed sounds
  cmulist.sort(key=lambda x: x[1][::-1])
  with open('cmudict-0.7b.end_rhyme', 'w') as f:
    for word, sounds, ipa in cmulist:
      line = '%20s  %50s  %20s\n' % (word, ' '.join(sounds), '/'+''.join(ipa)+'/')
      f.write(line)

  # Sort in alphanumeric order of sounds
  cmulist.sort(key=lambda x: x[1])
  with open('cmudict-0.7b.front_rhyme', 'w') as f:
    for word, sounds, ipa in cmulist:
      line = '%20s  %50s  %20s\n' % (word, ' '.join(sounds), '/'+''.join(ipa)+'/')
      f.write(line)


def foo3():
  cmulist = load_cmudict()
  cmulist.sort(key=lambda x: x[1][::-1])

  old_suffix = ''
  rhyme_sets = []
  rhyme_set = []
  for word, sounds, ipa in cmulist:
    ipa = ''.join(ipa)
    suffix = re.sub('.* (\w+[12][^1]*)', r'\1', ' '.join(sounds))
    if suffix == old_suffix:
      rhyme_set.append(word)
    else:
      rhyme_sets.append(rhyme_set)
      if len(rhyme_set) > 500:
        print(len(rhyme_set), rhyme_set[0:5])
        print()
      rhyme_set = [word]

    old_suffix = suffix

  rhyme_sets.append(rhyme_set)

  hist = collections.Counter([len(s) for s in rhyme_sets])
  #print(hist)
  pairs = list(hist.items())
  pairs.sort()
  print(pairs)




if __name__ == "__main__":
  #foo()
  foo2_rhyme()
  #foo3()

