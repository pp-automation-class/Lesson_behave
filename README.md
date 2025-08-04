# BDD Test Automation

A Behavior-Driven Development (BDD) test automation framework for web applications, specifically designed for testing the LinkMyGear application. This framework combines the power of Behave for BDD and Playwright for browser automation.

## Features

- Page Object Model design pattern for maintainable test code
- BDD scenarios written in Gherkin syntax
- Cross-browser testing support (Chromium, Firefox, WebKit)
- Configurable headless mode
- Reusable step definitions for common web interactions

## Requirements

- Python 3.13+
- Poetry for dependency management

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd Lesson_behave
   ```

2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

3. Install Playwright browsers:
   ```bash
   poetry run playwright install
   ```
