# IOAI Machine Learning Task Recognition

**Teacher Key | Suggested answers and discussion points**

> **Use this key as a reasoning guide:** Accept equivalent wording when the student correctly identifies the model input, target/output, source of supervision, task structure, and a defensible simple baseline.

## Scenario 1: Missed-Connection Risk

- **Input:** Passenger/itinerary features: inbound arrival time, connection time, terminal distance, airport congestion, weather, gate closing time, etc.
- **Output:** Probability or decision: will this passenger miss the connection / need assistance?
- **Label evidence:** Yes. Historical itineraries contain the actual boarding outcome for the connecting flight.
- **Task:** Binary classification.
- **Baseline:** Logistic Regression.
- **Metric:** F1 or PR-AUC if missed connections are relatively rare. Also inspect precision/recall depending on the operational cost of false alarms versus missed cases.
- **Reasoning:** The required output is a discrete yes/no outcome and historical outcomes are available.

## Scenario 2: Lunch-Hour Demand

- **Input:** Past neighborhood order counts plus time, weather, holidays, promotions, restaurant availability, and recent demand.
- **Output:** Expected number of orders for each future 30-minute interval.
- **Label evidence:** Yes. Historical order counts provide the target values for earlier time periods.
- **Task:** Regression; more specifically, time-series forecasting because time order matters.
- **Baseline:** Seasonal-naive forecast or a simple Linear Regression using calendar/weather features.
- **Metric:** MAE is easy to interpret; RMSE if large misses should be penalized more strongly.
- **Reasoning:** The output is a numeric quantity and it is predicted for future time intervals.

## Scenario 3: Homepage Article Ordering

- **Input:** Reader history, candidate-article features, context, and historical impression/engagement records.
- **Output:** An ordered list of candidate articles; top 10 shown first.
- **Label evidence:** Historical behavior provides preference signals such as clicks, reads, dwell time, or downstream engagement. These are implicit feedback signals rather than a single clean class label.
- **Task:** Recommendation / ranking.
- **Baseline:** Popularity ranking, recency ranking, or a simple weighted score before more advanced personalized models.
- **Metric:** Precision@K, Recall@K, NDCG@K, or MAP depending on course level.
- **Reasoning:** The model's primary output is an ordering of items for a user, not a single category.

## Scenario 4: Store Behavior Profiles

- **Input:** Monthly operational feature vectors for stores.
- **Output:** A small number of groups/profiles containing stores with similar behavior.
- **Label evidence:** No predefined target profile is described; existing geographic regions are explicitly not the desired grouping.
- **Task:** Clustering.
- **Baseline:** K-Means after appropriate scaling.
- **Metric:** Silhouette score plus qualitative/business interpretability. Inertia can help compare K within the same representation but should not be treated as a universal quality score.
- **Reasoning:** The goal is to discover groups from similarity rather than predict an existing target.

## Scenario 5: Unexpected Machine Behavior

- **Input:** Multivariate machine sensor measurements over time.
- **Output:** A score or flag indicating unusually different operating patterns.
- **Label evidence:** Only partial/weak supervision is implied: some runs led to investigations, but the goal includes previously unseen patterns. Treat the core task as anomaly detection rather than ordinary supervised classification.
- **Task:** Anomaly detection.
- **Baseline:** Isolation Forest (after sensible aggregation/scaling where needed).
- **Metric:** If reviewed incidents exist, use precision/recall on flagged events; otherwise combine expert review, false-alert rate, and detection rate on known incidents. Evaluation is harder without complete ground truth.
- **Reasoning:** The goal is to find rare deviations from ordinary operation, including novel patterns.

## Common Misdiagnoses to Listen For

- **"Predict" = regression.** Wrong: inspect the output structure.
- **"No obvious class names" = unsupervised.** Wrong: historical outcomes may still provide supervision.
- **"Unusual" = always anomaly detection.** Wrong: with complete labeled outcomes, it may be classification.
- **Recommendation = classification.** Usually the core output is ranking.
- **Choosing XGBoost / a neural network before identifying the task.** Model choice comes after problem structure.
