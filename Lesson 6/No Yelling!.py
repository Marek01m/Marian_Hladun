def filter_words(st):
    return ' '.join((st[:1].upper()+st[1:].lower()).split())