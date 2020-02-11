#!/usr/bin/env Rscript

library(ggplot2)
library(data.table)

data = as.data.frame(fread("cat /dev/stdin", header=TRUE))
# print(data) # DEBUG

args = commandArgs(trailingOnly=TRUE)
ggcode = args[1]

# print(ggcode) # DEBUG

eval(parse(text=ggcode))
