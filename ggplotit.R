#!/usr/bin/env Rscript

library(ggplot2)
library(data.table)
library(rjson)

jdata = fromJSON(file="stdin")
data = as.data.frame(jdata$data)
# print(data) # DEBUG

args = commandArgs(trailingOnly=TRUE)
ggcode = args[1]

# print(ggcode) # DEBUG

eval(parse(text=ggcode))
