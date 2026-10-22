
# AWS Housing Data Quality & Analysis Pipeline

## 1. Project Overview

In my technical upskilling journey, I became interested in learning Linux and cloud computing, in addition to developing my Python programming skills. I aimed to combine the three by building a repeatable data validation and analysis workflow in a cloud-hosted Linux environment.

Using a publicly available housing dataset, I wrote Python scripts to evaluate data quality, calculate descriptive statistics, and generate visualizations of housing prices and variable relationships. I also built a Bash script to orchestrate the workflow, record timestamped log messages, and stop execution when validation fails.

To evaluate reliability, I tested the pipeline using clean data and created deliberately problematic inputs, including invalid records and empty datasets. These tests helped verify that the pipeline identifies common data issues and handles failures without moving to further stages of analysis.

## 2. Technologies Used

- AWS EC2
- Linux
- Python (pandas, Matplotlib)
- Bash

## 3. Project Structure

- `housing.csv` — Input housing dataset.
- `validate_housing.py` — Checks data quality and reports validation failures.
- `analyze_housing.py` — Calculates descriptive statistics.
- `plot_price_distribution.py` — Generates a housing-price distribution histogram.
- `plot_price_vs_area.py` — Visualizes the relationship between housing area and price.
- `run_housing_pipeline.sh` — Runs the workflow, logs activity, and stops when a stage fails.
- `housing_price_distribution.png` and `housing_price_vs_area.png` — Generated visualizations.
- `housing_pipeline.log` — Records pipeline activity and errors.

## 4. How to Run the Pipeline

### Run the Pipeline

1. Navigate to the project directory in your Linux environment.
2. Run the pipeline using the default dataset:

   ```bash
   bash run_housing_pipeline.sh
   ```

3. To process a different CSV file, provide its filename:

   ```bash
   bash run_housing_pipeline.sh housing_test.csv
   ```

### Outputs

- Data quality validation report
- Descriptive statistics
- Housing price distribution histogram
- Housing area versus price visualization
- Timestamped pipeline log (`housing_pipeline.log`)

## 5. Testing and Error Handling

I tested the pipeline with multiple input scenarios to verify its validation and error-handling behavior.

| Test scenario | Expected behavior | Result |
|---|---|---|
| Valid housing dataset | Complete all pipeline stages | PASS |
| Negative housing price | Detect invalid data and stop | PASS |
| Missing input file | Display and log an error | PASS |
| Empty CSV file | Detect empty file and stop | PASS |
| CSV containing headers but no rows | Fail validation and stop | PASS |
| Missing required column | Report validation failure and stop | PASS |

The Bash pipeline uses exit codes and timestamped logging to help identify failures. When validation fails, the analysis and visualization stages do not run.

## 6. Results and Key Findings

### Data Quality

- Processed a dataset containing 545 rows and 13 columns.
- Found no missing cells or duplicate rows in the original dataset.
- Verified required columns, positive housing prices and areas, and expected categorical values.

### Statistical Analysis

- **Average housing price:** 4,766,729.25
- **Median housing price:** 4,340,000
- **Highest housing price:** 13,300,000
- **Average area:** 5,150.54
- **Area–price correlation:** 0.536

The price distribution is right-skewed, indicating that a smaller number of higher-priced properties extend the distribution toward the upper end. The area–price correlation indicates a moderate positive linear association between area and price in this dataset; this does not establish causation.

### Project Takeaways

Building this project provided me with an invaluable opportunity to connect concepts from Linux, cloud computing, and Python.

- **Learning through troubleshooting:** I encountered and resolved issues involving file paths, Python environments, script errors, and pipeline execution. These experiences helped me become more comfortable investigating problems independently rather than following a textbook example step by step.
- **Moving from individual scripts to automation:** I learned how to combine separate Python scripts into a repeatable Bash workflow, with logging and exit codes to make failures easier to identify.

This project strengthened my understanding of how Linux, Python, and Bash can work together to build a more reliable and maintainable data-processing workflow.
