## Data Dictionary

Column-level documentation for the machine-readable files in the `data/` folder.
All participant labels (`P01`–`P22`) correspond to the anonymous identifiers defined in
[`SUPPLEMENTARY.md`](SUPPLEMENTARY.md) (Participant Mapping table).

---

### `Hi-Audio_User_Evaluation_Survey.csv`

Anonymized full survey export (61 columns, 22 rows). Each row is one participant's
post-task questionnaire response. Participant email addresses have been replaced with
JotForm Submission IDs; the screenshot column has been removed.

The file includes all raw SUS and NASA-TLX item responses alongside demographic,
device, and open-ended feedback columns. The `Section_4_SUS.csv` and
`Section_5_NASA-TLX.csv` files extract and reorder the scale-specific columns with
cleaner headers and consistent `P01`–`P22` labels for easier reuse.

---

### `Section_4_SUS.csv`

Raw item responses for the 10-item System Usability Scale (SUS). One row per participant.

| Column | Type | Description |
| ------ | ---- | ----------- |
| `Participant` | string | Anonymous label P01–P22 |
| `Q1` | integer (1–5) | I think that I would like to use this system frequently |
| `Q2` | integer (1–5) | I found the system unnecessarily complex |
| `Q3` | integer (1–5) | I thought the system was easy to use |
| `Q4` | integer (1–5) | I think I would need the support of a technical person to use this system |
| `Q5` | integer (1–5) | I found the various functions in this system were well integrated |
| `Q6` | integer (1–5) | I thought there was too much inconsistency in this system |
| `Q7` | integer (1–5) | I would imagine that most people would learn to use this system very quickly |
| `Q8` | integer (1–5) | I found the system very cumbersome to use |
| `Q9` | integer (1–5) | I felt very confident using the system |
| `Q10` | integer (1–5) | I needed to learn a lot of things before I could get going with this system |

**Scale:** 1 = Strongly Disagree, 5 = Strongly Agree.

**Scoring:** SUS = `((Q1−1)+(5−Q2)+(Q3−1)+(5−Q4)+(Q5−1)+(5−Q6)+(Q7−1)+(5−Q8)+(Q9−1)+(5−Q10)) × 2.5`.
Range 0–100. SD reported as population SD (÷ n=22).

---

### `Section_5_NASA-TLX.csv`

Raw dimension scores for the unweighted NASA Task Load Index (NASA-TLX). One row per participant.

| Column | Type | Description |
| ------ | ---- | ----------- |
| `Participant` | string | Anonymous label P01–P22 |
| `Mental_Demand` | integer (0–100) | How much mental and perceptual activity was required? |
| `Physical_Demand` | integer (0–100) | How much physical activity was required? |
| `Temporal_Demand` | integer (0–100) | How much time pressure did you feel? |
| `Own_Performance` | integer (0–100) | How successful were you in accomplishing the tasks? (0 = perfect, 100 = failure — **raw survey value**) |
| `Effort` | integer (0–100) | How hard did you have to work to accomplish your level of performance? |
| `Frustration` | integer (0–100) | How insecure, discouraged, irritated, stressed, or annoyed were you? |

**Scoring:** Raw Score = `(Mental_Demand + Physical_Demand + Temporal_Demand + (100 − Own_Performance) + Effort + Frustration) / 6`.
`Own_Performance` is **inverted** (100 − value) before averaging so that higher scores uniformly indicate higher workload.
SD reported as sample SD of the 6 dimension means (with Performance inverted).

---

### `Task_Performance.csv`

Binary task completion outcomes. One row per participant, one column per task.

| Column | Type | Description |
| ------ | ---- | ----------- |
| `Participant` | string | Anonymous label P01–P22 |
| `T1` | Y / N | Record singing on an existing collaboration |
| `T2` | Y / N | Manual annotation of track language |
| `T3` | Y / N | Change title, composition country/language |
| `T4` | Y / N | Clone the correct Happy Birthday template |
| `T5` | Y / N | Screenshot the latency test result |
| `T6` | Y / N | Record on the Happy Birthday copy |
| `T7` | Y / N | Create a collection |
| `T8` | Y / N | Create a new composition inside the collection |
| `T9` | Y / N | Use the metronome or guide track |
| `T10` | Y / N | Invite a collaborator |

**Values:** `Y` = successfully completed, `N` = not completed.
Task success was determined by the evaluator via post-hoc review of platform recordings,
cross-referenced with participant self-report.
Full task instructions are in [`docs/Hi-Audio_Evaluation Tasks.pdf`](docs/Hi-Audio_Evaluation%20Tasks.pdf).
