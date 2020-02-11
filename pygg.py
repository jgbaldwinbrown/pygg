#!/usr/bin/env python3

import subprocess
import pandas as pd

def ggplot(data_frame, command):
    proc = subprocess.Popen(
        [
            "ggplotit",
            command
        ],
        stdin=subprocess.PIPE
    )
    proc.communicate(input = data_frame.to_csv(sep="\t", index=None).encode('utf-8'))

def main():
    # quick test of ggplot
    # should only run if not loading as a library
    
    a = pd.DataFrame({"b": [1,2,3], "c": [4,5,6]})
    command = """
    pdf("test_out.pdf", height=3, width=4)
    print(ggplot(data=data, aes(b, c)) + geom_point())
    dev.off()
    """
    ggplot(a, command)

if __name__ == "__main__":
    main()
