import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="eThekwini Election Forecast",
    page_icon="📊",
    layout="wide"
)

# ============================================================
# TITLE AND INTRODUCTION
# ============================================================

st.title("📊 eThekwini Metropolitan Municipality")
st.subheader("Machine Learning Election Analysis and 2026 Forecast")

st.markdown("""
This dashboard presents the results of a machine-learning analysis
of eThekwini Metropolitan Municipality using historical IEC election
results from 2016 and 2021 together with Stats SA ward-level
demographic data.
""")

st.warning("""
**Important:** The 2026 figures shown in this dashboard are
scenario-based machine-learning estimates. They should not be
interpreted as guaranteed election results or as a prediction
of which party will govern the municipality.
""")

# ============================================================
# SIDEBAR MENU
# ============================================================

st.sidebar.title("Dashboard Menu")

section = st.sidebar.radio(
    "Select Analysis",
    [
        "2026 Forecast",
        "Voter Turnout",
        "Three Selected Wards",
        "Historical Comparison",
        "Ward Clusters",
        "Model Performance"
    ]
)

# ============================================================
# 2026 FORECAST DATA
# ============================================================

forecast_data = pd.DataFrame({
    "Party": [
        "ANC",
        "DA",
        "EFF",
        "IFP",
        "Other Parties"
    ],
    "Projected Votes": [
        284608,
        204970,
        166811,
        112493,
        191663
    ],
    "Projected Share (%)": [
        29.63,
        21.34,
        17.37,
        11.71,
        19.95
    ]
})

# ============================================================
# THREE SELECTED WARDS
# ============================================================

ward_data = pd.DataFrame({
    "Ward": [
        "59500001",
        "59500026",
        "59500036"
    ],
    "Ward Type": [
        "ANC-dominant",
        "Competitive",
        "DA-dominant"
    ],
    "2016 Leader": [
        "ANC",
        "ANC",
        "DA"
    ],
    "2021 Leader": [
        "ANC",
        "DA",
        "DA"
    ],
    "Projected 2026 Leader": [
        "ANC",
        "ANC",
        "DA"
    ],
    "Model Confidence (%)": [
        99.21,
        78.44,
        96.52
    ]
})

# ============================================================
# HISTORICAL DATA
# ============================================================

historical_data = pd.DataFrame({
    "Party": [
        "ANC",
        "DA",
        "EFF",
        "IFP"
    ],
    "2016 Votes": [
        652891,
        304206,
        40087,
        47260
    ],
    "2021 Votes": [
        329307,
        203980,
        83699,
        57722
    ]
})

# ============================================================
# MODEL PERFORMANCE DATA
# ============================================================

model_data = pd.DataFrame({
    "Model": [
        "Regularized Logistic Regression",
        "Decision Tree",
        "Random Forest"
    ],
    "Validation Accuracy": [
        0.941,
        0.941,
        0.941
    ],
    "Validation Precision": [
        0.951,
        0.946,
        0.946
    ],
    "Validation Recall": [
        0.941,
        0.941,
        0.941
    ],
    "Validation F1": [
        0.942,
        0.939,
        0.939
    ],
    "Mean CV Accuracy": [
        0.944,
        0.963,
        0.972
    ]
})

# ============================================================
# CLUSTER DATA
# ============================================================

cluster_data = pd.DataFrame({
    "Cluster": [
        "Cluster 0",
        "Cluster 1"
    ],
    "Number of Wards": [
        72,
        38
    ],
    "ANC Share (%)": [
        56.93,
        20.34
    ],
    "DA Share (%)": [
        6.55,
        54.40
    ],
    "EFF Share (%)": [
        15.68,
        4.45
    ],
    "IFP Share (%)": [
        10.18,
        4.48
    ],
    "Youth Share (%)": [
        40.62,
        29.36
    ],
    "Older Share (%)": [
        4.68,
        11.42
    ]
})

# ============================================================
# SECTION 1 — 2026 FORECAST
# ============================================================

if section == "2026 Forecast":

    st.header("📊 2026 Projected Election Results")

    st.markdown("""
    The following results are the final metro-level 2026
    scenario estimates produced by the forecasting analysis.
    """)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Projected Voters", "960,545")
    col2.metric("Top Projected Party", "ANC")
    col3.metric("ANC Projected Share", "29.63%")
    col4.metric("Modelled Parties", "4")

    st.divider()

    st.subheader("Projected Party Vote Totals and Shares")

    st.dataframe(
        forecast_data,
        width="stretch",
        hide_index=True
    )

    st.subheader("Projected 2026 Vote Share")

    chart_data = forecast_data.set_index("Party")[
        "Projected Share (%)"
    ]

    st.bar_chart(chart_data)

    st.info("""
    No single party reaches 50% of the projected vote share.
    Coalition arrangements could therefore be relevant.

    However, coalition formation cannot be confirmed from vote
    shares alone because council seat allocation and all parties
    must also be considered.
    """)

# ============================================================
# SECTION 2 — VOTER TURNOUT
# ============================================================

elif section == "Voter Turnout":

    st.header("🗳️ Projected Voter Turnout")

    st.markdown("""
    Turnout is estimated using the historical 2016 and 2021
    eThekwini PR turnout rates.

    Because only two historical election observations are available,
    the midpoint between the two rates is used as a scenario estimate.
    """)

    col1, col2, col3 = st.columns(3)

    col1.metric("Registered Voters", "1,909,125")
    col2.metric("Projected Turnout", "50.31%")
    col3.metric("Projected Voters", "960,545")

    st.divider()

    turnout_data = pd.DataFrame({
        "Election": [
            "2016",
            "2021",
            "2026 Projected"
        ],
        "Turnout (%)": [
            59.10,
            41.53,
            50.31
        ]
    })

    st.subheader("Historical and Projected Turnout")

    st.dataframe(
        turnout_data,
        width="stretch",
        hide_index=True
    )

    st.line_chart(
        turnout_data.set_index("Election")
    )

    st.write("**2016 turnout:** 59.10%")
    st.write("**2021 turnout:** 41.53%")
    st.write("**Projected 2026 turnout:** 50.31%")
    st.write("**Projected voters:** 960,545")

    st.caption(
        "This is a scenario-based turnout estimate, not an official IEC forecast."
    )

# ============================================================
# SECTION 3 — THREE SELECTED WARDS
# ============================================================

elif section == "Three Selected Wards":

    st.header("🏘️ Three Selected Ward Projections")

    st.markdown("""
    Three wards were selected from the **110 wards common to both
    the 2016 and 2021 election datasets**.

    This makes the historical comparison geographically defensible.

    The three wards represent:

    - an ANC-dominant ward
    - a highly competitive ward
    - a DA-dominant ward
    """)

    st.dataframe(
        ward_data,
        width="stretch",
        hide_index=True
    )

    st.divider()

    selected_ward = st.selectbox(
        "Select a ward for detailed analysis",
        ward_data["Ward"]
    )

    selected = ward_data[
        ward_data["Ward"] == selected_ward
    ].iloc[0]

    st.subheader(f"Ward {selected_ward}")

    col1, col2, col3 = st.columns(3)

    col1.metric("2016 Leader", selected["2016 Leader"])
    col2.metric("2021 Leader", selected["2021 Leader"])
    col3.metric(
        "Projected 2026 Leader",
        selected["Projected 2026 Leader"]
    )

    st.metric(
        "Model Confidence",
        f"{selected['Model Confidence (%)']:.2f}%"
    )

    if selected_ward == "59500001":

        st.info("""
        Ward 59500001 was selected as an ANC-dominant ward.

        The model projects ANC as the leading party with
        approximately 99.21% model probability.
        """)

    elif selected_ward == "59500026":

        st.info("""
        Ward 59500026 was selected because it was highly competitive.

        In the observed 2021 PR results, DA led ANC by approximately
        1.6 percentage points.

        The model projects ANC as the 2026 ward leader, showing that
        the model is not simply copying the 2021 result.
        """)

    elif selected_ward == "59500036":

        st.info("""
        Ward 59500036 was selected as a DA-dominant ward.

        The model projects DA as the leading party with approximately
        96.52% model probability.
        """)

# ============================================================
# SECTION 4 — HISTORICAL COMPARISON
# ============================================================

elif section == "Historical Comparison":

    st.header("📈 2016 vs 2021 Historical Election Results")

    st.markdown("""
    Historical PR results are compared for the four parties used
    consistently in the machine-learning analysis.
    """)

    st.dataframe(
        historical_data,
        width="stretch",
        hide_index=True
    )

    st.subheader("Historical Party Vote Totals")

    chart_data = historical_data.set_index("Party")[
        ["2016 Votes", "2021 Votes"]
    ]

    st.bar_chart(chart_data)

    st.subheader("Historical Vote Share Comparison")

    total_2016 = historical_data["2016 Votes"].sum()
    total_2021 = historical_data["2021 Votes"].sum()

    share_comparison = pd.DataFrame({
        "Party": historical_data["Party"],
        "2016 Share (%)":
            historical_data["2016 Votes"] /
            total_2016 * 100,
        "2021 Share (%)":
            historical_data["2021 Votes"] /
            total_2021 * 100
    })

    st.dataframe(
        share_comparison.round(2),
        width="stretch",
        hide_index=True
    )

# ============================================================
# SECTION 5 — WARD CLUSTERS
# ============================================================

elif section == "Ward Clusters":

    st.header("🔵 Ward Clustering Analysis")

    st.markdown("""
    K-Means clustering was used to group eThekwini wards with
    similar electoral and demographic characteristics.

    The number of clusters was selected using the silhouette score.
    The highest silhouette score was obtained with **K = 2**.
    """)

    col1, col2, col3 = st.columns(3)

    col1.metric("Number of Clusters", "2")
    col2.metric("Cluster 0 Wards", "72")
    col3.metric("Cluster 1 Wards", "38")

    st.metric("Silhouette Score", "0.4771")

    st.divider()

    st.subheader("Cluster Profiles")

    st.dataframe(
        cluster_data,
        width="stretch",
        hide_index=True
    )

    st.subheader("Average ANC and DA Share by Cluster")

    fig, ax = plt.subplots(figsize=(9, 5))

    ax.bar(
        cluster_data["Cluster"],
        cluster_data["ANC Share (%)"],
        label="ANC"
    )

    ax.bar(
        cluster_data["Cluster"],
        cluster_data["DA Share (%)"],
        bottom=cluster_data["ANC Share (%)"],
        label="DA"
    )

    ax.set_xlabel("Cluster")
    ax.set_ylabel("Average Vote Share (%)")
    ax.set_title("Average ANC and DA Share by Ward Cluster")
    ax.legend()

    st.pyplot(fig)

    st.info("""
    Cluster 0 contains wards with substantially higher average ANC,
    EFF and IFP support.

    Cluster 1 contains wards with substantially higher average
    DA support.

    The clustering identifies similarities between wards and
    does not establish causation.
    """)

# ============================================================
# SECTION 6 — MODEL PERFORMANCE
# ============================================================

elif section == "Model Performance":

    st.header("🤖 Machine Learning Model Performance")

    st.markdown("""
    Three classification models were evaluated for predicting
    the leading party at ward level:

    - Regularized Logistic Regression
    - Decision Tree
    - Random Forest
    """)

    st.dataframe(
        model_data.round(3),
        width="stretch",
        hide_index=True
    )

    st.divider()

    st.subheader("Cross-Validation Accuracy")

    cv_chart = model_data.set_index("Model")[
        "Mean CV Accuracy"
    ]

    st.bar_chart(cv_chart)

    st.success("""
    **Selected model: Random Forest**

    Random Forest achieved the highest mean cross-validation
    accuracy of **97.2%** among the tested classification models.
    """)

    st.subheader("Final Random Forest Test Performance")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Test Accuracy", "94.1%")
    col2.metric("Test Precision", "95.1%")
    col3.metric("Test Recall", "94.1%")
    col4.metric("Test F1 Score", "94.3%")

    st.subheader("Confusion Matrix")

    confusion_data = pd.DataFrame(
        [
            [11, 0, 0],
            [1, 4, 0],
            [0, 0, 1]
        ],
        columns=[
            "Predicted ANC",
            "Predicted DA",
            "Predicted IFP"
        ],
        index=[
            "Actual ANC",
            "Actual DA",
            "Actual IFP"
        ]
    )

    st.dataframe(
        confusion_data,
        width="stretch"
    )

    st.caption("""
    The classification target contains ANC, DA and IFP.

    EFF had no ward in which it was the leading party among the
    four selected parties in the 2021 data, so EFF does not appear
    as a classification class.
    """)

# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Development Software 2 | Mangosuthu University of Technology | "
    "eThekwini Machine Learning Election Analysis"
)