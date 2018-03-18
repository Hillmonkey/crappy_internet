#!/usr/bin/python3

'''This file contains things-to-do, aka functions that can be triggered by
an http request hitting the get-server program'''

import datetime
from file_access import reversed_lines

# fname = "time_stamps.txt"


def append_timestamp(fname):
    '''append timestamp to a file full of timestamps!
    '''
    json_time = datetime.datetime.now()
    with open(fname, mode='a+', encoding='utf-8') as f:
        # go to prev last line
        prev_time = next(islice(reversed_lines(f), 1))
        # subtract prev_time from now, to the nearest minute
        # deal with rounding, import relative time?
        # every minute that is missing is a minute where no connectivity
        # was detected.
        # for minute_offset in range(minutes-missed):
        #     # create crappy_time = timestamp - minute_offset
        #      # f.write('[crappy]' + str(crappy_time) + '\n')
        # Question: does with-context carry to the subroutine above?
        f.write('[good]:' + str(json_time) + '\n')


if __name__ == "__main__":
    pass
