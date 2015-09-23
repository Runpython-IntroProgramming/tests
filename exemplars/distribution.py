import string
originaltext = input("Please enter a string of text (the bigger the better): ")
text = originaltext.lower()
counts = [text.count(c) for c in string.ascii_letters]  # build a list with character counts for a, b, c, etc..
pairs = list(zip(counts,string.ascii_letters))  # zip the counts together with the characters
pairs.sort(reverse=True)   # sort the zipped list of pairs so that biggest counts are first
charbars = [char*count for char,count in pairs]  # build a list of strings with correct # of chars
charbars = filter(lambda x : len(x)>0, charbars) # discard empty strings from the list
print ('The distribution of characters in "{0}" is: '.format(originaltext))
meta = []
# preparing to build a list of lists of charbars with same length
for bar in charbars:
    if len(meta) == 0 or len(bar) < len(meta[-1][0]):
        meta.append([bar])  # create new entry with a list of bar
    else:
        meta[-1].append(bar) # add this bar to the last list of bars
for charbarset in meta:
    charbarset.sort()
    for charbar in charbarset:
        print(charbar)
