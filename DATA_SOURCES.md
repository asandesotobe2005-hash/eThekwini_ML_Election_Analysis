 Data Sources



1. IEC 2021 eThekwini Local Government Election Results



\*\*Dataset:\*\* `ETH.csv`



\*\*Source:\*\* https://results.elections.org.za/home/LGEPublicReports/1091/Downloadable%20Party%20Results/KN/ETH.csv



The dataset contains the 2021 Local Government Election results for eThekwini Metropolitan Municipality. It includes voting districts, voting stations, registered voters, ballot types, spoilt votes, political parties and total valid votes.



\*\*Official source:\*\* https://www.elections.org.za/



The 2021 PR results were used as the primary party-level electoral measure for the metro-level analysis. Ward ballot results were kept separate and were used when examining ward-level constituency results.



\---



\## 2. IEC 2016 eThekwini Local Government Election Results



\*\*Dataset:\*\* `ETH (2).csv`



\*\*Source:\*\* https://results.elections.org.za/home/LGEPublicReports/402/Downloadable%20Party%20Results/KN/ETH.csv



The dataset contains the 2016 Local Government Election results for eThekwini Metropolitan Municipality.



The 2016 results were used as the historical comparison period for the 2021 results and for calculating historical changes in party vote shares and voter turnout.



\*\*Official source:\*\* https://www.elections.org.za/



\---



\## 3. Stats SA Ward-level Small Area Population Estimates, 2022



\*\*Dataset:\*\* `PP\_Age Group\_27-10-2025.xlsx`



\*\*Source:\*\* Statistics South Africa (Stats SA)



The dataset provides ward-level small area population estimates based on Census 2011 and Census 2022. The selected spreadsheet contains population estimates by age group.



The age-group data was used to create demographic features including:



\* Youth population aged 0–24

\* Working-age population aged 25–64

\* Older population aged 65+

\* Youth share

\* Working-age share

\* Older population share



\*\*Official product page:\*\* https://www.statssa.gov.za/?p=18967



\*\*Direct dataset download:\*\* https://www.statssa.gov.za/wp-content/uploads/2025/11/Ward-Product\_Locked-spreadsheets.zip



\*\*Technical documentation:\*\* https://www.statssa.gov.za/wp-content/uploads/2025/11/Ward-statistical-product-technical-note.pdf



\---



\## Geographic Integration



The IEC datasets contain eThekwini ward codes in the form:



`59500001` to `59500111`



The Stats SA ward-level data was filtered to the eThekwini ward-code range beginning with `595`.



The 2016 and 2021 IEC datasets contained 110 wards in common. The additional 2021 ward was excluded from historical ward-to-ward comparisons so that the comparison remained geographically defensible.



The three detailed wards selected for analysis were:



\* Ward 59500001

\* Ward 59500026

\* Ward 59500036



All three wards are included in the 110 wards common to the 2016 and 2021 datasets.



\---



\## Data Usage Note



The datasets are used for academic examination and analytical purposes. Users of this repository should consult the original IEC and Stats SA sources for the authoritative datasets and documentation.



The 2026 electoral results presented by the project are machine-learning scenario estimates and are not official IEC election results.



