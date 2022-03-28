library("rcompanion")
library("dplyr")
library("psych")
library("mvnormtest")
library("gmodels")
library("tidyr")
library("car")
library("fastR2")
library("effects")
library("multcomp")
library("IDPmisc")

#loading up libraries

AU <- Austin %>% group_by(room_type) %>% summarize(Mean = mean(price))
AU

Bt <- boston %>% group_by(room_type) %>% summarize(Mean = mean(price))
Bt

Cg <- chicago %>% group_by(room_type) %>% summarize(Mean = mean(price))
Cg

Dv <- Denver %>% group_by(room_type) %>% summarize(Mean = mean(price))
Dv

la <- los_angeles %>% group_by(room_type) %>% summarize(Mean = mean(price))
la

Na <- nashville %>% group_by(room_type) %>% summarize(Mean = mean(price))
Na

pd <- portland %>% group_by(room_type) %>% summarize(Mean = mean(price))
pd

sf <- san_fran %>% group_by(room_type) %>% summarize(Mean = mean(price))
sf

st <- seattle %>% group_by(room_type) %>% summarize(Mean = mean(price))
st

#running the means for all the dataserts loads for cities

auc <- Austin %>% group_by(room_type) %>% summarize(count = n())
auc

btc <- boston %>% group_by(room_type) %>% summarize(count = n())
btc

cgc <- chicago %>% group_by(room_type) %>% summarize(count = n())
cgc

Dvc <- Denver %>% group_by(room_type) %>% summarize(count = n())
Dvc

lac <- los_angeles %>% group_by(room_type) %>% summarize(count = n())
lac

Nac <- nashville %>% group_by(room_type) %>% summarize(count = n())
Nac

pdc <- portland %>% group_by(room_type) %>% summarize(count = n())
pdc


sfc <- san_fran %>% group_by(room_type) %>% summarize(count = n())
sfc

stc <- seattle %>% group_by(room_type) %>% summarize(count = n())
stc

#getting the counts for all the cities to know how much data is being used

plotNormalHistogram(Austin$price)
plotNormalHistogram(boston$price)
plotNormalHistogram(chicago$price)
plotNormalHistogram(Denver$price)
plotNormalHistogram(los_angeles$price)
plotNormalHistogram(nashville$price)
plotNormalHistogram(portland$price)
plotNormalHistogram(san_fran$price)
plotNormalHistogram(seattle$price)

#making histograms to see the normality of all the datasets 