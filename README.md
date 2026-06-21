# 🍲 Local Food Wastage Management System

## 📌 Project Overview

The Local Food Wastage Management System is designed to reduce food waste by connecting food providers with individuals and organizations in need. The platform allows providers to list surplus food and enables receivers to claim available food items efficiently.

This project helps improve food redistribution, minimize wastage, and support community welfare through data-driven insights and an interactive web application.

---

## 🎯 Objectives

- Reduce food wastage through efficient redistribution.
- Connect food providers with receivers.
- Track food donations and claims.
- Analyze food distribution trends using SQL.
- Develop an interactive Streamlit application for users.

---

## 🛠️ Technologies Used

- Python
- SQL (SQLite)
- Pandas
- Streamlit
- Matplotlib
- GitHub

---

## 📂 Dataset Information

The project uses four datasets:

### Providers
Contains details of food providers.

Columns:
- Provider_ID
- Name
- Type
- Address
- City
- Contact

### Receivers
Contains details of food receivers.

Columns:
- Receiver_ID
- Name
- Type
- City
- Contact

### Food Listings
Contains information about available food items.

Columns:
- Food_ID
- Food_Name
- Quantity
- Expiry_Date
- Provider_ID
- Provider_Type
- Location
- Food_Type
- Meal_Type

### Claims
Contains records of food claims.

Columns:
- Claim_ID
- Food_ID
- Receiver_ID
- Status
- Timestamp

---

## 🧹 Data Cleaning

The datasets were cleaned using Python and Pandas.

Steps performed:

- Checked missing values
- Removed duplicate records
- Standardized text columns
- Converted date columns to datetime format
- Validated unique IDs

---

## 🗄️ Database Design

The project uses SQLite database.

Tables:

- Providers
- Receivers
- Food_Listings
- Claims

Relationships:

Providers → Food Listings

Food Listings → Claims

Receivers → Claims

---

## 📊 SQL Analysis

The project answers key business questions such as:

1. Number of providers in each city
2. Number of receivers in each city
3. Provider type contributing the most food
4. Provider contact details
5. Top receivers by claims
6. Total food available
7. City with highest food listings
8. Most common food types
9. Claims per food item
10. Provider with highest successful claims
11. Claim status percentage
12. Average quantity claimed per receiver
13. Most claimed meal type
14. Total quantity donated by each provider
15. Top providers by listings

---

## 📈 Exploratory Data Analysis (EDA)

Visualizations created:

- Provider Type Distribution
- Food Type Distribution
- Meal Type Distribution
- Claim Status Distribution
- Top Cities by Food Listings
- Top Providers by Quantity Donated
- Claims Trend Analysis

---

## 💻 Streamlit Application Features

### Dashboard
- Total Providers
- Total Receivers
- Total Food Listings
- Total Claims

### Food Listings
- Filter by Location
- Filter by Food Type
- Filter by Meal Type

### Provider Contacts
- Provider details
- Contact information
- City-wise filtering

### SQL Analysis
- Display outputs of 15 SQL queries

### CRUD Operations
- Add Food Listings
- Delete Food Listings

---

## 🚀 How to Run the Project

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/food-waste-management-system.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit App

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```text
Food_Waste_Management/

│
├── app.py
├── food_wastage.db
├── requirements.txt
├── README.md
│
├── providers_clean.csv
├── receivers_clean.csv
├── food_clean.csv
└── claims_clean.csv
```

---

## 📌 Key Insights

- Certain provider types contribute significantly more food than others.
- Food claims are concentrated in specific cities.
- Some meal types experience higher demand.
- The platform effectively supports food redistribution and waste reduction.

---

## 👩‍💻 Author

Komal

Aspiring Data Analyst

Skills:
- SQL
- Python
- Power BI
- Streamlit
- Data Analytics
