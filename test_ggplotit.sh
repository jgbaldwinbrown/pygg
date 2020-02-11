#!/bin/bash
set -e

cat testdat.txt | ./ggplotit.R '
pdf("testplot.pdf", height=3, width=4)
print(ggplot(data=data, aes(number, size)) + geom_point())
dev.off()
'
