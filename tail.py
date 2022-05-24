import time
import os
def follow(thefile):
    '''generator function that yields new lines in a file
    '''
    # seek the end of the file
    thefile.seek(0, os.SEEK_END)
    # import ipdb; ipdb.set_trace()
    # start infinite loop
    while True:
        # read last line of file
        line = thefile.readline()
        # sleep if file hasn't been updated
        if not line:
            # print("in not line")
            time.sleep(0.1)
            continue
        # print("out of loop, near yield")
        yield line



def tail_last_ten(f, n, offset=None):
    """Reads a n lines from f with an offset of offset lines.  The return
    value is a tuple in the form ``(lines, has_more)`` where `has_more` is
    an indicator that is `True` if there are more lines in the file.
    """
    avg_line_length = 74
    to_read = n + (offset or 0)
    # import ipdb; ipdb.set_trace()
    while 1:
        try:
            f.seek(-(avg_line_length * to_read), 2)
        except IOError:
            # woops.  apparently file is smaller than what we want
            # to step back, go to the beginning instead
            f.seek(0)
        pos = f.tell()
        lines = f.read().splitlines()
        if len(lines) >= to_read or pos == 0:
            return lines[-to_read:offset and -offset or None]
        avg_line_length *= 1.3
    
    
if __name__ == '__main__':
    import os
    path_to_file = "/Users/praful/websockets/access.log"
    # stat = os.stat(path_to_file)
    # import ipdb; ipdb.set_trace()
    logfile = open("/Users/praful/websockets/access.log","rb")
    # print(next(tail_first_ten(logfile, 10)))
    print(tail_last_ten(logfile, 10))
    # logfile = open("/Users/praful/websockets/access.log","r")
    loglines = follow(logfile)
    # iterate over the generator
    print("aise hi kuch bhi")
    for line in loglines:
        print(line)

# logfile = open("/Users/praful/websockets/access.log","rb")
# print(next(tail_first_ten(logfile, 10)))