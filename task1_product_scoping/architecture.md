# System Architecture Thinking

## Data Sources

The platform collects marketing data from multiple external sources:

- Google Ads API
- Meta Ads API
- Google Analytics API

---

## Data Processing Flow

The system follows a simple pipeline to collect, process, and present marketing insights.

### 1. External APIs
Data is pulled from connected marketing platforms.

↓

### 2. Data Extraction Layer
Responsible for fetching raw campaign and analytics data from each source.

↓

### 3. Transformation Layer
Raw data is cleaned and converted into a consistent internal format.

Key responsibilities:

- Standardizing metrics across platforms
- Handling missing or incomplete values
- Normalizing channel-specific data structures

↓

### 4. Analytics Layer
Business logic is applied to generate useful insights.

This layer handles:

- KPI calculations
- Performance evaluation rules
- Recommendation generation

↓

### 5. Dashboard UI
Processed data is displayed through a unified cross-channel dashboard for end users.

---

## Trust & Reliability Considerations

Since marketing decisions depend on data accuracy, the system includes a few transparency features to improve user confidence.

### Reliability Features

- **Last Refreshed Timestamp** → shows when the data was last updated
- **Data Source Labels** → makes it clear which platform each metric comes from
- **Metric Definitions** → helps users understand KPI calculations
- **Recommendation Explanations** → shows why a recommendation was generated

---

## Architecture Goal

The architecture is designed to keep the system **simple, understandable, and scalable**, while providing reliable cross-channel marketing insights.