# article: https://fivethirtyeight.com/features/higher-rates-of-hate-crimes-are-tied-to-income-inequality/
# all data: https://data.fivethirtyeight.com/
# linear regression: http://r-statistics.co/Linear-Regression.html
# multiple linear regression: https://www.statmethods.net/stats/regression.html  

# manually set working directory

# load packages
library(data.table)
library(ggplot2)
library(pls)

# load data
data <- fread("hate_crimes.csv")

# try plotting
ggplot(data, aes(x = median_household_income, y = share_unemployed_seasonal)) +
  geom_point() +
  theme_bw()

# build linear model and add it to the plot
linear.mod <- lm(share_unemployed_seasonal ~ median_household_income, data = data)

# try plotting - direct from linear model
ggplot(data, aes(x = median_household_income, y = share_unemployed_seasonal)) +
  geom_point() +
  geom_abline(intercept = coef(linear.mod)[["(Intercept)"]],
              slope = coef(linear.mod)[["median_household_income"]]) + 
  theme_bw()

# try plotting - ggplot's stat_smooth
ggplot(data, aes(x = median_household_income, y = share_unemployed_seasonal)) +
  geom_point() +
  stat_smooth(method="lm") +
  theme_bw()


#Multiple regression
multi.mod <- lm(avg_hatecrimes_per_100k_fbi~ share_white_poverty+ share_voters_voted_trump+ gini_index, data = data)

#plot the data:
plot(linear.mod)

#principal component regression

pcr_fit = pcr(data, avg_hatecrimes_per_100k_fbi)
coef(mod, comps=1:4)
summary(pcr_fit)
