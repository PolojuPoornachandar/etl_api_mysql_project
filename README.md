# ETL API MySQL Project

## Overview

This project implements a simple **ETL (Extract, Transform, Load)** pipeline in Python that:

- Extracts data from a fake API server
- Transforms the data by cleaning and formatting it
- Loads the cleaned data into a MySQL database

The goal is to demonstrate a full ETL workflow with modular Python code and integration with MySQL.

---

## Features

- Modular codebase with separate extraction, transformation, and loading steps
- Local fake API server to simulate data source
- Uses pandas for data transformation and cleaning
- Loads data efficiently into MySQL using `mysql-connector-python`
- Environment variables managed via `.env` file for secure configuration
- Basic testing using pytest for API endpoints

---

## Prerequisites

- Python 3.7 or higher
- MySQL Server installed and running
- `pip` package manager
