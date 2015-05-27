df = read.csv('/home/damoncrockett/Dropbox/CALIT2DATA/weather/processedData/weather2013.csv')

jan = subset(df, df$Date >= 20130101 & df$Date < 20130201)
feb = subset(df, df$Date >= 20130201 & df$Date < 20130301)
mar = subset(df, df$Date >= 20130301 & df$Date < 20130401)
apr = subset(df, df$Date >= 20130401 & df$Date < 20130501)
may = subset(df, df$Date >= 20130501 & df$Date < 20130601)
jun = subset(df, df$Date >= 20130601 & df$Date < 20130701)
jul = subset(df, df$Date >= 20130701 & df$Date < 20130801)
aug = subset(df, df$Date >= 20130801 & df$Date < 20130901)
sep = subset(df, df$Date >= 20130901 & df$Date < 20131001)
oct = subset(df, df$Date >= 20131001 & df$Date < 20131101)
nov = subset(df, df$Date >= 20131101 & df$Date < 20131201)
dec = subset(df, df$Date >= 20131201 & df$Date <= 20131231)
rm(df)

length(unique(jan$CITY))
length(unique(feb$CITY))
length(unique(mar$CITY))
length(unique(apr$CITY))
length(unique(may$CITY))
length(unique(jun$CITY))
length(unique(jul$CITY))
length(unique(aug$CITY))
length(unique(sep$CITY))
length(unique(oct$CITY))
length(unique(nov$CITY))
length(unique(dec$CITY))

table(jan$CITY)
table(feb$CITY)
table(mar$CITY)
table(apr$CITY)
table(may$CITY)
table(jun$CITY)
table(jul$CITY)
table(aug$CITY)
table(sep$CITY)
table(oct$CITY)
table(nov$CITY)
table(dec$CITY)

## incomplete cities: 
## Eureka
## Marquette
## Dallas Fort Worth
## Wichita
