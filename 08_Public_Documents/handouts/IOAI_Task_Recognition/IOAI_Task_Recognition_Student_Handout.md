# IOAI Machine Learning Task Recognition

**Student Handout | Identify the problem before choosing the model**

> **Core rule:** Do not hunt for keywords. Reconstruct the problem. Start with the required output, then use the historical data description to infer whether a target is available.

## The 5-Step Recognition Routine

| Step | Question to Ask |
|---|---|
| **1. INPUT** | What information is available to the model? |
| **2. OUTPUT** | What exactly must the model produce? |
| **3. LABEL EVIDENCE** | For historical examples, do we know the correct target outcome? |
| **4. TASK TYPE** | What structure does the output have: category, number, groups, ranking, unusual case...? |
| **5. BASELINE** | What is the simplest reasonable model for that task? |

## Task Signatures - Use Structure, Not Keywords

| Output structure | Likely task | Simple baseline |
|---|---|---|
| Category | Classification | Logistic Regression |
| Continuous number | Regression | Linear Regression |
| Groups discovered from similarity | Clustering | K-Means |
| Rare / unusual cases | Anomaly Detection | Isolation Forest |
| Ordered items for a user/query | Recommendation / Ranking | Popularity or simple scoring baseline |
| Future numeric values with time order | Forecasting (usually regression) | Naive / seasonal naive or linear model |

> **Important distinction:** "Supervised / unsupervised" describes how learning is supported by target information. "Classification / regression / clustering / ranking" describes what the model is being asked to do.

## How to Answer

Use one short justification sentence after your task choice:

> "The model must output ______, and the historical records contain / do not contain ______, so this is a ______ problem."

---

# Mixed Practice Set

Complete Steps 1-5 for every scenario. Complete Step 6 only when your teacher assigns it.

## Scenario 1: Missed-Connection Risk

An airline records each passenger's inbound arrival time, scheduled connection time, terminal distance, airport congestion, weather, and boarding-gate closing time. For past itineraries, the database also records whether the passenger actually boarded the connecting flight. The operations team wants a model that can flag current passengers who may need assistance before their next gate closes.

1. **Input:**  
2. **Output:**  
3. **Label evidence:**  
4. **Task type:**  
5. **Baseline:**  
6. **Metric (only if assigned):**  

## Scenario 2: Lunch-Hour Demand

A food-delivery company stores two years of order counts for each neighborhood in 30-minute intervals together with weather, weekday, holidays, promotions, nearby restaurant availability, and recent order volume. At 9:00 a.m., dispatchers want an estimate of how many orders each neighborhood will receive during every 30-minute interval from 11:00 a.m. to 2:00 p.m.

1. **Input:**  
2. **Output:**  
3. **Label evidence:**  
4. **Task type:**  
5. **Baseline:**  
6. **Metric (only if assigned):**  

## Scenario 3: Homepage Article Ordering

A news app has hundreds of candidate articles whenever a reader opens the app. It stores the reader's past reading behavior, article topics, publication time, device context, and records of which articles were shown previously and what the reader did afterward. The app must decide which ten articles should appear first for the current reader.

1. **Input:**  
2. **Output:**  
3. **Label evidence:**  
4. **Task type:**  
5. **Baseline:**  
6. **Metric (only if assigned):**  

## Scenario 4: Store Behavior Profiles

A retail chain has detailed monthly summaries for 2,000 stores: average basket size, return rate, weekday/weekend traffic, product mix, promotion response, and seasonal variation. Regional managers say the existing geographic regions are not useful for operational comparison. They want a small set of data-driven store profiles so that stores with similar operating behavior can be reviewed together.

1. **Input:**  
2. **Output:**  
3. **Label evidence:**  
4. **Task type:**  
5. **Baseline:**  
6. **Metric (only if assigned):**  

## Scenario 5: Unexpected Machine Behavior

A factory collects temperature, vibration, current, pressure, and acoustic measurements from each machine every second. Most production runs are uneventful, while a small number later trigger engineer investigations for unusual behavior. The monitoring team wants an early-warning system that highlights sensor patterns that differ strongly from ordinary operation, including patterns they may not have seen before.

1. **Input:**  
2. **Output:**  
3. **Label evidence:**  
4. **Task type:**  
5. **Baseline:**  
6. **Metric (only if assigned):**  

## Exit Self-Assessment

- [ ] Not yet fluent
- [ ] Mostly fluent
- [ ] Very fluent

**One task type I still confuse with another:** ________________________________________________

**The clue I will check first next time:** ___________________________________________________
