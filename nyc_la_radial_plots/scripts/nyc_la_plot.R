nyc = read.csv('/Users/damoncrockett/images_nyc/nyc_metadata.csv')
la = read.csv('/Users/damoncrockett/images_la/la_metadata.csv')

library(ggplot2)
ggplot(la,aes(hue)) + geom_histogram(color='white') +
  theme(panel.background = element_rect(fill = "black"),
        panel.grid.major = element_line(color = "black"),
        panel.grid.minor = element_line(color = "black"),
        plot.background = element_rect(fill = "black"),
        legend.position="none",
        axis.text = element_text(size=rel(0.7), color='white'),
        text = element_text(face='plain', color='white', size = 15)) +
  labs(title='LA HUE')
