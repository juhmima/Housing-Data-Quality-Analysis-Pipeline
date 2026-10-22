#!/bin/bash
set -o pipefail 
csv_file="${1:-housing.csv}"
log_file="housing_pipeline.log"

log_message() {
        echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$log_file"
}
# Identifying each run
log_message "Starting pipeline with input file: $csv_file"

cd /home/newuser/AI

# Input file check
if [[ ! -f "$csv_file" ]]; then
	log_message "ERROR: Input file '$csv_file' not found"
	echo "ERROR: Input file '$csv_file' not found"
	exit 1
fi 
# Missing file check
if [[ ! -s "$csv_file" ]]; then
	log_message "ERROR: Input file '$csv_file' is empty"
	echo "ERROR: Input file '$csv_file' is empty"
	exit 1
fi 

source /home/newuser/AI/.venv/bin/activate 

# Check whether validation fails
if python validate_housing.py "$csv_file" 2>&1 | tee -a "$log_file"; then 
	log_message "Validation passed"
else 
	log_message "Validation failed"
	exit 1
fi
echo "Pipeline continuing to next stage..."
if python analyze_housing.py "$csv_file"; then
	log_message "Analysis passed"
else 
	log_message "Analysis failed"
	exit 1
fi 
echo "Generating price distribution plot..."

# Add price distribution plot
if python plot_price_distribution.py "$csv_file"; then
        log_message "Price distribution plot passed"
else 
	log_message "Price distribution plot failed"
	exit 1
fi 
echo "Generating area vs price plot..."

# Add area vs. price plot
if python plot_price_vs_area.py "$csv_file"; then
        log_message "Area vs price plot passed"
else
        log_message "Area vs price plot failed"
        exit 1
fi
log_message "Pipeline completed successfully for $csv_file"
echo "Pipeline completed successfully for $csv_file"
