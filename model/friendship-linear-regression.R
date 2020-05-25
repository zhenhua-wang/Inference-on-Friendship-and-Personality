library(sjPlot)
library(sjmisc)
library(sjlabelled)
library(dplyr)

dm = read.csv('dm.csv')

# Calculate correlation
cor(dm%>%select(c(E_s, A_s, C_s, N_s, O_s,
                  E_t, A_t, C_t, N_t, O_t)) %>%na.omit())

# Linear regression
reg = lm(weight ~ E_s + A_s + C_s + N_s + O_s + 
           E_t + A_t + C_t + N_t + O_t, dm)


summary(reg)
tab_model(reg)