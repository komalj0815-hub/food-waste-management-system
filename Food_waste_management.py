import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# -------------------------------
# PAGE CONFIG
# -------------------------------

st.set_page_config(
    page_title="Local Food Wastage Management System",
    page_icon="🍲",
    layout="wide"
)

# -------------------------------
# DATABASE CONNECTION
# -------------------------------

conn = sqlite3.connect(
    "food_wastage.db",
    check_same_thread=False
)

# -------------------------------
# LOAD TABLES
# -------------------------------

providers = pd.read_sql(
    "SELECT * FROM Providers",
    conn
)

receivers = pd.read_sql(
    "SELECT * FROM Receivers",
    conn
)

food = pd.read_sql(
    "SELECT * FROM Food_Listings",
    conn
)

claims = pd.read_sql(
    "SELECT * FROM Claims",
    conn
)

# -------------------------------
# SIDEBAR
# -------------------------------

st.sidebar.title("🍲 Food Waste Management")

page = st.sidebar.selectbox(
    "Select Page",
    [
        "Dashboard",
        "Food Listings",
        "Provider Contacts",
        "SQL Analysis",
        "CRUD Operations"
    ]
)

# =====================================================
# DASHBOARD
# =====================================================

if page == "Dashboard":

    st.title("Local Food Wastage Management System")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Providers",
        providers["Provider_ID"].nunique()
    )

    col2.metric(
        "Total Receivers",
        receivers["Receiver_ID"].nunique()
    )

    col3.metric(
        "Food Listings",
        food["Food_ID"].nunique()
    )

    col4.metric(
        "Total Claims",
        claims["Claim_ID"].nunique()
    )

    st.markdown("---")

    c1, c2 = st.columns(2)

    with c1:

        st.subheader("Food Type Distribution")

        fig, ax = plt.subplots()

        food["Food_Type"].value_counts().plot(
            kind="bar",
            ax=ax
        )

        plt.xticks(rotation=45)

        st.pyplot(fig)

    with c2:

        st.subheader("Meal Type Distribution")

        fig, ax = plt.subplots()

        food["Meal_Type"].value_counts().plot(
            kind="bar",
            ax=ax
        )

        plt.xticks(rotation=45)

        st.pyplot(fig)

    c3, c4 = st.columns(2)

    with c3:

        st.subheader("Provider Type Distribution")

        fig, ax = plt.subplots()

        providers["Type"].value_counts().plot(
            kind="bar",
            ax=ax
        )

        plt.xticks(rotation=45)

        st.pyplot(fig)

    with c4:

        st.subheader("Claim Status Distribution")

        status = claims["Status"].value_counts()

        fig, ax = plt.subplots()

        ax.pie(
            status,
            labels=status.index,
            autopct="%1.1f%%"
        )

        st.pyplot(fig)

# =====================================================
# FOOD LISTINGS
# =====================================================

elif page == "Food Listings":

    st.header("Food Listings")

    city = st.selectbox(
        "Location",
        ["All"] + sorted(food["Location"].unique().tolist())
    )

    food_type = st.selectbox(
        "Food Type",
        ["All"] + sorted(food["Food_Type"].unique().tolist())
    )

    meal_type = st.selectbox(
        "Meal Type",
        ["All"] + sorted(food["Meal_Type"].unique().tolist())
    )

    filtered = food.copy()

    if city != "All":
        filtered = filtered[
            filtered["Location"] == city
        ]

    if food_type != "All":
        filtered = filtered[
            filtered["Food_Type"] == food_type
        ]

    if meal_type != "All":
        filtered = filtered[
            filtered["Meal_Type"] == meal_type
        ]

    st.dataframe(
        filtered,
        use_container_width=True
    )

# =====================================================
# PROVIDER CONTACTS
# =====================================================

elif page == "Provider Contacts":

    st.header("Provider Contact Details")

    city = st.selectbox(
        "Select City",
        ["All"] + sorted(providers["City"].unique().tolist())
    )

    provider_df = providers.copy()

    if city != "All":

        provider_df = provider_df[
            provider_df["City"] == city
        ]

    st.dataframe(
        provider_df[
            [
                "Name",
                "Type",
                "City",
                "Contact"
            ]
        ],
        use_container_width=True
    )

# =====================================================
# SQL ANALYSIS
# =====================================================

elif page == "SQL Analysis":

    st.header("SQL Query Results")

    query_name = st.selectbox(
        "Select Query",
        [
            "Q1 Providers per City",
            "Q2 Receivers per City",
            "Q3 Provider Type Contribution",
            "Q4 Provider Contacts",
            "Q5 Top Receivers",
            "Q6 Total Food Available",
            "Q7 City With Most Listings",
            "Q8 Most Available Food Types",
            "Q9 Claims Per Food Item",
            "Q10 Highest Successful Claims",
            "Q11 Claim Status Percentage",
            "Q12 Average Quantity Claimed",
            "Q13 Most Claimed Meal Type",
            "Q14 Total Quantity By Provider",
            "Q15 Top Providers By Listings"
        ]
    )

    queries = {

        "Q1 Providers per City":
        """
        SELECT City,
        COUNT(*) AS Providers
        FROM Providers
        GROUP BY City
        ORDER BY Providers DESC
        """,

        "Q2 Receivers per City":
        """
        SELECT City,
        COUNT(*) AS Receivers
        FROM Receivers
        GROUP BY City
        ORDER BY Receivers DESC
        """,

        "Q3 Provider Type Contribution":
        """
        SELECT Provider_Type,
        SUM(Quantity) AS Total_Quantity
        FROM Food_Listings
        GROUP BY Provider_Type
        ORDER BY Total_Quantity DESC
        """,

        "Q4 Provider Contacts":
        """
        SELECT Name,
        Contact,
        City
        FROM Providers
        """,

        "Q5 Top Receivers":
        """
        SELECT r.Name,
        COUNT(c.Claim_ID) AS Total_Claims
        FROM Claims c
        JOIN Receivers r
        ON c.Receiver_ID=r.Receiver_ID
        GROUP BY r.Name
        ORDER BY Total_Claims DESC
        """,

        "Q6 Total Food Available":
        """
        SELECT SUM(Quantity)
        AS Total_Food
        FROM Food_Listings
        """,

        "Q7 City With Most Listings":
        """
        SELECT Location,
        COUNT(*) AS Listings
        FROM Food_Listings
        GROUP BY Location
        ORDER BY Listings DESC
        """,

        "Q8 Most Available Food Types":
        """
        SELECT Food_Type,
        COUNT(*) AS Frequency
        FROM Food_Listings
        GROUP BY Food_Type
        ORDER BY Frequency DESC
        """,

        "Q9 Claims Per Food Item":
        """
        SELECT f.Food_Name,
        COUNT(c.Claim_ID) AS Claims
        FROM Food_Listings f
        LEFT JOIN Claims c
        ON f.Food_ID=c.Food_ID
        GROUP BY f.Food_Name
        ORDER BY Claims DESC
        """,

        "Q10 Highest Successful Claims":
        """
        SELECT p.Name,
        COUNT(*) AS Successful_Claims
        FROM Claims c
        JOIN Food_Listings f
        ON c.Food_ID=f.Food_ID
        JOIN Providers p
        ON f.Provider_ID=p.Provider_ID
        WHERE c.Status='Completed'
        GROUP BY p.Name
        ORDER BY Successful_Claims DESC
        """,

        "Q11 Claim Status Percentage":
        """
        SELECT Status,
        ROUND(
        COUNT(*)*100.0/
        (SELECT COUNT(*) FROM Claims),2
        ) AS Percentage
        FROM Claims
        GROUP BY Status
        """,

        "Q12 Average Quantity Claimed":
        """
        SELECT r.Name,
        ROUND(AVG(f.Quantity),2) AS Avg_Quantity
        FROM Claims c
        JOIN Food_Listings f
        ON c.Food_ID=f.Food_ID
        JOIN Receivers r
        ON c.Receiver_ID=r.Receiver_ID
        GROUP BY r.Name
        ORDER BY Avg_Quantity DESC
        """,

        "Q13 Most Claimed Meal Type":
        """
        SELECT f.Meal_Type,
        COUNT(*) AS Claims
        FROM Claims c
        JOIN Food_Listings f
        ON c.Food_ID=f.Food_ID
        GROUP BY f.Meal_Type
        ORDER BY Claims DESC
        """,

        "Q14 Total Quantity By Provider":
        """
        SELECT p.Name,
        SUM(f.Quantity) AS Total_Donated
        FROM Providers p
        JOIN Food_Listings f
        ON p.Provider_ID=f.Provider_ID
        GROUP BY p.Name
        ORDER BY Total_Donated DESC
        """,

        "Q15 Top Providers By Listings":
        """
        SELECT p.Name,
        COUNT(f.Food_ID) AS Listings
        FROM Providers p
        JOIN Food_Listings f
        ON p.Provider_ID=f.Provider_ID
        GROUP BY p.Name
        ORDER BY Listings DESC
        """
    }

    result = pd.read_sql(
        queries[query_name],
        conn
    )

    st.dataframe(
        result,
        use_container_width=True
    )

# =====================================================
# CRUD OPERATIONS
# =====================================================

elif page == "CRUD Operations":

    st.header("Food Listing Management")

    operation = st.radio(
        "Choose Operation",
        ["Add Food", "Delete Food"]
    )

    if operation == "Add Food":

        food_name = st.text_input("Food Name")

        quantity = st.number_input(
            "Quantity",
            min_value=1
        )

        provider_id = st.number_input(
            "Provider ID",
            min_value=1
        )

        location = st.text_input("Location")
        food_type = st.text_input("Food Type")
        meal_type = st.text_input("Meal Type")

        if st.button("Add Record"):

            cursor = conn.cursor()

            cursor.execute("""
            INSERT INTO Food_Listings
            (
                Food_Name,
                Quantity,
                Provider_ID,
                Location,
                Food_Type,
                Meal_Type
            )
            VALUES (?,?,?,?,?,?)
            """,
            (
                food_name,
                quantity,
                provider_id,
                location,
                food_type,
                meal_type
            ))

            conn.commit()

            st.success(
                "Food Listing Added Successfully"
            )

    else:

        food_id = st.number_input(
            "Enter Food ID",
            min_value=1
        )

        if st.button("Delete Record"):

            cursor = conn.cursor()

            cursor.execute("""
            DELETE FROM Food_Listings
            WHERE Food_ID=?
            """,
            (food_id,)
            )

            conn.commit()

            st.success(
                "Food Listing Deleted Successfully"
            )
