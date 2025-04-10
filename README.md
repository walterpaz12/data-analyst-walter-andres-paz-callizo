# Data Analyst and Data Science Portfolio by Walter Andrés Paz Callizo

## Project I: City of Vancouver's Analysis for AWS Data Management

### Project Overview
This group project at UCW analyzed City of Vancouver's open data for developing an AWS data management model. My focus was on the Business License dataset, covering data acquisition, storage in S3, ETL pipeline design with Glue, and initial analysis using Athena and visualizations.

### Skills Demonstrated
AWS (S3, Glue, Athena), Data Engineering (ETL, Data Cleaning), SQL, Data Visualization, Data Analysis, Project Management.

### Key Contributions
Data question formulation, data discovery, S3 storage design, initial data cleaning, ETL pipeline contribution, SQL analysis, basic visualization, cost estimation.

### Key Findings
Analysis of business license trends (1997-2024) and initial rate calculations.

## Project II: UCW Human Resources Office - Health and Organizational Safety (HOS) Data Management

### Project Overview
A group project designing an AWS infrastructure for UCW's HR and HOS data management, focusing on S3, Glue, Athena, and security considerations.

### Skills Demonstrated
AWS (S3, Glue, Athena, CloudTrail, CloudWatch, IAM, KMS), System Design (Draw.IO), Data Engineering (ETL Planning), Data Analysis (Preparation), Security & Monitoring Concepts.

### Key Contributions
AWS infrastructure planning, S3 bucket design, ETL exploration, Athena querying, security/monitoring awareness, system diagramming.

## Project III: Surviving the Titanic: An Exploratory Data Analysis

### Project Overview
Individual EDA project on the Titanic dataset to identify factors influencing survival rates (gender, class, age).

### Skills Demonstrated
Python (Pandas, NumPy, Matplotlib, Seaborn), Data Analysis (EDA), Descriptive Statistics, Data Visualization, Survival Analysis, Insight Generation.

### Key Contributions
Data acquisition, cleaning, exploratory analysis, visualization of survival patterns, interpretation of results.

### Key Findings
Higher survival rates for women and first-class passengers; children and young adults prioritized.

## Project IV: USA's Finances - Gold Price Prediction (Practice Sample)

### Project Overview
A practice project exploring trends in USA's finances by analyzing gold prices over time.

### Skills Demonstrated
Data Analysis (Time Series - Implied), Data Visualization, Financial Data Understanding.

### Key Contributions
Data acquisition, initial exploration, trend identification in gold prices.

## Project V: Loan Dataset Analysis and Visualization for Future Changes

### Project Overview
Individual project analyzing a loan dataset for insights into loan amounts and approvals, with initial modeling attempts.

### Skills Demonstrated
Python (Pandas, NumPy, Matplotlib, Seaborn, scikit-learn, TensorFlow, SciPy, statsmodels), Data Analysis, Data Visualization, Basic Machine Learning (Regression, Classification - Initial Exploration).

### Key Contributions
Data loading/exploration, feature/target definition, initial visualization, attempted model building (Linear Regression, Decision Trees), consideration of RandomForestRegressor.

## [Link to your GitHub Repository](https://walterpaz12.github.io/data-analyst-walter-andres-paz-callizo/)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

name: Auto Embed Issue Images

on:
  schedule:
    - cron: '0 * * * *' # Runs every hour
  workflow_dispatch:     # Allows manual run

jobs:
  update-readme:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repo
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      - name: Install Python dependencies
        run: pip install PyGithub markdown

      - name: Extract Images and Update README
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          REPO_NAME: ${{ github.repository }}
        run: |
          python <<EOF
          from github import Github
          import os
          import re

          g = Github(os.environ['GITHUB_TOKEN'])
          repo = g.get_repo(os.environ['REPO_NAME'])
          issues = repo.get_issues(state='all')
          
          image_md = "## 🖼️ USA Financial System Graphics\n\n"
          for issue in issues:
              matches = re.findall(r'!\[.*?\]\((.*?)\)', issue.body or "")
              for img_url in matches:
                  image_md += f"![Image]({img_url})\n\n"

          # Replace the section between two markers in README
          readme_path = "README.md"
          with open(readme_path, "r", encoding="utf-8") as f:
              content = f.read()

          new_section = f"<!-- AUTO-IMAGES-START -->\n{image_md}<!-- AUTO-IMAGES-END -->"
          content = re.sub(
              r'<!-- AUTO-IMAGES-START -->(.|\n)*?<!-- AUTO-IMAGES-END -->',
              new_section,
              content
          )

          with open(readme_path, "w", encoding="utf-8") as f:
              f.write(content)
          EOF

      - name: Commit and Push if Changes
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add README.md
          git diff --quiet && echo "No changes" || git commit -m "🖼️ Auto-update images from Issues"
          git push
