
fileData <- "E:/algorithm_carPredict/data/1x.txt"
data <- read.csv(fileData)
str(data)

fileData1 <- "E:/algorithm_carPredict/data/10x.txt"
data1 <- read.csv(fileData1)
str(data1)
#plot(data1$latitude, data1$longitude, type='b')

fileData2 <- "E:/algorithm_carPredict/data/1x_04.txt"
data2 <- read.csv(fileData2)
str(data2)

fileData3 <- "E:/algorithm_carPredict/data/1x_05.txt"
data3 <- read.csv(fileData3)
str(data3)

opar = par(no.readonly = T)
plot(data$longitude, data$latitude,, type='b', col="red", main="1、10号车在8.3号全天行驶路线图",
     ylab="纬度", xlab="经度", ylim=c(30.55,30.73),xlim=c(103.95,104.14))
lines(data1$longitude, data1$latitude, type='b', col="blue")
legend("topleft", inset=.05, legend =c(1,10), col=c("red","blue"),title = "car number", pch = c(1,1))
par(opar)

opar = par(no.readonly = T)
plot(data$longitude, data$latitude,, type='b', col="red", main="1号车在8.3、8.4号全天行驶路线图",
     ylab="纬度", xlab="经度", ylim=c(30.55,30.73),xlim=c(103.95,104.14))
lines(data2$longitude, data2$latitude, type='b', col="blue")
legend("topleft", inset=.05, legend =c("8.3号","8.4号"), col=c("red","blue"),title = "day number", pch = c(1,1))
par(opar)

opar = par(no.readonly = T)
plot(data$longitude, data$latitude,, type='b', col="red", main="1号车在8.3、8.5号全天行驶路线图",
     ylab="纬度", xlab="经度", ylim=c(30.55,30.73),xlim=c(103.95,104.14))
lines(data3$longitude, data3$latitude, type='b', col="blue")
legend("topleft", inset=.05, legend =c("8.3号","8.5号"), col=c("red","blue"),title = "day number", pch = c(1,1))
par(opar)



fileData1 <- "E:/algorithm_carPredict/data/predPaths_test.txt"
data1 <- read.csv(fileData1, header = F)
data1 <- data1[which(data1$V1==1),]
str(data1)

fileData2 <- "E:/algorithm_carPredict/data/2788x_03.txt"
data2 <- read.csv(fileData2)
str(data2)

opar = par(no.readonly = T)
plot(data2$longitude, data2$latitude,, type='b', col="red", main="2788号车在8.3号全天行驶路线图与测试集1号路线图",
     ylab="纬度", xlab="经度")
lines(data1$V4, data1$V3, type='b', col="blue")
legend("topleft", inset=.05, legend =c(2788,'路线1'), col=c("red","blue"),title = "car number", pch = c(1,1))
par(opar)

plot(data1$V4, data1$V3,, type='b', col="red", main="2788号车在8.3号全天行驶路线图与测试集1号路线图",
     ylab="纬度", xlab="经度")