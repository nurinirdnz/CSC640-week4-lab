# Tech Stack Evaluation

## Project

AI-Based Real-Time Classification and Prioritisation of Fire Hotspots for Transboundary Haze Risk in Sarawak

## Requirements that drive the decision

### Functional Requirements:

- FR1: The system shall fetch new satellite hotspot data automatically every 10 minutes
- FR2: The system shall keep only hotspots located in Sarawak and in West and Central Kalimantan.
- FR3: The system shall classify each hotspot as a persistent fire or a short-lived detection
- FR4: The system shall predict for each selected Sarawak monitoring station, whether the API will exceed 100 the next day
- FR5: The system shall rank hotspots from highest to lowest haze risk to Sarawak, using each hotspot's class, fire strength, distance and wind direction.

### Non-Functional Requirements

- NFR1: The system shall complete each update within 5 minutes of new satellite data arriving.
- NFR2: The system shall classify hotspots with an F1-score of at least 0.80 when tested on data not used for training, using the August–September 2026 haze episode.

## Options

- Option A: Static website (HTML and JavaScript) on GitHub Pages. It is free and simple, but it cannot run the Python machine learning models or fetch new hotspot data by itself. It could only show results that were prepared beforehand.
- Option B: Python web app (Flask) with a database on a cloud host. It can run the models and store hotspot and API records, but it needs more setup, and free cloud hosting is limited.
- Option C: Python dashboard built with Streamlit and Folium, with the data and model code kept in GitHub. A scheduler (APScheduler) fetches new NASA FIRMS hotspot data and DOE API readings, runs the classification and prediction models, and updates the risk map. It is deployed on Streamlit Community Cloud, with GitHub Codespaces used for development.

## Decision matrix

Weight: how important the criterion is for YOUR project (1 = low, 5 = high).
Score: how well each option does (1 = poor, 5 = excellent).
Weighted score = weight x score. Add them up for each option.

| Criterion                        | Weight | A score | B score | C score |
| -------------------------------- | ------ | ------- | ------- | ------- |
| Fits my requirements             | 5      | 1 (5)   | 4 (20)  | 5 (25)  |
| Skills I already have            | 4      | 2 (8)   | 3 (12)  | 5 (20)  |
| Time to build before my deadline | 4      | 4 (16)  | 2 (8)   | 4 (16)  |
| Free hosting and tools           | 3      | 5 (15)  | 2 (6)   | 4 (12)  |
| Performance and security needs   | 3      | 2 (6)   | 4 (12)  | 3 (9)   |
| Room to grow later               | 2      | 2 (4)   | 5 (10)  | 3 (6)   |
| **Total (weighted)**             |        | **54**  | **68**  | **88**  |

(Maximum possible total: 115.)

## Decision record

- **Context:** The project classifies fire hotspots in Sarawak, predicts whether the next-day API will pass 100, and ranks hotspots by haze risk on a map. It needs Python machine learning models and regularly updated data from NASA FIRMS and the DOE. Limits: one student, a fixed semester deadline, and no budget for paid hosting.
- **Decision:** Option C, a Streamlit and Folium dashboard in Python, with APScheduler for scheduled data updates, code kept in GitHub, and deployment on Streamlit Community Cloud.
- **Reasons:**
  1. It scored highest (88 out of 115) and matches the requirements best, because the models and the map are all written in Python.
  2. I already use Python, pandas, scikit-learn and XGBoost, so I do not need to learn a new language or framework.
  3. It is free to host and quick to build, which suits the deadline better than Option B.
- **Consequences:** Building the map, risk table and model output in one place becomes easy. A custom design, user logins and heavy traffic become harder, because Streamlit is less flexible than a full web framework such as Flask.
- **Risks and next review:** The free hosting can sleep when idle or run out of memory, and the data sources can be slow or change format. If the dashboard cannot meet the 5-minute processing target, or the free hosting is not enough, I will review the decision at the end of the next sprint and consider moving to Option B.
