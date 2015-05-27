setwd("~/Dropbox/thinkpad_home/Software-Studies/housing_and_ACS")
load('housing_and_ACS.Rda')

library(ggplot2)
attach(f)

ggplot(f,aes(bachelors,income)) + 
  geom_text(aes(label=RegionName), size=3)

ggplot(f,aes(disabled,bachelors)) + 
  geom_text(aes(label=RegionName), size=3)

