# -*- coding: utf-8 -*-
'''
@author: 10873 Jorge Coveiro
@author: 12794 Carlos Rosário 
@date: 05-11-2012
@obs1: Este código foi copiado do site da biblioteca CSV para
ser possivel a escrita num ficheiro CSV quando os dados do
ficheiro XLS estão em unicode.
@obs2: Foi acrescentedo um "if isinstance(s,unicode) else s" a uma linha do 
UnicodeWriter pois estava a tentar codificar um float em utf-8, e isso 
estava a gerava um erro.
'''

import csv, codecs, cStringIO

class UTF8Recoder:
    """
    Iterator that reads an encoded stream and reencodes the input to UTF-8
    """
    def __init__(self, f, encoding):
        self.reader = codecs.getreader(encoding)(f)

    def __iter__(self):
        return self

    def next(self):
        return self.reader.next().encode("utf-8")

class UnicodeReader:
    """
    A CSV reader which will iterate over lines in the CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        f = UTF8Recoder(f, encoding)
        self.reader = csv.reader(f, dialect=dialect, **kwds)

    def next(self):
        row = self.reader.next()
        return [unicode(s, "utf-8") for s in row]

    def __iter__(self):
        return self

class UnicodeWriter:
    """
    A CSV writer which will write rows to CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8",**kwds):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, quoting=csv.QUOTE_NONNUMERIC,**kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
		self.writer.writerow([s.encode("utf-8") if isinstance(s,unicode) else s for s in row])
        # Fetch UTF-8 output from the queue ...
		data = self.queue.getvalue()
		data = data.decode("utf-8")
        # ... and reencode it into the target encoding
		data = self.encoder.encode(data)
        # write to the target stream
		self.stream.write(data)
        # empty queue
		self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)
