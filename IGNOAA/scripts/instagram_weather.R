setwd("~/Desktop")

df = read.csv('/home/damoncrockett/Desktop/IGNOAA/instagram_weather.csv')


df$X = NULL
df$link_author = as.character(df$link_author)
df$link_author = strsplit(df$link_author, '/')
df$link_author = lapply(df$link_author, function(x)(x = x[4]))  
df$link_author = as.character(df$link_author)
df$link_author = as.factor(df$link_author)

#####################
### Resolved FULL####
#####################


df = df[df$flag=='False',]
df$flag = NULL

tmp = rle(sort(c(as.character(df$resolution))))
df$count = tmp[[1]][match(df$resolution, tmp[[2]])]

# rle - nifty!
individual_count = rle(sort(c(as.character(df$link_author))))
df$individual_count = individual_count[[1]][match(df$link_author, individual_count[[2]])]
df$link_author = droplevels(df$link_author)

summary(df$individual_count)

summary(lm(data=df, count~individual_count))

length(unique(df$link_author))
table(df$individual_count)

qplot(df$individual_count, binwidth=1)

community = subset(df, df$individual_count > 158)
community$link_author = droplevels(community$link_author)
community$flag=NULL

#####################
### Individuals  ####
#####################

anova(lm(data=df, individual_count~temp))
summary(lm(data=df, individual_count~temp))

library(plyr)

by.resolution = ddply(df, c('resolution'), summarize,
                      count = mean(count),
                      individual_count = mean(individual_count),
                      temp = mean(temp),
                      sky = mean(sky),
                      precipitation = mean(precipitation),
                      weekday = mean(weekday),
                      month = mean(month),
                      hour = mean(hour),
                      lat = mean(lat),
                      lon = mean(lon))

options('scipen'=100, 'digits'=4)

summary(lm(data=by.resolution, individual_count~temp))
summary(lm(data=by.resolution, individual_count~precipitation))
summary(lm(data=by.resolution, individual_count~sky))
summary(lm(data=by.resolution, individual_count~lat))
summary(lm(data=by.resolution, individual_count~lon))
summary(lm(data=by.resolution, individual_count~factor(weekday)))
summary(lm(data=by.resolution, individual_count~factor(hour)))
summary(lm(data=by.resolution, individual_count~factor(month)))


strangers = df[df$individual_count == 1,]
strangers_sample = strangers[sample(1:nrow(strangers), 13641, replace=FALSE),]

ggplot(RS[RS$weekend.primetime==TRUE,], aes(x=lon, y=lat, color=stranger)) + 
  geom_point(alpha=.42, size=4.2) +
  #scale_size_continuous(range = c(1,56)) +
  #scale_color_gradient(low='green', high='red') +
  theme(panel.background = element_rect(fill = "black"),
        panel.grid.major = element_line(color = "black"),
        panel.grid.minor = element_line(color = "black"),
        plot.background = element_rect(fill = "black"),
        legend.position="none",
        axis.text = element_text(size=rel(0.7), color='white'),
        text = element_text(family='arial', face='plain', color='white', size = 15)) +
  labs(x='LON',y='LAT', title='WEEKEND PRIMETIME') +
  xlim(cp.lon - margin, cp.lon + margin) +
  ylim(cp.lat - margin, cp.lat + margin)


#####################
### R vs. S      ####
#####################

ggplot(strangers_sample, aes(x=temp, y=count, color = count)) + 
  geom_point(size=2.1, alpha = 0.77) +
  scale_color_gradient(low = "blue", high = "red") +
  theme(panel.background = element_rect(fill = "black"),
        panel.grid.major = element_line(color = "black"),
        panel.grid.minor = element_line(color = "black"),
        plot.background = element_rect(fill = "black"),
        legend.position="none",
        axis.text = element_text(size=rel(0.7), color='white'),
        text = element_text(family='arial', face='plain', color='white', size = 15)) +
  labs(x='FAHRENHEIT',y='POSTS/HR', title='STRANGERS') +
  xlim(0, 100) +
  ylim(0, 1000)

RS=rbind(community,strangers_sample)
RS$stranger = RS$individual_count==1
RS$rain = RS$precipitation > 0

library(gmodels)

summary(lm(data=RS, count~stranger))
summary(lm(data=RS, temp~stranger))
summary(lm(data=RS, sky~stranger))
CrossTable(RS$stranger, RS$rain, expected=TRUE)

RS$weekdays = RS$weekday < 6
RS$weekend = RS$weekday > 5
RS$warm = RS$temp > 65
RS$summer = RS$month > 5 & RS$month < 8
RS$daylight = RS$hour > 5 & RS$hour < 19
RS$waking = RS$hour > 5 & RS$hour < 23
RS$midday = RS$hour > 11 & RS$hour < 16
RS$dead.of.night = RS$hour > 2 & RS$hour < 5
RS$party = RS$hour > 21 | RS$hour < 2
RS$weekend.party = RS$hour > 20 & RS$weekday > 4 & RS$weekday < 7
RS$primetime = RS$hour > 16 & RS$hour < 22
RS$morning = RS$hour > 5 & RS$hour < 12
RS$business = RS$hour > 8 & RS$hour < 18 & RS$weekday < 6
RS$midday.summer = RS$hour > 11 & RS$hour < 14 & RS$month > 5
RS$midday.schoolyear = RS$hour > 11 & RS$hour < 14 & RS$month < 6
RS$weekend.primetime = RS$weekday > 5 & RS$hour > 16 & RS$hour < 22

CrossTable(RS$stranger, RS$weekdays, expected=TRUE)
CrossTable(RS$stranger, RS$warm, expected=TRUE)
CrossTable(RS$stranger, RS$summer, expected=TRUE)
CrossTable(RS$stranger, RS$daylight, expected=TRUE)
CrossTable(RS$stranger, RS$waking, expected=TRUE)
CrossTable(RS$stranger, RS$midday, expected=TRUE)
CrossTable(RS$stranger, RS$dead.of.night, expected=TRUE)
CrossTable(RS$stranger, RS$party, expected=TRUE)
CrossTable(RS$stranger, RS$weekend.party, expected=TRUE)
CrossTable(RS$stranger, RS$primetime, expected=TRUE)
CrossTable(RS$stranger, RS$morning, expected=TRUE)
CrossTable(RS$stranger, RS$business, expected=TRUE)
CrossTable(RS$stranger, RS$midday.summer, expected=TRUE)
CrossTable(RS$stranger, RS$midday.schoolyear, expected=TRUE)
CrossTable(RS$stranger, RS$weekend.primetime, expected=TRUE)




#####################
### Geo Variance ####
#####################




#####################
###   Plots     #####
#####################


library(ggplot2)


core = read.csv('/home/damoncrockett/Desktop/IGNOAA/instagram_by_resolution.csv')

library(ggplot2)

ggplot(core, aes(x=temp, y=count, color = count)) + 
  geom_point(size=I(5.4), alpha = 0.88) +
  scale_color_gradient(low = "blue", high = "red") +
  theme(panel.background = element_rect(fill = "black"),
        panel.grid.major = element_line(color = "black"),
        panel.grid.minor = element_line(color = "black"),
        plot.background = element_rect(fill = "black"),
        legend.position="none",
        axis.text = element_text(size=rel(0.7), color='white'),
        text = element_text(family='arial', face='plain', color='white', size = 30)) +
  labs(x='FAHRENHEIT',y='POSTS/HR')




ggplot(rain.no.clouds, aes(x=precipitation, y=count, color = count)) + 
  geom_point(size=I(5.4), alpha = 0.77) +
  scale_color_gradient(low = "blue", high = "red") +
  theme(panel.background = element_rect(fill = "black"),
        panel.grid.major = element_line(color = "black"),
        panel.grid.minor = element_line(color = "black"),
        plot.background = element_rect(fill = "black"),
        legend.position="none",
        axis.text = element_text(size=rel(0.7), color='white'),
        text = element_text(family='arial', face='plain', color='white', size = 30)) +
  labs(x='IN RAINFALL/HR WHEN RAINING WO/CLOUDS',y='POSTS/HR')


ggplot(no.rain, aes(x=factor(sky), y=count)) + 
  geom_boxplot() +
  theme(panel.background = element_rect(fill = "black"),
        panel.grid.major = element_line(color = "black"),
        panel.grid.minor = element_line(color = "black"),
        plot.background = element_rect(fill = "black"),
        legend.position="none",
        axis.text = element_text(size=rel(0.7), color='white'),
        text = element_text(family='arial', face='plain', color='white', size = 17)) +
  labs(x='SKY COVER WO/RAIN',y='POSTS/HR')

ggplot(core, aes(x=factor(sky))) + 
  geom_histogram(fill='white') +
  theme(panel.background = element_rect(fill = "black"),
        panel.grid.major = element_line(color = "black"),
        panel.grid.minor = element_line(color = "black"),
        plot.background = element_rect(fill = "black"),
        legend.position="none",
        axis.text = element_text(size=rel(0.7), color='white'),
        text = element_text(family='arial', face='plain', color='white', size = 17)) +
  labs(x='SKY COVER',y='COUNT')

ggplot(core, aes(x=factor(sky))) + 
  geom_histogram(fill='black', color='white') +
  theme(panel.background = element_rect(fill = "black"),
        panel.grid.major = element_line(color = "black"),
        panel.grid.minor = element_line(color = "black"),
        plot.background = element_rect(fill = "black"),
        legend.position="none",
        axis.text = element_text(size=rel(0.7), color='white'),
        text = element_text(family='arial', face='plain', color='white', size = 17)) +
  labs(x='SKY COVER',y='COUNT')




margin = 0.0125
cp.lon = -73.96917
cp.lat = 40.77889















ggplot(regulars, aes(x=lon, y=lat, color = factor())) + 
  geom_point(size=I(17), alpha = 0.17) +
  theme(panel.background = element_rect(fill = "black"),
        panel.grid.major = element_line(color = "black"),
        panel.grid.minor = element_line(color = "black"),
        plot.background = element_rect(fill = "black"),
        legend.position="none",
        axis.text = element_text(size=rel(0.7), color='white'),
        text = element_text(family='arial', face='plain', color='white', size = 15)) +
  labs(x='LON',y='LAT', title='10') +
  xlim(cp.lon - margin, cp.lon + margin) +
  ylim(cp.lat - margin, cp.lat + margin)



ggplot(h0llyx_, aes(x=factor(sky))) + 
  geom_histogram(fill='black', color='white') +
  theme(panel.background = element_rect(fill = "black"),
        panel.grid.major = element_line(color = "black"),
        panel.grid.minor = element_line(color = "black"),
        plot.background = element_rect(fill = "black"),
        legend.position="none",
        axis.text = element_text(size=rel(0.7), color='white'),
        text = element_text(family='arial', face='plain', color='white', size = 17)) +
  labs(x='SKY COVER',y='COUNT', title='h0llyx_') +
  ylim(0,500)






ggplot(regulars, aes(x=lon, y=lat, color = factor(link_author))) + 
  geom_point(size=I(17), alpha = 0.17) +
  theme(panel.background = element_rect(fill = "black"),
        panel.grid.major = element_line(color = "black"),
        panel.grid.minor = element_line(color = "black"),
        plot.background = element_rect(fill = "black"),
        legend.position="none",
        axis.text = element_text(size=rel(0.7), color='white'),
        text = element_text(family='arial', face='plain', color='white', size = 15)) +
  labs(x='LON',y='LAT', title='10') +
  xlim(cp.lon - margin, cp.lon + margin) +
  ylim(cp.lat - margin, cp.lat + margin)  

community = subset(df, df$individual_count > 158)
community$link_author = droplevels(community$link_author)

"30a0506"                  "agh212"                   "arianesloanpr"            "ascresale"                "ayyeldc"                  "badgirlgenie"             "beautygypsy"             
[8] "bellaz_beauty"            "billfelty"                "briannadprice"            "bridalbeautician"         "briggettebausthair"       "buffy.the.vampire.slayer" "butterfieldnyc"          
[15] "celine_cute_crazy"        "claudinhaweiss"           "core_personal_training"   "danapirulli"              "dustycratez"              "fd_gallery"               "francisco689"            
[22] "franfinefashion"          "gymnast_and_stuff"        "h0llyx_"                  "_hova"                    "jackie589_"               "jay_kemosabee"            "jedchase"                
[29] "johnalfred"               "kittybella1"              "lulujam"                  "mysilversparklesjewelry"  "nikkislesin"              "oujia_iji"                "piercemattie"            
[36] "rcourihay"                "sofiajain"                "sportsviness"             "streetskessel"            "studsandsummer"           "susanwinship"             "the_first_slayer"        
[43] "the_kidd29"               "thelilcizzle"             "tonydodgewriter"          "triviaaddotcom"           "trucnnyc"                 "venus_nyc1"               "weareallmonsters_"       
[50] "westnyc"    


community_resolved_rain = subset(community_resolved, community_resolved$precipitation > 0)

ggplot(community_resolved[community_resolved$link_author == 'westnyc',], aes(x=lon, y=lat, size=precipitation, color=temp)) + 
  geom_point(alpha = 0.14) +
  scale_color_gradient(low='green', high='red') +
  scale_size_continuous(range = c(7,35)) + 
  theme(panel.background = element_rect(fill = "black"),
        panel.grid.major = element_line(color = "black"),
        panel.grid.minor = element_line(color = "black"),
        plot.background = element_rect(fill = "black"),
        legend.position="none",
        axis.text = element_text(size=rel(0.7), color='white'),
        text = element_text(family='arial', face='plain', color='white', size = 15)) +
  labs(x='LON',y='LAT', title='westnyc') +
  xlim(cp.lon - margin, cp.lon + margin) +
  ylim(cp.lat - margin, cp.lat + margin)
  #geom_point(data=community_resolved[community_resolved$link_author == 'claudinhaweiss',], aes(size=precipitation), color='blue',alpha=0.14)



sum(community$individual_count)



#####################
### Resolved     ####
#####################


tmp = df_resolved[c('link_author','lat','lon')]
authors = as.list(unique(as.character(df$link_author)))


df_sample = df[sample(1:nrow(df), 10625, replace=FALSE),]


ggplot(df_sample, aes(reorder(link_author, individual_count), count, color = count)) + 
  geom_point(size=1, alpha = 0.77) +
  scale_color_gradient(low = "blue", high = "red") +
  theme(panel.background = element_rect(fill = "black"),
        panel.grid.major = element_line(color = "black"),
        panel.grid.minor = element_line(color = "black"),
        plot.background = element_rect(fill = "black"),
        legend.position="none",
        axis.text = element_text(size=rel(0.47), color='white'),
        text = element_text(family='arial', face='plain', color='white', size = 20)) +
  labs(x='INDIVIDUAL BY VOLUME',y='COUNT FOR RESOLUTION')



write.csv(df, '/home/damoncrockett/Desktop/IGNOAA/IGNOAA.csv')
write.csv(RS, '/home/damoncrockett/Desktop/IGNOAA/IGNOAA_RS.csv')

mean(RS$lon)






