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


def foo3():
  to_ipa = load_key()

  phone_list = []
  with open('cmudict-0.7b', encoding='latin-1') as f:
    for line in f:
      if re.match(';;;', line):
        continue
      if re.search('  ', line):
        word, phones = line.split('  ')
        phones = phones.split()
        phone_list.append((phones[::-1], word, line))
  phone_list.sort()
  with open('cmudict-0.7b.end_rhyme', 'w') as f:
    for phones, word, line in phone_list:
      sounds = ' '.join(phones[::-1])
      ipa = [to_ipa[re.sub('\d', '', p)] for p in phones[::-1]]
      ipa = '/' + ''.join(ipa) + '/'
      #f.write(line.strip() + ' /' + ''.join(ipa) + '/\n')
      line = '%20s %50s %20s\n' % (word, sounds, ipa)
      f.write(line)

def foo4():
  to_ipa = load_key()

  phone_list = []
  with open('cmudict-0.7b', encoding='latin-1') as f:
    for line in f:
      if re.match(';;;', line):
        continue
      if re.search('  ', line):
        word, phones = line.split('  ')
        phones = phones.split()
        phone_list.append((phones, word, line))
      for letter in line:
        if ord(letter) > 127:
          print(line)
          break
  phone_list.sort()
  with open('cmudict-0.7b.front_rhyme', 'w') as f:
    for phones, word, line in phone_list:
      phones = [re.sub('\d', '', p) for p in phones]
      ipa = [to_ipa[p] for p in phones]
      line = '%20s %30s %20s\n' % (word, ' '.join(phones), ipa)
      f.write(line)



if __name__ == "__main__":
  #foo()
  #foo2()
  foo3()
  #foo4()

