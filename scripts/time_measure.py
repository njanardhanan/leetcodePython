#!/anaconda3/envs/py37/bin/python
import time


def time_it(f):

    def timed(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
        print ('Time taken : %2.2f sec' % (te-ts))
        #print ('%r (%r, %r) %2.2f sec' % \
        #      (f.__name__, args, kw, te-ts))
        return result

    return timed
