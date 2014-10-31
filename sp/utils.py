# -*- coding: utf-8 -*-
from django.utils.encoding import force_unicode

# utils
def transliterate(text):
    TRANS_MAP = { u'а':'a', u'б':'b', u'в':'v', u'г':'g', u'д':'d', u'е':'e', u'ё':'e', u'ж':'zh',
              u'з':'z', u'и':'i', u'й':'i', u'к':'k', u'л':'l', u'м':'m', u'н':'n', u'о':'o',
              u'п':'p', u'р':'r', u'с':'s', u'т':'t', u'у':'u', u'ф':'f', u'х':'h', u'ц':'ts',
              u'ч':'ch', u'ш':'sh', u'щ':'sch', u'ъ':'j', u'ы':'y', u'ь':'j', u'э':'e', u'ю':'yu',
              u'я':'ya', u' ':'-', u'_':'_', u'№': '', u'"': '', u'\'': '', u'«': '', u'»': ''}

    if not isinstance(text, unicode):
        text = force_unicode(text)
    text = text.lower()
    retval = []
    for t in text:
        translation = TRANS_MAP.get(t,None)
        if translation is not None:
            retval += translation
        else:
            retval += t
    retval = "".join(retval)
    return retval
