
INFILE = "index.html.in"
OUTFILE = "index.html"

def process(version):

    with open(INFILE, "r") as f:
        text = f.read()

    text %= {'version': version}

    with open(OUTFILE, "w") as f:
        f.write(text)


if __name__ == "__main__":
    import sys
    process(sys.argv[1])
