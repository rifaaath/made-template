# Educational Access and Economic Mobility in the Americas

This project investigates the relationship between educational access, as measured by primary school enrollment rates, and economic mobility, as indicated by GDP per capita, across various countries in the Americas. The analysis utilizes data from the World Bank Open Data from 1970 to 2023.

## Project Description

The core objective is to determine if there is a correlation between a country's average primary school enrollment rate and its average GDP per capita over the specified time period. The project employs an automated ETL (Extract, Transform, Load) pipeline, data visualization, and statistical analysis to explore this relationship.

## Data Sources

The analysis is based on two datasets from the World Bank Open Data:

1.  **Primary School Enrollment (% gross)**: Data on gross primary school enrollment rates for countries in the Americas from 1970-2023.
2.  **GDP per capita (current US$)**: Data on GDP per capita, measured in current US dollars for countries in the Americas from 1960-2023.

These datasets are licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0) license. Proper attribution to the World Bank is included in the report.

## Project Structure

The project repository contains the following files and directories:

*   **`data/`**: Contains the raw CSV datasets: `data1.csv` (enrollment) and `data2.csv` (GDP).
*   **`analysis.py`**: Python script for data analysis and visualization.
*  **`eda_script.py`**: Python script that performs exploratory data analysis.
*   **`generate_maps.py`**: Python script to generate the map visualizations.
*   **`report.tex`**: LaTeX source file for the report.
*   **`references.bib`**: BibTeX file containing all the references for the LaTeX document.
*   **`README.md`**: This file (project documentation).
* **`enrollment_map.png`**: Choropleth map showing the mean enrollment per country.
* **`gdp_map.png`**: Choropleth map showing the mean GDP per capita per country.
* **`data1_sample.png`**: Screenshot showing the first few lines of the `data1.csv` file.
* **`data2_sample.png`**: Screenshot showing the first few lines of the `data2.csv` file.
* **`hist_enrollment.png`**: histogram of the mean enrollment rates.
* **`hist_gdp.png`**: histogram of the mean GDP per capita.
* **`scatter.png`**: scatter plot showing the relation between the mean enrollment and the mean GDP.
* **`timeseries_Argentina.png`**: time series of GDP and enrolment for Argentina.
* **`timeseries_United States.png`**: time series of GDP and enrolment for the United States.
* **`timeseries_Brazil.png`**: time series of GDP and enrolment for Brazil.
* **`timeseries_Chile.png`**: time series of GDP and enrolment for Chile.
* **`boxplot_enrollment.png`**: boxplot of the mean enrollment rates.
* **`boxplot_gdp.png`**: boxplot of the mean GDP per capita.

## Setup and Installation

1.  **Clone the repository** to your local machine:
    ```bash
    git clone [repository URL]
    ```
2.  **Install Python dependencies** using pip:
    ```bash
    pip install pandas geopandas matplotlib requests seaborn
    ```

## Data Processing and Analysis

*   The `pipeline.py` script loads the CSV data, calculates mean values for enrollment and GDP, merges the data, performs correlation analysis, and generates maps.
*  The `analysis.py` performs Exploratory Data Analysis to understand the main features of the data, and also generates choropleth maps using geopandas and matplotlib.

## Findings

The analysis shows a very weak negative correlation between primary school enrollment rates and GDP per capita in the Americas over the studied period. The details of the analysis and results are described in the generated PDF report.

## Further Research

Possible avenues for further research include exploring other levels of education, looking at other geographic regions, and including other factors that can affect economic output.

## License
This project is licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0) license.

## Project Work
Your data engineering project will run alongside lectures during the semester. We will ask you to regularly submit project work as milestones, so you can reasonably pace your work. All project work submissions **must** be placed in the `project` folder.

### Exporting a Jupyter Notebook
Jupyter Notebooks can be exported using `nbconvert` (`pip install nbconvert`). For example, to export the example notebook to HTML: `jupyter nbconvert --to html examples/final-report-example.ipynb --embed-images --output final-report.html`


## Exercises
During the semester you will need to complete exercises using [Jayvee](https://github.com/jvalue/jayvee). You **must** place your submission in the `exercises` folder in your repository and name them according to their number from one to five: `exercise<number from 1-5>.jv`.

In regular intervals, exercises will be given as homework to complete during the semester. Details and deadlines will be discussed in the lecture, also see the [course schedule](https://made.uni1.de/).

### Exercise Feedback
We provide automated exercise feedback using a GitHub action (that is defined in `.github/workflows/exercise-feedback.yml`). 

To view your exercise feedback, navigate to Actions → Exercise Feedback in your repository.

The exercise feedback is executed whenever you make a change in files in the `exercise` folder and push your local changes to the repository on GitHub. To see the feedback, open the latest GitHub Action run, open the `exercise-feedback` job and `Exercise Feedback` step. You should see command line output that contains output like this:

```sh
Found exercises/exercise1.jv, executing model...
Found output file airports.sqlite, grading...
Grading Exercise 1
	Overall points 17 of 17
	---
	By category:
		Shape: 4 of 4
		Types: 13 of 13
```
