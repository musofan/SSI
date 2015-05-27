library(RWordPress)
options(WordpressLogin = c(damoncrockett = 'Cerberus6921'),
        WordpressURL = 'https://damoncrockett.wordpress.com/xmlrpc.php')
library(knitr)
knit2wp('IGNOAA.Rmd', title = 'Analyzing Instagram and Weather Data')
