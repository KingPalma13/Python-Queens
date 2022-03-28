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

install.packages("fastR2")

NYC$price <- as.numeric(NYC$price)
NOC$price <- as.numeric(NOC$price)
NorthCarC$price <- as.numeric(NorthCarC$price)

#making the dependent variable numeric in order to run anova on dataset

plotNormalHistogram(NYC$price)
#running histogram on price column in NYC dataset
NYC$priceSQRt <- sqrt(NYC$price)
#the data is positively skewed to have to SQRt it to make more normal
plotNormalHistogram(NYC$priceSQRt)
#checking normality of the new dataset after SQRT
NYC$priceLOG <- log(NYC$price)
#it was still positively skewed 
plotNormalHistogram(NYC$priceLOG)

NYC2 <- NaRV.omit(NYC)
#error messaged recieved then loaded IDPmisc to make get rid of error message
#then used above code in order to omit missing data to do the log process

plotNormalHistogram(NYC2$priceLOG)
#looking at new dataset to see if its more normal; and it is
#now normal

plotNormalHistogram(NOC$price)
#looking at normality
NOC$priceSQRT <- sqrt(NOC$price)
#sqrt dataset to make more normal
plotNormalHistogram(NOC$priceSQRT)
#looking at sqrt data to see normality
#it is normal now

plotNormalHistogram(NorthCarC$price)
#looking at normality of dataset needs to be more normal

NorthCarC$priceLOG <- log(NorthCarC$price)
plotNormalHistogram(NorthCarC$priceLOG)
#running log on data to make data set more normal
#it is normal now

bartlett.test(NYC$price ~ NYC$room_type, data=NYC)
#testing for homogeneity of variance
#p-value <0.5 so violated homogeneity of variance

bartlett.test(NYC2$priceLOG ~ NYC2$room_type, data=NYC2)
#testing for homogeneity of variance
#p-value <0.5 so violated homogeneity of variance

fligner.test(NYC$price ~ NYC$room_type, data= NYC)
#testing for homogeneity of variance
#p-value <0.5 so violated homogeneity of variance

NYCANOVA <- aov(NYC$price ~ NYC$room_type)
#run this if homogeneity if met 
summary(NYCANOVA)
#this was not met but still ran to see what effect it would have if ran 

ANOVA <- lm(NYC2$priceLOG ~ NYC2$room_type, data=NYC2)
Anova(ANOVA, Type="II", white.adjust=TRUE)
#running anova to see if there is significant difference in price

pairwise.t.test(NYC2$priceLOG, NYC2$room_type, p.adjust="none")
pairwise.t.test(NYC$price, NYC$room_type, p.adjust="none")
#checking to see if there is significant difference between each individual room type in prices

pairwise.t.test(NYC2$priceLOG, NYC2$room_type, p.adjust="bonferroni")
#checking to see if there is difference with type errors added

NYCM <- NYC %>% group_by(NYC$room_type) %>% summarize(Mean = mean(NYC$price))
NYCM
#made chart to group room types together and then find the mean price for each room

NYCM2 <- NYC2 %>% group_by(NYC2$room_type) %>% summarize(Mean = mean(NYC2$price))
NYCM2
#made chart to group room types together and then find the mean price for each room

NYCM3 <- NYC2 %>% group_by(NYC2$price) %>% summarize(Mean = mean(NYC2$room_type))
NYCM3
#invalid analysis just playing with code, not valid

NYCM4 <- NYC2 %>% group_by(room_type) %>% summarize(Mean = mean(price))
NYCM4
#running mean comparisons

pairwise.t.test(NYC2$priceLOG, NYC2$room_type, p.adjust="bonferroni", pool.sd = FALSE)
#running test because homogeneit is violated

plotNormalHistogram(NOC$price)
NOC$priceSQRt <- sqrt(NOC$price)
plotNormalHistogram(NOC$priceSQRT)
NOC$priceLOG <- log(NOC$price)
plotNormalHistogram(NOC$priceLOG)
NOC2 <- NaRV.omit(NOC)
plotNormalHistogram(NOC2$priceLOG)
#forgot i ran this already. so ignore this

bartlett.test(NOC2$priceLOG ~ NOC2$room_type, data=NOC2)
#results need to be non-sig so it violates homogeneity

fligner.test(NOC2$priceLOG ~ NOC2$room_type, data=NOC2)
#results need to be non-sig so it violates homogeneity

ANOVANOC <- lm(NOC2$priceLOG ~ NOC2$room_type, data=NOC2)
Anova(ANOVANOC, Type="II", white.adjust=TRUE)
#running because homogeneity was not met but there is a sig diff

pairwise.t.test(NOC2$priceLOG, NOC2$room_type, p.adjust="bonferroni", pool.sd = FALSE )
#running post hoc because homogeneity was not met


NOCM2 <- NOC2 %>% group_by(room_type) %>% summarize(Mean = mean(price))
NOCM2

countNOC <- NOC2 %>% group_by(RT) %>% summarize(Count = Count(RT))
countNOC
#trying to count room type but code is not right


NorthCarC$priceLOG <- log(NorthCarC$price)
plotNormalHistogram(NorthCarC$priceLOG)
#looking at North Carolina data to run anova

bartlett.test(NorthCarC$priceLOG ~ NorthCarC$room_type, data=NorthCarC)
#assumption of homogeneity met

fligner.test(NorthCarC$priceLOG ~ NorthCarC$room_type, data=NorthCarC)
#assumption of homogeneity met

NCANOVA <- aov(NorthCarC$priceLOG ~ NorthCarC$room_type)
summary(NCANOVA)
#homogeneity is met, so running anova on data set 

pairwise.t.test(NorthCarC$priceLOG, NorthCarC$room_type, p.adjust="none")
#looking for sig diff between room types

NC <- NorthCarC %>% group_by(room_type) %>% summarize(Mean = mean(price))
NC
#looking at mean difference by room type group
NOCM2
#looking at mean difference by room type group
NYCM4

#looking at mean difference by room type group


#North carolina is only data set to meet homogeneity
#when it comes to price there is a significant difference in price depending on room type in New york and North Carolina
#new orleans entire room/ apt and hotel rooms thee is no difference their pairwise comparison came out to be 1
#new york and north carolina have no sig diff between the hotel room in mean prices
#new york and north carolina have no sig diff between shared room in mean prices

#north carolina entire rooms/apt count is 2211
#north carolina hotel room count is 17
#north carolina private room count is 390
#north carolina shared room count is 8
#total airbnb count is 2,626

#new york entire rooms/apt count is 20,397
#new york hotel room count is 210
#new york private room count is 17098
#new york shared room count is 572
#total airbnb count is 38,277

#new orleans entire rooms/apt count is 5124
#new orleans hotel room count is 70
#new orleans private room count is 810
#new orleans shared room count is 34
#new orleans airbnb total is 6,038
