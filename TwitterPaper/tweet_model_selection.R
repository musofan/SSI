d = read.csv('twitter_regressors.csv')

# need to pull in housing_and_ACS.Rda as f
f = f[c(1,4,5,6,7,8,21)]

df = merge(d,f,on='RegionName')

g = read.csv("gallup.txt")

# to keep all bbox-defined RegionNames
#dfg = merge(df,g,on='RegionName',all.x=1)
#dfg[c(1,36)][is.na(dfg$overall),]

# to eliminate any that in Gallup are part of group
dfg = merge(df,g,on='RegionName')

str(dfg)

overall = lm(data=dfg, overall~ Hbin.00 +
               Hbin.01 +
               Hbin.02 +
               Hbin.03 +
               Hbin.04 +
               Hbin.05 +
               Hbin.06 +
               Hbin.07 +
               Hbin.08 +
               Hbin.09 +
               Hbin.10 +
               Hbin.11 +
               Hbin.12 + 
               num.faces.alt + 
               face.present.alt + 
               solo.face.alt +
               face.present.rate.alt +
               solo.face.rate.alt +
               social.face.rate.alt +
               num.people.social.faces.alt +
               social.face.alt +
               num.unique.images +
               num.unique.face.images.alt)
summary(overall)

summary(lm(data=dfg,overall~solo.face.rate.alt +
             social.face.rate.alt +
             face.present.rate.alt))


###################
## Comparisons ####
###################

#primary model: gallup overall
overall.lm = lm(data=dfg, 
               overall ~ rank(bachelors)+
                 rank(disabled)+
                 rank(income)+
                 rank(pop)+
                 rank(unemployed)+
                 rank(median.2013)
               )

purpose.lm = lm(data=dfg, 
               purpose ~ rank(bachelors)+
                 rank(disabled)+
                 rank(income)+
                 rank(pop)+
                 rank(unemployed)+
                 rank(median.2013)
)



social.lm = lm(data=dfg, 
               social ~ rank(bachelors)+
                 rank(disabled)+
                 rank(income)+
                 rank(pop)+
                 rank(unemployed)+
                 rank(median.2013)
)



financial.lm = lm(data=dfg, 
               financial ~ rank(bachelors)+
                 rank(disabled)+
                 rank(income)+
                 rank(pop)+
                 rank(unemployed)+
                 rank(median.2013)
)



community.lm = lm(data=dfg, 
               community ~ rank(bachelors)+
                 rank(disabled)+
                 rank(income)+
                 rank(pop)+
                 rank(unemployed)+
                 rank(median.2013)
)



physical.lm = lm(data=dfg, 
               physical ~ rank(bachelors)+
                 rank(disabled)+
                 rank(income)+
                 rank(pop)+
                 rank(unemployed)+
                 rank(median.2013)
)

criterion.overall = summary(overall.lm)$r.squared
criterion.purpose = summary(purpose.lm)$r.squared
criterion.social = summary(social.lm)$r.squared
criterion.financial = summary(financial.lm)$r.squared
criterion.community = summary(community.lm)$r.squared
criterion.physical = summary(physical.lm)$r.squared


dr = data.frame(sapply(dfg[c(2:24)],function(x) rank(x) ))

regressors = colnames(dr)
combos = combn(regressors,6,simplify=0)
c = data.frame(r1 = rapply(combos, function(x) x[[1]]),
               r2 = rapply(combos, function(x) x[[2]]),
               r3 = rapply(combos, function(x) x[[3]]),
               r4 = rapply(combos, function(x) x[[4]]),
               r5 = rapply(combos, function(x) x[[5]]),
               r6 = rapply(combos, function(x) x[[6]])
)

# primary function
rsq.overall <- function(xs) {
  f <- as.formula(paste("overall ~", paste(xs, collapse="+")))
  summary(do.call("lm", args = list(f,data=as.name("dfg"))))$r.squared
}

rsq.purpose <- function(xs) {
  f <- as.formula(paste("purpose ~", paste(xs, collapse="+")))
  summary(do.call("lm", args = list(f,data=as.name("dfg"))))$r.squared
}

rsq.social <- function(xs) {
  f <- as.formula(paste("social ~", paste(xs, collapse="+")))
  summary(do.call("lm", args = list(f,data=as.name("dfg"))))$r.squared
}

rsq.financial <- function(xs) {
  f <- as.formula(paste("financial ~", paste(xs, collapse="+")))
  summary(do.call("lm", args = list(f,data=as.name("dfg"))))$r.squared
}

rsq.community <- function(xs) {
  f <- as.formula(paste("community ~", paste(xs, collapse="+")))
  summary(do.call("lm", args = list(f,data=as.name("dfg"))))$r.squared
}

rsq.physical <- function(xs) {
  f <- as.formula(paste("physical ~", paste(xs, collapse="+")))
  summary(do.call("lm", args = list(f,data=as.name("dfg"))))$r.squared
}


dfg[c(2:24)] = dr
# over 100,000 regressions here...takes a couple minutes
r.squareds.overall = lapply(combos,rsq.overall)

r.squareds.purpose = lapply(combos,rsq.purpose)
r.squareds.social = lapply(combos,rsq.social)
r.squareds.financial = lapply(combos,rsq.financial)
r.squareds.community = lapply(combos,rsq.community)
r.squareds.physical = lapply(combos,rsq.physical)

c$rsq.overall = 1:length(c$r1)
c$rsq.purpose = 1:length(c$r1)
c$rsq.social = 1:length(c$r1)
c$rsq.financial = 1:length(c$r1)
c$rsq.community = 1:length(c$r1)
c$rsq.physical = 1:length(c$r1)


# fill in r-squared values to regressor dataframe 'c'
n = length(r.squareds.overall)
for (i in 1:n) {
  c$rsq.overall[i] = r.squareds.overall[i]
}

for (i in 1:n) {
  c$rsq.purpose[i] = r.squareds.purpose[i]
}

for (i in 1:n) {
  c$rsq.social[i] = r.squareds.social[i]
}

for (i in 1:n) {
  c$rsq.financial[i] = r.squareds.financial[i]
}

for (i in 1:n) {
  c$rsq.community[i] = r.squareds.community[i]
}

for (i in 1:n) {
  c$rsq.physical[i] = r.squareds.physical[i]
}






overall.max = c[c$rsq.overall == max(unlist(c$rsq.overall)),]
overall.purpose = c[c$rsq.purpose == max(unlist(c$rsq.purpose)),]
overall.social = c[c$rsq.social == max(unlist(c$rsq.social)),]
overall.financial = c[c$rsq.financial == max(unlist(c$rsq.financial)),]
overall.community = c[c$rsq.community == max(unlist(c$rsq.community)),]
overall.physical = c[c$rsq.physical == max(unlist(c$rsq.physical)),]



###############
## 5 regr #####
###############


house.lm = lm(data=df, median.2013 ~ bachelors+disabled+income+pop+unemployed)
bach.lm = lm(data=df, bachelors ~ median.2013+disabled+income+pop+unemployed)
income.lm = lm(data=df, income ~ bachelors+disabled+median.2013+pop+unemployed)
empl.lm = lm(data=df, unemployed ~ bachelors+disabled+income+pop+median.2013)
pop.lm = lm(data=df, pop ~ bachelors+disabled+income+median.2013+unemployed)

criterion.house = summary(house.lm)$r.squared
criterion.bach = summary(bach.lm)$r.squared
criterion.income = summary(income.lm)$r.squared
criterion.empl = summary(empl.lm)$r.squared
criterion.pop = summary(pop.lm)$r.squared

"
regressors = colnames(d[c(-1)])
combos = combn(regressors,5,simplify=0)
c = data.frame(r1 = rapply(combos, function(x) x[[1]]),
               r2 = rapply(combos, function(x) x[[2]]),
               r3 = rapply(combos, function(x) x[[3]]),
               r4 = rapply(combos, function(x) x[[4]]),
               r5 = rapply(combos, function(x) x[[5]]))
"

rsq.house <- function(xs) {
  f <- as.formula(paste("median.2013 ~", paste(xs, collapse="+")))
  summary(do.call("lm", args = list(f,data=as.name("df"))))$r.squared
}

rsq.bach <- function(xs) {
  f <- as.formula(paste("bachelors ~", paste(xs, collapse="+")))
  summary(do.call("lm", args = list(f,data=as.name("df"))))$r.squared
}

rsq.income <- function(xs) {
  f <- as.formula(paste("income ~", paste(xs, collapse="+")))
  summary(do.call("lm", args = list(f,data=as.name("df"))))$r.squared
}

rsq.empl <- function(xs) {
  f <- as.formula(paste("unemployed ~", paste(xs, collapse="+")))
  summary(do.call("lm", args = list(f,data=as.name("df"))))$r.squared
}

rsq.pop <- function(xs) {
  f <- as.formula(paste("pop ~", paste(xs, collapse="+")))
  summary(do.call("lm", args = list(f,data=as.name("df"))))$r.squared
}


r.squareds.house = lapply(combos,rsq.house)
r.squareds.income = lapply(combos,rsq.income)
r.squareds.empl = lapply(combos,rsq.empl)
r.squareds.bach = lapply(combos,rsq.bach)
r.squareds.pop = lapply(combos,rsq.pop)


c$rsq.house = 1:length(c$r1)
c$rsq.bach = 1:length(c$r1)
c$rsq.income = 1:length(c$r1)
c$rsq.empl = 1:length(c$r1)
c$rsq.pop = 1:length(c$r1)



#n = length(r.squared.house)
for (i in 1:n) {
  c$rsq.house[i] = r.squareds.house[i]
}

for (i in 1:n) {
  c$rsq.bach[i] = r.squareds.bach[i]
}

for (i in 1:n) {
  c$rsq.income[i] = r.squareds.income[i]
}

for (i in 1:n) {
  c$rsq.empl[i] = r.squareds.empl[i]
}

for (i in 1:n) {
  c$rsq.pop[i] = r.squareds.pop[i]
}




house.max = c[c$rsq.house == max(unlist(c$rsq.house)),]
bach.max = c[c$rsq.bach == max(unlist(c$rsq.bach)),]
income.max = c[c$rsq.income == max(unlist(c$rsq.income)),]
empl.max = c[c$rsq.empl == max(unlist(c$rsq.empl)),]
pop.max = c[c$rsq.pop == max(unlist(c$rsq.pop)),]

