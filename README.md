# Data Science Salary Estimator : Overview of the Project 
* created a model which can be used as a tool that estimates data science salaries (MAE ~$ 11k) to offer a hand for data scientists for negotiating their salary when they get a job.
* Scrapped over 1000 descriptions of job using python and selenium.
* Features Engineered from the text of each job description to get insights on companies which value necessary programming languages/tools python, aws, excel and spark.
* Used GridSearchCV to optimize models like Linear, Lasso and RandomForest and hypertuned the parameters to get the best-fitting model
* Built a client facing API using Flask

## Description of code and resources used in this project
** Python version:** 3.7
** Packages:** pandas, sklearn, numpy, seaborn, matplotlib, selenium, flask, dill, pickle, json, stastmodel.api
** Scrapper Code Article:** https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905
** Scrapper code Github:** https://github.com/arapfaik/scraping-glassdoor-selenium
** Flask Article on Productionization: ** https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2

## Web Scraping
Took the webscraper code (above) did some tweaks to scrape 1000 job postings from glassdoor.com . we got the following information on each job:
*         Job title
*         Salary Estimate
*         Job description
*         Rating
*         Company
*         Location
*         Company Size
*         Company Headquarters
*         Ownership Type
*         Sector
*         Industry
*         Revenue
*         Competitors


