# Student Result Prediction ML CI

A browser-based MLOps practical repository demonstrating Python Continuous Integration, machine-learning training and testing, an ML quality gate, and preservation of validated model artifacts with GitHub Actions.

## Practical 1 — First Python CI

Files:
- `practical-1/result_logic.py` — PASS/FAIL decision logic.
- `practical-1/test_result_logic.py` — three automated unit tests.
- `.github/workflows/first-python-ci.yml` — runs the tests on GitHub-hosted Ubuntu with Python 3.11.

The workflow supports pushes to `main`, pull requests targeting `main`, and manual execution using `workflow_dispatch`. It is scoped to Practical 1 files so unrelated ML changes do not trigger this workflow.

To inspect it: open **Actions → First Python CI**.

## Practical 2 — Student Result Prediction ML CI

- `train_model.py` creates a reproducible synthetic dataset of 300 records, trains a Logistic Regression pipeline, evaluates it, and writes a model, dataset, and metrics.
- `test_ml_pipeline.py` contains seven automated pipeline and prediction tests.
- `requirements.txt` lists the Python dependencies.
- `.github/workflows/ml-ci.yml` installs dependencies, trains the model, validates it, runs tests, and uploads generated outputs.

## Practical 3 — ML Quality Gate

`quality_gate.py` reads `metrics.json` and requires accuracy of at least **0.85**. A failed quality gate exits with a non-zero status and stops subsequent steps.

## Practical 4 — Preserve ML Artifacts

After the quality gate and tests pass, the workflow uploads:
- `student_result_model.pkl`
- `metrics.json`
- `student_results.csv`

The workflow first checks that each expected output exists, then uploads the artifact named `student-result-ml-artifacts` with a seven-day retention period. This explicit pre-upload validation is important: `if-no-files-found: error` in the upload action does not necessarily fail when just one path from a multi-file list is missing, as long as other files are found. Open the successful workflow run in **Actions** and use its Artifacts section to download it.

## Run the practicals

All execution happens on GitHub-hosted runners; no local Python, Git, Ubuntu, or WSL installation is required for the browser-based demonstration.

1. Open the **Actions** tab.
2. Choose **First Python CI** for Practical 1, or **Student Result ML CI** for Practicals 2–4.
3. Open a run and inspect each job step and its logs.
4. Use **Run workflow** to execute either workflow manually.
5. Download the ML artifact from a successful Student Result ML CI run.

## Repository layout

```text
.github/workflows/
  first-python-ci.yml
  ml-ci.yml
practical-1/
  result_logic.py
  test_result_logic.py
requirements.txt
train_model.py
test_ml_pipeline.py
quality_gate.py
README.md
```

**Note:** The ML data and model are generated in the temporary workflow runner. They are retained separately as an Actions artifact, not committed to the source repository.
