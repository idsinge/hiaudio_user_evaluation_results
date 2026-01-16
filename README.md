## 📑 Repository Index

* [Overview](#overview)
* [Purpose of the Study](#purpose-of-the-study)
* [Evaluation Design](#evaluation-design)

  * [Participants](#participants)
  * [Study Structure](#study-structure)
* [Task-Based Performance Results](#task-based-performance-results)

  * [Key Observations](#key-observations)
  * [Task Completion Summary](#task-completion-summary)
* [Questionnaire-Based Results](#questionnaire-based-results)

  * [Participant Profile and Context](#participant-profile-and-context)
  * [Task Duration and Support](#task-duration-and-support)
* [Usability and Workload Metrics](#usability-and-workload-metrics)

  * [System Usability Scale (SUS)](#system-usability-scale-sus)
  * [NASA Task Load Index (NASA-tlx)](#nasa-task-load-index-nasa-tlx)
* [Discussion and Limitations](#discussion-and-limitations)

  * [Identified Challenges](#identified-challenges)
  * [Limitations](#limitations)

---

## Overview

This repository contains the results of a **preliminary user evaluation** conducted for the **Hi-Audio online platform**, with a focus on its practical usability and applicability from the perspective of amateur musicians.

The study is directly linked to the following **preprint publication**:
[https://hal.science/hal-05153739](https://hal.science/hal-05153739)

Additional contextual information about the evaluation call and recruitment process is available here:
[https://hi-audio.imt.fr/agenda/user-evaluation-test/](https://hi-audio.imt.fr/agenda/user-evaluation-test/)

The **post-task questionnaire** administered to participants (including usability and workload assessments) can be accessed at:
[https://form.jotform.com/253353324134348](https://form.jotform.com/253353324134348)

The evaluation was conducted in collaboration with **La Scène**, the student music association of Télécom Paris:
[https://lascene.rezel.net/](https://lascene.rezel.net/)


---

## Purpose of the Study

This evaluation complements the technical validation of the Hi-Audio platform by examining **real user interaction under realistic usage conditions**. Rather than focusing solely on system performance, it aims to provide empirical insight into how musicians engage with the platform’s core features, including:

* collaborative audio recording
* metadata annotation
* collection and composition management
* browser-based round-trip latency estimation

The primary objective is to assess usability, discoverability, and cognitive workload, thereby supporting the research and design goals presented in the associated publication.

---

## Evaluation Design

### Participants

* **Total participants:** 22
* **Evaluation mode:**

  * 20 participants completed the evaluation remotely
  * 2 participants completed it in person at the development team’s facilities

### Study Structure

The evaluation consisted of **two exercises**, comprising **ten task-based activities** in total.
The original PDF with the instructions can be found at ![exercises](docs/Hi-Audio_Evaluation Tasks.pdf). These tasks were designed to cover the platform’s main functionalities, including:

* collaborative audio recording
* use of recording templates
* collection and composition management
* metadata annotation
* collaboration and access control
* browser-based round-trip latency estimation

Tasks were described in a **concise, minimally guided document**, specifying *what* needed to be achieved but not *how*.
This approach was intentionally chosen to:

* rely on users’ intuition
* expose discoverability and usability issues
* avoid bias introduced by detailed documentation

After completing the tasks, participants answered a post-test questionnaire including:

* background and context questions
* the **System Usability Scale (SUS)**
* the **NASA Task Load Index (NASA-TLX)**

Detailed scoring procedures and statistical analyses are provided in the supplementary materials of the project.

---

## Task-Based Performance Results

Across all participants, **72% of the assigned tasks were completed successfully**, indicating that most users were able to achieve the core objectives using the platform.

### Key Observations

* **Recording and performance tasks** showed consistently high success rates
* **Latency estimation** was successfully completed by nearly all participants
* **Metadata annotation and collaboration management** tasks were more error-prone

This suggests that the platform’s primary recording workflow is robust, while secondary features may require clearer affordances or onboarding.

### Task Completion Summary

| Exercise | Task | Description                                              | Completed (%) | Completed (n) |
| -------- | ---- | -------------------------------------------------------- | ------------- | ------------- |
| Ex. 1    | T1   | Record in an existing collaborative composition          | 68.2          | 15 / 22       |
| Ex. 1    | T2   | Manually annotate track metadata (language)              | 31.8          | 7 / 22        |
| Ex. 1    | T3   | Update composition title with country/language reference | 59.1          | 13 / 22       |
| Ex. 1    | T4   | Select and clone a recording template                    | 77.3          | 17 / 22       |
| Ex. 1    | T5   | Estimate browser round-trip latency                      | 95.5          | 21 / 22       |
| Ex. 1    | T6   | Record a performance on top of existing tracks           | 90.9          | 20 / 22       |
| Ex. 2    | T7   | Create a new collection                                  | 72.7          | 16 / 22       |
| Ex. 2    | T8   | Create a composition within a collection                 | 77.3          | 17 / 22       |
| Ex. 2    | T9   | Record using a metronome and/or guide track              | 100.0         | 22 / 22       |
| Ex. 2    | T10  | Invite a collaborator via email                          | 45.5          | 10 / 22       |

---

## Questionnaire-Based Results

Individual participants’ questionnaire responses can be found in the [`surveys/`](surveys/) folder.

### Participant Profile and Context

Participants generally reported:

* strong musical backgrounds (training and regular practice)
* familiarity with collaborative music-making
* varied levels of technical expertise and DAW experience

The evaluation was conducted under **realistic and largely uncontrolled conditions**:

* participants used their own devices, browsers, operating systems, and audio equipment
* a wide range of hardware and software configurations was observed
* some participants used Bluetooth audio devices despite recommendations

This variability increased **ecological validity**, better reflecting real-world usage scenarios.

### Task Duration and Support

* Most participants completed the evaluation in **20–40 minutes**
* 4.5% took more than 60 minutes
* 13.6% completed it in less than 20 minutes
* Approximately 30% required occasional external assistance

All participants reported that this was their **first interaction with the Hi-Audio platform**.

---

## Usability and Workload Metrics

### System Usability Scale (SUS)

The SUS results indicate **marginal overall usability**, with substantial variability across users.

| Metric    | Mean | SD   | Median | Min  | Max  |
| --------- | ---- | ---- | ------ | ---- | ---- |
| SUS Score | 55.8 | 19.8 | 55.0   | 15.0 | 82.5 |

* The average score is below the commonly cited benchmark of 68
* The wide score range suggests that usability issues affect some users more than others

### NASA Task Load Index (NASA-TLX)

Workload scores indicate a **moderate perceived workload**, primarily driven by mental demand and effort rather than physical demand.

| Metric         | Mean | SD   | Min | Max  |
| -------------- | ---- | ---- | --- | ---- |
| NASA-TLX (raw) | 37.3 | 13.8 | 1.7 | 61.0 |

---

## Discussion and Limitations

Overall, the evaluation indicates that the platform successfully supports its **primary objective of collaborative audio recording for dataset creation**.
High success rates for recording and latency-related tasks demonstrate that core functionality can be used effectively by musicians without extensive prior training.

Although participants were not explicitly instructed to configure privacy levels or user roles, these features were implicitly used throughout the exercises.
Post-hoc inspection of the generated data confirmed:

* multiple privacy settings across compositions
* varied collaborator roles (e.g., Member, Admin)

This suggests that access-control mechanisms are **intuitively discoverable**, even without direct instruction.

### Identified Challenges

* Metadata annotation and collaboration management tasks had lower success rates
* Errors were more frequent during early tasks, suggesting a **learning curve effect** rather than fundamental usability flaws

### Limitations

* limited number of participants
* short-term interaction only (no longitudinal usage)
* no comparison with alternative platforms
* participant pool skewed toward technically skilled students

Despite these limitations, combining **objective task performance** with **subjective usability and workload measures** provides a transparent and practical view of how musicians interact with the platform in real conditions.