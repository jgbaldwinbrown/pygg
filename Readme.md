# pygg

A python3 wrapper for R's ggplot2

# Installation

1. Copy ggplotit.R into a directory that has been added to your PATH. For example:
```sh
export PATH=$PATH:~/mybin
cp ggplotit.R ~/mybin
```

2. add this directory to your PYTHONPATH. For example:
```sh
export PYTHONPATH=$PYTHONPATH:`pwd`
```

# Usage

This package allows you to write arbitrary R code in a text string in python3 source code,
then call that in R for plotting purposes. For example:

```python
#/usr/bin/env python3

import pygg
import pandas as pd

my_data = pd.DataFrame({"Fruit": ["apple", "apple", "apple", "banana", "banana", "banana"],
    "Day": [1, 2, 3, 1, 2, 3],
    "Number": [55, 66, 77, 38, 36, 35]
})

my_command = """
pdf("fruits_by_day.pdf", height=3, width=4)
print(ggplot(data=data, aes(Day, Number, color=Fruit)) + geom_line())
dev.off()
"""

pygg.ggplot(my_data, my_command)
```

The above script should produce a plot in the file "fruits_by_day.pdf".

## Notes

1. `pygg.ggplot()` imports your data into `R` under the name `data`, so the `data=data` argument to `ggplot` is necessary in almost every case.
2. All `R` ggplot commands must be werapped in `print()` commands in order to actually plot.
