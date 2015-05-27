f = read.csv('frame.csv')
f$X = NULL
f = f[,c(2,7,8,1,3,4,5,6,9,10,11,12,13,14,15,16,17,18,19,20,21)]
save(f,file='housing_and_ACS.Rda')