\# eThekwini Metropolitan Municipality Machine Learning Election Analysis



\## Technical Programming 2 Examination Project



This project develops a machine-learning and data-analysis solution for the eThekwini Metropolitan Municipality in KwaZulu-Natal, South Africa.



The project combines historical Local Government Election results from the Electoral Commission of South Africa (IEC) with ward-level demographic information from Statistics South Africa (Stats SA).



\## Project Objectives



The solution addresses the following analytical questions:



1\. Which relevant party is projected to receive the largest aggregate vote total or vote share?

2\. Which relevant party is projected to lead in each of three selected wards?

3\. What vote total and vote share are projected for each relevant party?

4\. What voter turnout is projected for the selected municipality?



The results are presented as machine-learning scenario estimates and should not be interpreted as official election results or as a prediction of which party will govern the municipality.



\## Datasets



The project uses three datasets:



\### IEC 2021



`data/ETH.csv`



2021 eThekwini Local Government Election results.



\### IEC 2016



`data/ETH (2).csv`



2016 eThekwini Local Government Election results.



\### Stats SA Age Group Data



`data/PP\_Age Group\_27-10-2025.xlsx`



Ward-level age-group population estimates from Statistics South Africa.



Detailed source information is provided in `DATA\_SOURCES.md`.



\## Main Analysis



The project follows the complete data science workflow:



1\. Dataset selection and justification

2\. Data loading

3\. Data understanding

4\. Data preprocessing

5\. Exploratory Data Analysis

6\. Feature engineering

7\. Machine learning implementation

8\. Model validation

9\. Model evaluation

10\. Model improvement

11\. Ward-level analysis

12\. Voter turnout analysis

13\. 2026 scenario forecasting

14\. K-Means clustering

15\. Streamlit dashboard development

16\. Complexity analysis

17\. Code organization and documentation

18\. Conclusion



\## Machine Learning Models



Three classification algorithms were evaluated:



\* Regularized Logistic Regression

\* Decision Tree

\* Random Forest



Random Forest was selected as the final classification model because it achieved the highest mean cross-validation accuracy among the tested models.



\### Final Results



\*\*Mean cross-validation accuracy:\*\* 97.2%



\*\*Test accuracy:\*\* 94.1%



\*\*Test precision:\*\* 95.1%



\*\*Test recall:\*\* 94.1%



\*\*Test F1 score:\*\* 94.3%



\## 2026 Scenario Forecast



The final scenario forecast produced by the analysis is:



| Party         | Projected Votes | Projected Share |

| ------------- | --------------: | --------------: |

| ANC           |         284,608 |          29.63% |

| DA            |         204,970 |          21.34% |

| EFF           |         166,811 |          17.37% |

| IFP           |         112,493 |          11.71% |

| Other Parties |         191,663 |          19.95% |



The projected voter turnout is:



\*\*50.31%\*\*



Estimated projected voters:



\*\*960,545\*\*



No single party reaches 50% in the scenario forecast. Coalition arrangements could therefore be relevant, but vote share alone cannot determine council seat allocation or governance outcomes.



\## Three Selected Wards



Three wards were selected from the 110 wards common to the 2016 and 2021 datasets.



| Ward     | Type         | 2016 Leader | 2021 Leader | Projected 2026 Leader |

| -------- | ------------ | ----------- | ----------- | --------------------- |

| 59500001 | ANC-dominant | ANC         | ANC         | ANC                   |

| 59500026 | Competitive  | ANC         | DA          | ANC                   |

| 59500036 | DA-dominant  | DA          | DA          | DA                    |



The selected wards were chosen to represent different electoral profiles while maintaining geographical comparability across the historical datasets.



\## Clustering



K-Means clustering was applied to ward-level electoral and demographic characteristics.



The optimal number of clusters was selected using the silhouette score.



\*\*Optimal K:\*\* 2



\*\*Silhouette score:\*\* 0.4771



Cluster 0 contains 72 wards and has substantially higher average ANC support.



Cluster 1 contains 38 wards and has substantially higher average DA support.



\## Voter Turnout



Historical PR turnout:



\* 2016: 59.10%

\* 2021: 41.53%



A midpoint scenario estimate was used because only two historical election observations were available.



\*\*Projected 2026 turnout: 50.31%\*\*



\*\*Projected voters: 960,545\*\*



This is a scenario estimate and is not an official IEC turnout forecast.



\## Streamlit Dashboard



The project includes an interactive Streamlit dashboard.



The dashboard provides:



\* 2026 Forecast

\* Voter Turnout

\* Three Selected Wards

\* Historical Comparison

\* Ward Clusters

\* Model Performance



\### Running the Dashboard



Install the required packages:



```bash

pip install -r requirements.txt

```



Run the application:



```bash

python -m streamlit run app.py

```



The dashboard will normally open at:



`http://localhost:8501`



\## Complexity Analysis



The project analyses the computational complexity of the main algorithms:



\* Logistic Regression: approximately O(n × p × i)

\* Decision Tree: approximately O(n × p × log(n))

\* Random Forest: approximately O(t × n × p × log(n))

\* K-Means: approximately O(n × k × p × i)



The dataset used for the final ward-level modelling contains 110 geographically comparable wards and 9 classification features, making the selected algorithms computationally practical on a standard computer.



\## Limitations



The forecasting component has an important limitation: only two historical election periods, 2016 and 2021, are available for the analysis.



Therefore, the 2026 results should be interpreted as scenario-based machine-learning estimates rather than guaranteed future election results.



The classification target also contains a small number of IFP-leading wards, while EFF does not lead any ward among the four selected parties in the 2021 data. This creates class-imbalance limitations.



The analysis also does not determine which party will govern the municipality. Governance depends on electoral seat allocation, council composition, coalition agreements and other political factors.



\## Author



\*\*Asande Sibiya\*\*



Technical Programming 2



Mangosuthu University of Technology



Examination Project — 2026



