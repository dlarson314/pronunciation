import re

def foo():
  phones = set()

  #with open('cmudict-0.7b.baseform') as f:
  with open('cmudict-0.7b.baseform', encoding="latin1") as f:
    for line in f:
      tokens = line.strip().split()
      for t in tokens[1:]:
        phones.add(t)

  print(phones)
  phones = list(phones)
  phones.sort()

  with open('20210109_phones.txt', 'w') as f:
    for phone in phones:
      f.write('%s\n' % phone)


def load_key():
  to_ipa = {}
  with open('key_v2.csv') as f:
    for line in f:
      tokens = line.split()
      to_ipa[tokens[0]] = tokens[1]
  return to_ipa


def foo2():
  to_ipa = load_key()
  print(to_ipa)


def foo3():
  to_ipa = load_key()
  with open('cmudict-0.7b.baseform_ipa', 'w') as out:
    with open('cmudict-0.7b.baseform', encoding="latin1") as f:
      for line in f:
        tokens = line.strip().split()
        ipa = ' '.join([to_ipa[phone] for phone in tokens[1:]])
        out.write(line.strip() + ' ----- ' + ipa + '\n')




if __name__ == "__main__":
  #foo()
  #foo2()
  foo3()

