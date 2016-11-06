import sys


def readlines(filename):
    with open(filename, 'r') as f:
        for line in f.readlines():
            yield line

def filter_gen(fn, lines):
    return (line for line in lines if fn(line))

def split(n, filename):
    lines = readlines(filename)
    i = 0
    collect = []
    for line in lines:
        if i+1 % n == 0:
            o_filename = "split-{0}".format((i//n)+1)
            print(o_filename)
            with open('split-output/' + o_filename, 'w') as f:
                for l in collect:
                    f.write(l)
        else:
            i += 1
            collect.append(line)


if __name__ == "__main__":
    params = sys.argv[1:]
    try:
        split(int(params[0]), params[1])
    except:
        raise

