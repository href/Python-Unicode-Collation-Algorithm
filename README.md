Python Unicode Collation Algorithm (pyuca)
------------------------------------------

Originally developed by James Tauber this module provides a limited way of
sorting unicode strings in the way humans expect it.

I stumpled on this module while looking for a sorting solution for a Plone module. 
While pyuca is not as thorough as UCA it does sorting better than the default 
sorted function in Python and it does it without having to rely on the locale module, 
which is not very useful in a webserver environment as it isn't threadsafe.

In fact, the nice thing about pyuca is that it does not need to know about the
language of the text (unlike locale). It simply provides a sort function relying 
on the Default Unicode Collation Element Table.

I decided to put the module up on github as the original from the author's site
was down. I notified the author and I do not claim to have done any work :)

Installation
------------

Simply run `python setup.py install`

Usage
-----

1. Get the element table from the following link:

    [http://www.unicode.org/Public/UCA/latest/allkeys.txt](http://www.unicode.org/Public/UCA/latest/allkeys.txt)

2. Try it

        >>> words = [u'Cafe', u'Café', u'Caff']

        >>> from pyuca import Collator
        >>> c = Collator('allkeys.txt')

        # standard sort
        >>> sorted(words)
        >>> [u'Cafe', u'Caff', u'Café']

        # pyuca sort
        >>> sorted(words, key=c.sort_key)
        >>> [u'Cafe', u'Café', u'Caff']

More
----

Original post by James Tauber:

[http://jtauber.com/blog/2006/01/27/python_unicode_collation_algorithm/](http://jtauber.com/blog/2006/01/27/python_unicode_collation_algorithm/)