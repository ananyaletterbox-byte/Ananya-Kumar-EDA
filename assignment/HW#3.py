#ChatGPT was used as a guide

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



#QUESTION 2

#load
df = pd.read_csv('./ForeignGifts_edu.csv', low_memory=False)

#quick look
df.head()
df.info()

#histogram
plt.figure()
plt.hist(df["Foreign Gift Amount"], bins=50)
plt.xlabel("Foreign Gift Amount")
plt.ylabel("Frequency")
plt.title("Histogram of Foreign Gift Amount")
plt.show()

#2.2 ANSWER: this is a highly right skewed dataset, meaning most gifts are less expensive expensive, with a few gits on the slightly more expensive amount to create the tail. No gift exceeds around 0.1 ($100,000)

#gift types
gift_counts = df["Gift Type"].value_counts()
gift_props = gift_counts / gift_counts.sum()

gift_counts
gift_props

#2.3 ANSWER:
#contract: 61.20%, real estate: 0.039%, monetary gift: 38.75%

#kernel density plot clean and log-transform
df_clean = df[df["Foreign Gift Amount"] > 0].copy()
df_clean["log_amount"] = np.log(df_clean["Foreign Gift Amount"])

#overall KDE
plt.figure()
sns.kdeplot(df_clean["log_amount"])
plt.xlabel("Log Foreign Gift Amount")
plt.title("KDE of Log Foreign Gift Amount")
plt.show()

#KDE of log(Foreign Gift Amount) conditional on Gift Type
plt.figure()
sns.kdeplot(
    data=df_clean,
    x="log_amount",
    hue="Gift Type",
    common_norm=False
)
plt.xlabel("Log Foreign Gift Amount")
plt.title("KDE of Log Foreign Gift Amount by Gift Type")
plt.show()

#2.4 ANSWER: monetary and contract are bimodal whereas real estate is unimodal; monetary gifts have the widest range whereeas real estate has the highest density point yet the narrowest range; contract is in the middle



#Top 15 countries by number of gifts
top_countries_count = (
    df["Country of Giftor"]
    .value_counts()
    .head(15)
)

top_countries_count

'''''
#2.5a ANSWER
in terms of number of gifts:
ENGLAND            3655
CHINA              2461
CANADA             2344
JAPAN              1896
SWITZERLAND        1676
SAUDI ARABIA       1610
FRANCE             1437
GERMANY            1394
HONG KONG          1080
SOUTH KOREA         811
QATAR               693
THE NETHERLANDS     512
KOREA               452
INDIA               434
TAIWAN              381
'''''

#Top 15 countries by total amount given
top_countries_amount = (
    df.groupby("Country of Giftor")["Foreign Gift Amount"]
    .sum()
    .sort_values(ascending=False)
    .head(15)
)

top_countries_amount

'''''
#2.5.b ANSWER:
in terms of amount given:
QATAR                   2706240869
ENGLAND                 1464906771
CHINA                   1237952112
SAUDI ARABIA            1065205930
BERMUDA                  899593972
CANADA                   898160656
HONG KONG                887402529
JAPAN                    655954776
SWITZERLAND              619899445
INDIA                    539556490
GERMANY                  442475605
UNITED ARAB EMIRATES     431396357
FRANCE                   405839396
SINGAPORE                401157692
AUSTRALIA                248409202
'''

#Top 15 institutions by total amount received
top_institutions = (
    df.groupby("Institution Name")["Foreign Gift Amount"]
    .sum()
    .sort_values(ascending=False)
    .head(15)
)

top_institutions

'''''
ANSWER 2.6.
Carnegie Mellon University                       1477922504
Cornell University                               1289937761
Harvard University                                954803610
Massachusetts Institute of Technology             859071692
Yale University                                   613441311
Texas A&M University                              521455050
Johns Hopkins University                          502409595
Northwestern University                           402316221
Georgetown University                             379950511
University of Chicago (The)                       364544338
University of Colorado Boulder                    360173159
Duke University                                   343699498
Brigham Young University                          323509863
Stanford University                               319561362
University of Texas MD Anderson Cancer Center     301527419
'''''

#Histogram of total amount received by all institutions
institution_totals = (
    df.groupby("Institution Name")["Foreign Gift Amount"]
    .sum()
)

plt.figure()
plt.hist(institution_totals, bins=50)
plt.xlabel("Total Amount Received")
plt.ylabel("Number of Institutions")
plt.title("Distribution of Total Amount Received by Institutions")
plt.show()


#Which giftors provide the most money?
top_giftors = (
    df.groupby("Giftor Name")["Foreign Gift Amount"]
    .sum()
    .sort_values(ascending=False)
    .head(15)
)

top_giftors

'''''
#2.7 ANSWER:
Qatar Foundation                       1166503744
Qatar Foundation/Qatar National Res     796197000
Qatar Foundation for Education          373945215
Anonymous                               338793629
Saudi Arabian Cultural Mission          275221475
HCL                                     190000000
Church of Jesus Christ of LDS           185203715
Emirates Institute for Advanced Sc      170641244
QIC                                     148355497
Anonymous #9                             96334996
Qatar National Research Fund             79021705
Government of Saudi Arabia               75192434
Contracting Party                        69996984
CMKL University                          67700000
Royal Embassy of Saudi Arabia            67062486
'''



#QUESTION 3:

# Load data
df = pd.read_csv("airbnb_hw (1).csv")

# Dimensions
print("Data dimensions (rows, columns):", df.shape)


# Variables
print("\nVariables:")
print(df.columns)


# First few rows
df.head()

'''''
#ANSWER 3.2: Data dimensions (rows, columns): (30478, 13)
#therefore, 30478 observations
#variables: 'Host Id', 'Host Since', 'Name', 'Neighbourhood ', 'Property Type',
       'Review Scores Rating (bin)', 'Room Type', 'Zipcode', 'Beds',
       'Number of Records', 'Number Of Reviews', 'Price',
       'Review Scores Rating'
'''

room_property_ct = pd.crosstab(df["Room Type"], df["Property Type"])
print(room_property_ct)
'''''
Property Type    Apartment  Bed & Breakfast  Boat  Bungalow  ...  Tent  Townhouse  Treehouse  Villa
Room Type                                                    ...                                   
Entire home/apt      15669               13     7         4  ...     0         83          0      4
Private room         10748              155     1         0  ...     4         52          1      4
Shared room            685               12     0         0  ...     0          1          3      0
'''
#ANSWER 3.a
#most rentals are apartments; vast majority are entire home/apt or private room
#shared rooms less common
#more niche types are rare
#only bed and breakfast private rooms are more common otherwise entire properties listings are more common



# histogram
print(df["Price"].describe())
plt.figure()
plt.hist(df["Price"], bins=50)
plt.xlabel("Price")
plt.ylabel("Count")
plt.title("Histogram of Price")
plt.show()
df["Price"].dtype

# Remove $ and commas if present, then convert
df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
)

df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

#kernel density estimate
sns.kdeplot(df['Price'], shade=True)
plt.title('Price Density')
plt.show()

#boxplot
sns.boxplot(x=df['Price'])
plt.title('Price Boxplot')
plt.show()

#statistical description
print(df['Price'].describe())
'''''
count    30478.000000
mean       163.589737
std        197.785454
min         10.000000
25%         80.000000
50%        125.000000
75%        195.000000
max      10000.000000
Name: Price, dtype: float64
'''
#ANSWER 3.4
#there are some outliers as seen in the boxplot and yes the values are pretty spread out which can cause scaling issues; logging will help with this

df['price_log'] = np.log(df['Price'] + 1)  # Add 1 to avoid log(0)

# Repeat visualizations
plt.hist(df['price_log'], bins=50, color='salmon')
plt.title('Log-Transformed Price Distribution')
plt.show()

sns.kdeplot(df['price_log'], shade=True)
plt.title('Log-Price Density')
plt.show()

sns.boxplot(x=df['price_log'])
plt.title('Log-Price Boxplot')
plt.show()

print(df['price_log'].describe())


#scatterplot of price_log vs beds
plt.figure(figsize=(8,6))
plt.scatter(df['Beds'], df['price_log'], alpha=0.5)
plt.xlabel('Number of Beds')
plt.ylabel('Log-Price')
plt.title('Price_log vs Beds')
plt.show()

#ANSWER 3.5.a
#positive correlation between number of beds and log_price so as one increases, so does the other; between 1-6 beds is where density mainly is; pretty high price variability with some outliers with properties at around 12-16 and also more non-linear patterns at these high bed counts

#price stats grouped
price_by_beds = df.groupby('Beds')['Price'].describe()
print(price_by_beds)

#ANSWER 3.5.b
#general trend is more beds is higher price; stats show high variability in higher bed counts and also small sample sizes makes the standard deviation greater bc extreme prices will more heavily impact the average
#median is usually lower than the mean, particularly for higher bed counts which means the data is right-skewed since outliers are increasing the mean



#scatterplot by room type and property type
plt.figure(figsize=(10,6))
sns.scatterplot(
    data=df, x='Beds', y='price_log',
    hue='Room Type', style='Property Type', alpha=0.6
)
plt.title('Price_log vs Beds by Room Type and Property Type')
plt.show()

#ANSWER 3.6.a
#majority of listings are for entire home/apt; each property has btwn 1-4 beds; there is weak positive correlation between number of beds and price_log; most common property type is apartment and then houses


#description
price_by_room_property = df.groupby(['Room Type','Property Type'])['Price'].describe()
print(price_by_room_property)

#ANSWER 3.6.b
# other" and villas property types in entire home/apt room types have the highest prices; "other" and "apartment" have the highest standard deviations meaning they have extreme out;iers; also B%B in shared rooms have high std dev; due to these outliers, median is more reliable bc outliers directly impact the mean which can mislead you when interpretating the data


#hexagonal jointplot with Seaborn
sns.jointplot(
    data=df, x='Beds', y='price_log', kind='hex', height=8, gridsize=25, cmap='viridis'
)
plt.show()

#ANSWER 3.7
#the data is mainly in the lower-left portion (0,1,2 beds with log_price at 4 and 6)
#this means that most of the data represents properties with few beds and lower prices so in plots 5 and 6, analysis should be focused on this area and any other datapoints may be outliers that skewing the data and could be misleading in analysis (less reliable)



#QUESTION 4:

# Load data
df = pd.read_csv("drilling_rigs.csv")

# Number of observations and variables
print("Shape (rows, columns):", df.shape)

#ANSWER 4.1:
#number of observations: 623
#number of variables: 10
#the columns that should be numeric are currently "object" which could be caused by commas or missing values
#the data can be cleaned by removing commas and whitespace, along with converting to numeric and filling/dropping missing values


# Variable names
print("\nColumns:")
print(df.columns)

# Data types
print("\nData types:")
print(df.dtypes)


# Look at first few rows
df.head()

numeric_cols = [
    "Crude Oil and Natural Gas Rotary Rigs in Operation, Onshore (Number of Rigs)",
    "Crude Oil and Natural Gas Rotary Rigs in Operation, Offshore (Number of Rigs)",
    "Active Well Service Rig Count (Number of Rigs)"
]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")
df = df.rename(columns={
    "Crude Oil and Natural Gas Rotary Rigs in Operation, Onshore (Number of Rigs)": "onshore",
    "Crude Oil and Natural Gas Rotary Rigs in Operation, Offshore (Number of Rigs)": "offshore",
    "Crude Oil and Natural Gas Rotary Rigs in Operation, Total (Number of Rigs)": "total_rigs",
    "Active Well Service Rig Count (Number of Rigs)": "active_rigs"
})
df["the_time"] = pd.to_datetime(df["Month"], format="mixed")


#ANSWER 4.3
#the rig count peaked at 1980s; general downward trend with a sharp decline at the 2000 year and then after 2014, the number of rigs decreased; reached its lowest point at 2020


# Sort by time (important for time series)
df = df.sort_values("time")

plt.figure()
plt.plot(
    df["time"],
    df["active_rigs"]
)
plt.xlabel("Time")
plt.ylabel("Number of Rigs")
plt.title("active_rigs")
plt.show()

df["rig_diff"] = df["active_rigs"].diff()

plt.figure()
plt.plot(df["time"], df["rig_diff"])
plt.axhline(0)
plt.xlabel("Time")
plt.ylabel("Change in Number of Rigs")
plt.title("First Difference of Active Well Service Rig Count")
plt.show()

df_long = df.melt(
    id_vars="time",
    value_vars=[
        "onshore",
        "offshore"
    ],
    var_name="Rig Type",
    value_name="Rig Count"
)

plt.figure()
for rig_type in df_long["Rig Type"].unique():
    subset = df_long[df_long["Rig Type"] == rig_type]
    plt.plot(subset["time"], subset["Rig Count"], label=rig_type)

plt.xlabel("Time")
plt.ylabel("Number of Rigs")
plt.title("Onshore vs Offshore Oil and Gas Rigs Over Time")
plt.legend()
plt.show()

#ANSWER 4.4: the data is pretty spread out; are pretty large negative spikes at 1980s and 2000s but once we hit 2010, the spikes are less extreme and it balances out a bit



































