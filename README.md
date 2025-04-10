# DSA210-TermProject -> Second-Hand Car Price Analysis  

##  Objective  
This project aims to find out what affects the prices of second-hand cars by how much. By collecting data on different car models, mileage, brands, accident history, and more, I will look for patterns that impact car prices and how much it affects them. I will also investigate how a brand's value affects the weight of these data points' effects.

##  Motivation  
I'm currently looking to buy a second-hand car, and I’ve noticed that prices can vary a lot and decided to make it a little bit more scientific to determine whether a price is appropriate for the given car or not so that I don't buy an overpriced car. This project will help me (and others) understand which factors make a car more expensive or cheaper and prevent us from paying unnecesary money.  

##  Data Collection  
- **Where will the data come from?** I combined two second hand car listings data that I found from kaggle. The data sources:
- https://www.kaggle.com/datasets/erenakbulut/user-car-prices-barcelona-2022
- https://www.kaggle.com/datasets/mayankpatel14/second-hand-used-cars-data-set-linear-regression
- **What information is present in my dataset?**  
  - Car brand and model  
  - Year of manufacture  
  - Mileage (km)  
  - Accident history (if available)  
  - How many of the given car model is on the market currently (rarity) 
  - Fuel type (gasoline, diesel, electric, etc.)  
  - Transmission type (manual or automatic)  
  - Price (this is the main thing I want to analyze)  

##  Tools & Technologies  
- **Python** for working with data  
- **Pandas** to organize and analyze the dataset  
- **Matplotlib & Seaborn** to create charts and graphs  
- **BeautifulSoup/Selenium** for potential web scraping (if it will be necessary)

##  How Will I Analyze the Data?  
1. **Collect Data:** I will use the car listings data I gathered from different sources in kaggle.  
2. **Clean Data:** Remove missing or incorrect values and make sure the data is structured properly.  
3. **Explore the Data:**  
   - Check how price changes with mileage, brand, and other factors.  
   - Create graphs to visualize trends.
   - Estimate a **market price value** for different car models based on key factors.  
   - Compare actual listing prices to the estimated market price to see if they are overpriced or underpriced.  
4. **Test Hypotheses:**  
   - Which characteristic of a car determines its price the most?
   - Which brands hold their value the longest?
   - Will X brand's car keep its value compared to Y brand's car until Y's car shows enough flaws?
   - Can I estimate a fair market price for a car based on key attributes?  
   - Are some car listings significantly overpriced or underpriced compared to the estimated market price?  

5. **Findings & Conclusions:** Summarize the key takeaways.  

##  Example Analysis & What I Expect to Find  
As an example, I might create a scatter plot to see if cars with more mileage are always cheaper. 
**"The price sensitivity to mileage changes across different car brands, with luxury and performance brands showing lower decrease per kilometer compared to economy brands."**  

## Possible Future Improvements  
- Collecting data from more websites to get better results  
- Using machine learning to predict car prices based on the data  
- Adding extra details like service history and location-based price differences  
