# Legacy Session Migration Map

Maps **new club sessions (1–72)** to **legacy packets (1–78)** for content reuse during migration.

**Legend:** `→` = primary reuse · `(alt)` = supplementary · `new` = write fresh packet

## Year A (G10) — Sessions 1–24

| New | Title | Legacy reuse |
|---:|---|---|
| 1 | Club charter & portfolio | 1 (rewrite framing) + `08_Public_Documents/posters/` |
| 2 | GitHub & evidence | 2 |
| 3 | Entry diagnostic | new |
| 4 | NumPy refresh | 13–14 |
| 5 | Pandas | 15–16 |
| 6 | Data quality | 17 |
| 7 | Visualisation / EDA | 18 |
| 8 | Task formalisation | 24, 41 |
| 9 | Splits & baselines | 41 (embedded Kaggle baseline) |
| 10 | Logistic regression | 25, 44 |
| 11 | Trees & forests | 30, 48–49 |
| 12 | Ensembles | 49–50 |
| 13 | Mitchell Ch 1 | 33 |
| 14 | Bias & representation | 34–35 |
| 15 | What models learn | 36 |
| 16 | Generative AI & policy | 40 + AI use policy poster |
| 17 | Fairness & stakeholders | 34 (alt) + new case bank |
| 18 | Ethics workshop | new |
| 19–23 | Scholar project | 18 mini-project pattern + templates |
| 24 | Year A review | new |

## Year B (G11) — Sessions 25–48

| New | Title | Legacy reuse |
|---:|---|---|
| 25–27 | Math bridge | 41–43 |
| 28–30 | PyTorch loops | 59–61 |
| 31–33 | CV core | 62–64 |
| 34–37 | Robotics vision | new + 62–64 (alt) |
| 38–39 | NLP or audio | 66–69 (pick one track) |
| 40–48 | Applied project | 71–74 patterns + new robotics brief |

## Year C (G12) — Sessions 49–72

| New | Title | Legacy reuse |
|---:|---|---|
| 49–51 | Transformers / GenAI / RAG | 66–69, Mitchell synthesis |
| 52–54 | Advanced evaluation | 71–74 |
| 55–58 | Responsible deployment | new + Mitchell trust chapters |
| 59–70 | Capstone | 07_Competition_Projects/ templates (adapt) |
| 71–72 | Portfolio & transition | new |

## Demoted / optional legacy blocks

| Legacy block | Sessions | Disposition |
|---|---:|---|
| CS50P Python | 3–12 | Gap-fill only |
| Bohrium ML | 19–32 | Optional Mandarin enrichment; cut from core |
| Full Mitchell seminars | 33–40 | Compressed to 13–18 in Year A |
| Andrew Ng ML depth | 45–58 | Split: core in A2, enrichment in E-module |
| Tuning / competition sim | 75–78 | Competition Enrichment E2–E3 only |

## Authoring priority

1. **Sessions 1–3, 13–18, 34–37, 59–70** — mostly new or heavily rewritten  
2. **Sessions 4–12, 25–33** — adapt legacy with club framing  
3. **Year-band SESSION_LAUNCHER files** — create after packets drafted

## Folder plan (target)

```text
02_Class_Missions/
  Year_A_G10/          # Sessions 1–24 (target)
  Year_B_G11/          # Sessions 25–48 (target)
  Year_C_G12/          # Sessions 49–72 (target)
  00_Orientation_and_Evidence/ … 08_Tuning…/   # legacy bank (current)
```
