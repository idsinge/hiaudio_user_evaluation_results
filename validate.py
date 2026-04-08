#!/usr/bin/env python3
"""
Validation script for Hi-Audio user evaluation data.

Recomputes headline statistics from the CSV files in data/ and checks them
against the values reported in the README and journal article.

Usage:
    python validate.py

Exits with code 0 if all checks pass, 1 otherwise.
"""
import csv
import statistics
import sys

EXPECTED_PARTICIPANTS = [f'P{i:02d}' for i in range(1, 23)]


def sus_score(items):
    """Standard SUS scoring: odd items (score-1), even items (5-score), sum * 2.5."""
    return ((items[0]-1)+(5-items[1])+(items[2]-1)+(5-items[3])+(items[4]-1)+
            (5-items[5])+(items[6]-1)+(5-items[7])+(items[8]-1)+(5-items[9]))*2.5


def nasa_score(dims):
    """Unweighted NASA-TLX raw score; Own Performance (index 3) is inverted."""
    return (dims[0]+dims[1]+dims[2]+(100-dims[3])+dims[4]+dims[5])/6


def check(label, got, expected, tol=0.05):
    ok = abs(got - expected) <= tol
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {label}: got {got:.2f}, expected {expected:.2f}")
    return ok


def check_bool(label, condition):
    status = "PASS" if condition else "FAIL"
    print(f"  [{status}] {label}")
    return condition


def main():
    passed = True

    # ── Consistency: participant labels across all three CSVs ─────────────────
    print("Participant consistency:")
    files = {
        'Section_4_SUS.csv':       'Participant',
        'Section_5_NASA-TLX.csv':  'Participant',
        'Task_Performance.csv':    'Participant',
    }
    all_ids = {}
    for fname, id_col in files.items():
        with open(f'data/{fname}') as f:
            ids = [r[id_col] for r in csv.DictReader(f)]
        all_ids[fname] = ids
        passed &= check_bool(f"{fname}: 22 rows",   len(ids) == 22)
        passed &= check_bool(f"{fname}: P01–P22 in order", ids == EXPECTED_PARTICIPANTS)

    sus_ids  = all_ids['Section_4_SUS.csv']
    nasa_ids = all_ids['Section_5_NASA-TLX.csv']
    task_ids = all_ids['Task_Performance.csv']
    passed &= check_bool("SUS and NASA-TLX participant lists match",  sus_ids == nasa_ids)
    passed &= check_bool("SUS and Task participant lists match",       sus_ids == task_ids)

    # ── SUS ──────────────────────────────────────────────────────────────────
    with open('data/Section_4_SUS.csv') as f:
        rows = list(csv.DictReader(f))
    sus_scores = [sus_score([int(r[f'Q{i}']) for i in range(1, 11)]) for r in rows]
    n = len(sus_scores)
    pop_sd = (sum((x - statistics.mean(sus_scores))**2 for x in sus_scores) / n) ** 0.5

    print("\nSUS (n=22):")
    passed &= check("mean",            statistics.mean(sus_scores),   55.8)
    passed &= check("SD (population)", pop_sd,                        19.3)
    passed &= check("median",          statistics.median(sus_scores), 55.0)
    passed &= check("min",             min(sus_scores),               15.0)
    passed &= check("max",             max(sus_scores),               82.5)

    # ── NASA-TLX ─────────────────────────────────────────────────────────────
    with open('data/Section_5_NASA-TLX.csv') as f:
        rows = list(csv.DictReader(f))
    cols = ['Mental_Demand', 'Physical_Demand', 'Temporal_Demand',
            'Own_Performance', 'Effort', 'Frustration']
    dim_values  = [[int(r[c]) for r in rows] for c in cols]
    raw_scores  = [nasa_score([int(r[c]) for c in cols]) for r in rows]
    dim_means   = [statistics.mean(dv) for dv in dim_values]
    dim_means_w = dim_means[:]
    dim_means_w[3] = 100 - dim_means[3]   # invert Own Performance
    sd_dim_means = statistics.stdev(dim_means_w)

    print("\nNASA-TLX (n=22):")
    passed &= check("raw mean",               statistics.mean(raw_scores), 37.3, tol=0.1)
    passed &= check("SD of dimension means",  sd_dim_means,               13.5, tol=0.1)
    passed &= check("Mental Demand mean",     dim_means[0],               54.36, tol=0.01)
    passed &= check("Physical Demand mean",   dim_means[1],               14.91, tol=0.01)
    passed &= check("Temporal Demand mean",   dim_means[2],               30.00, tol=0.01)
    passed &= check("Performance mean (inv)", dim_means_w[3],             41.09, tol=0.01)
    passed &= check("Effort mean",            dim_means[4],               38.86, tol=0.01)
    passed &= check("Frustration mean",       dim_means[5],               44.50, tol=0.01)

    # ── Task performance ─────────────────────────────────────────────────────
    with open('data/Task_Performance.csv') as f:
        task_rows = list(csv.DictReader(f))
    task_cols       = [f'T{i}' for i in range(1, 11)]
    total_attempts  = len(task_rows) * len(task_cols)
    total_completed = sum(r[t] == 'Y' for r in task_rows for t in task_cols)
    completion_rate = total_completed / total_attempts * 100
    per_task        = {t: sum(r[t] == 'Y' for r in task_rows) for t in task_cols}

    print("\nTask performance (22 participants × 10 tasks):")
    passed &= check("total attempts",    float(total_attempts),  220.0, tol=0)
    passed &= check("total completed",   float(total_completed), 158.0, tol=0)
    passed &= check("completion rate %", completion_rate,         71.8, tol=0.1)

    expected_per_task = {
        'T1': 15, 'T2': 7,  'T3': 13, 'T4': 17, 'T5': 21,
        'T6': 20, 'T7': 16, 'T8': 17, 'T9': 22, 'T10': 10,
    }
    print("\n  Per-task completion counts:")
    for t, exp in expected_per_task.items():
        passed &= check_bool(f"  {t}: {per_task[t]}/22 (expected {exp})",
                             per_task[t] == exp)

    print(f"\n{'All checks passed.' if passed else 'Some checks FAILED.'}")
    sys.exit(0 if passed else 1)


if __name__ == '__main__':
    main()
