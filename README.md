# DSA210-TermProject -> Second-Hand Car Price Analysis  

##  Objective  
This project aims to find out what affects the prices of second-hand cars by how much. By collecting data on different car models, mileage, brands, accident history, and more, I will look for patterns that impact car prices and how much it affects them. I will also investigate how a brand's value affects the weight of these data points' effects.

##  Motivation  
I'm currently looking to buy a second-hand car, and I’ve noticed that prices can vary a lot and decided to make it a little bit more scientific to determine whether a price is appropriate for the given car or not so that I don't buy an overpriced car. This project will help me (and others) understand which factors make a car more expensive or cheaper and prevent us from paying unnecesary money.  

##  Data Collection  
- **Where will the data come from?** I combined two second hand car listings data that I found from kaggle. I combined them appropriately and refinemened the data by feature engineering.
- **What information is present in my dataset?**  
  - Car brand and model  
  - Year of manufacture  
  - Mileage (km)  
  - Fuel type (gasoline, diesel, electric, etc.)  
  - Price (this is the main thing I want to analyze)
  - Location
  - **Feature Transformation and Enrichment:**
    - car_age
    - brand_classification (luxury,economy..)
    - log_price
    - log_mileage
    - price_per_km

#### My Data Set:
https://github.com/CemKaya1/DSA210-TermProject/blob/main/used_cars_data_dsa.csv

**The data sources used in the making are:**
- https://www.kaggle.com/datasets/erenakbulut/user-car-prices-barcelona-2022
- https://www.kaggle.com/datasets/mayankpatel14/second-hand-used-cars-data-set-linear-regression


##  Tools & Technologies  
- **Python** for working with data  
- **Pandas** to organize and analyze the dataset  
- **Matplotlib & Seaborn** to create charts and graphs  
- **BeautifulSoup/Selenium** for potential web scraping (if it will be necessary)

##  How Will I Analyze the Data?  
1. **Collect Data:** I will use the car listings data I gathered from different sources in kaggle.  
2. **Clean Data:** Remove missing or incorrect values and make sure the data is structured properly.  
3. **Explore the Data:**  
   - Check how price changes with mileage, brand, and other factors using bivariate analysis.  
   - Create graphs to visualize trends and detect correlations.
   - Estimate a **market price value** for different car models based on key factors.  
   - Compare actual listing prices to the estimated market price to see if they are overpriced or underpriced.  
4. **Test Hypotheses:**
   - Alternative Hypothesis (HA): "The price sensitivity to mileage changes across different car brands, with luxury brands showing higher        decrease per kilometer compared to economy brands."
   - Explaratory Questions:
     - Which brands hold their value the longest?
     - Can I estimate a fair market price for a car based on key attributes?  
     - Are some car listings significantly overpriced or underpriced compared to the estimated market price?  

6. **Findings & Conclusions:** Summarize the key takeaways and come to a conclusion regarding fail to reject or to reject the Null Hypothesis.  

##  Example Analysis & What I Expect to Find  
Example Analysis: As an example, I might create a scatter plot to see if cars with more mileage are always cheaper.

What i expect to find: **"The price sensitivity to mileage changes across different car brands, with luxury brands showing higher decrease per kilometer compared to economy brands."**  

## Explatory Anlalysis Findings

Exploratory Analysis Results
Our exploratory analysis revealed a significant correlation between a car's brand category (luxury vs. economy) and its price sensitivity to increased mileage. The p-value from our statistical test was effectively 0.000, allowing us to confidently reject the Null Hypothesis at the 0.05 significance level.

The most influential factor affecting car price was car age, followed closely by mileage. Notably, luxury brands exhibited greater value loss with higher mileage compared to economy brands. Among individual brands, Kia (economy) held its value best, while BMW (luxury) showed the steepest depreciation.

Overall, while mileage and age impact all car prices, the degree of that impact varies significantly by brand—insights we quantified in detail across different manufacturers.



## Possible Future Improvements  
- Collecting data from more websites to get better results  
- Adding extra details like service history and location-based price differences  
