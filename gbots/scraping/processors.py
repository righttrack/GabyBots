import re
from gbots.util.loggers import getLogger

logger = getLogger(__name__)

__author__ = 'jeffmay'

class UnrecognizedProcessor(ValueError):
    pass

class IllegalProcessorCommand(ValueError):
    pass


def process(command, value):
    def combine_ending_backslashes(seq, next):
        last = seq.pop() if len(seq) > 0 else None
        if last is not None and last.endswith('\\'):
            seq.append("%s/%s" % (last, next))
        else:
            if last is not None:
                seq.append(last)
            seq.append(next)
        return seq
    chunks = reduce(combine_ending_backslashes, command.split('/'), [])
    try:
        processor, find, repl, flags = chunks
    except ValueError, e:
        logger.warning("Could not parse processor command: %s, expected %d unpacked %d" % (e, 4, len(chunks)))
        raise IllegalProcessorCommand(command, e)
    if processor == 's':
        # skipping flags for now
        return substitute(find, repl.replace("\/", "/"), value)
    else:
        raise UnrecognizedProcessor("Unrecognized processor: '%s'" % processor)


def substitute(find, replace, value):
    return re.sub(find, replace, value)