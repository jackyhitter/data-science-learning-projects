# AWS Elastic Beanstalk Regression Model Deployment

This repository contains a machine learning regression model built with Python and configured for automated continuous deployment (CI/CD) to AWS Elastic Beanstalk using AWS CodePipeline.

## 🚀 Project Overview
This project demonstrates how to package and deploy a Python-based machine learning model to the cloud. It is specifically optimized to run on the AWS Elastic Beanstalk Free Tier, handling common deployment bottlenecks such as memory limitations during dependency installation and strict WSGI naming conventions.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Web Framework:** Flask (WSGI standard)
* **Machine Learning:** Scikit-Learn, Pandas, NumPy (or your specific ML libraries)
* **Cloud Infrastructure:** AWS Elastic Beanstalk (EC2, Nginx)
* **CI/CD:** AWS CodePipeline

## 📂 Repository Structure

```text
regression_project_deploy/
│
├── .ebextensions/
│   └── 01_fast_install.config    # Allocates swap memory to prevent Out of Memory (OOM) errors during deployment
├── application.py                # Main entry point for the AWS WSGI server
├── requirements.txt              # Python dependencies
├── model.pkl                     # Serialized machine learning model (example)
└── README.md                     # Project documentation