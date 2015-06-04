d = read.csv('twitter_regressors.csv')

# need to pull in housing_and_ACS.Rda as f
f = f[c(1,4,5,6,7,8,21)]

df = merge(d,f,on='RegionName')

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


regressors = colnames(d[c(-1)])
combos = combn(regressors,5,simplify=0)
c = data.frame(r1 = rapply(combos, function(x) x[[1]]),
               r2 = rapply(combos, function(x) x[[2]]),
               r3 = rapply(combos, function(x) x[[3]]),
               r4 = rapply(combos, function(x) x[[4]]),
               r5 = rapply(combos, function(x) x[[5]]))

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

n = length(r.squareds.house)

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

