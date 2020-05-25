data(IR90s)
gdp<-IR90s$nodevars[,2] 
topgdp<-which(gdp>=sort(gdp,decreasing=TRUE)[30] )
Y<-log( IR90s$dyadvars[topgdp,topgdp,2] + 1 )

Rowcountry<-matrix(rownames(Y),nrow(Y),ncol(Y)) 
Colcountry<-t(Rowcountry)
anova(lm( c(Y) ~ c(Rowcountry) + c(Colcountry) ) )

rmean<-rowMeans(Y,na.rm=TRUE) ; cmean<-colMeans(Y,na.rm=TRUE)

muhat<-mean(Y,na.rm=TRUE) 
ahat<-rmean-muhat 
bhat<-cmean-muhat
Xd<-IR90s$dyadvars[topgdp,topgdp,c(1,3,4,5)] 
Xd[,,3]<-log(Xd[,,3])