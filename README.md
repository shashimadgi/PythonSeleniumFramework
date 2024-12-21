cross-Browser Testing and Page Object Model
This repository provides a Cross-Browser Testing Framework implemented using Selenium, Pytest, and the Page Object Model (POM) design pattern. It supports running tests across multiple browsers, generating detailed HTML reports, and debugging with embedded screenshots for failed test cases.

Features
1. Cross-Browser Support
Easily run tests on Chrome, Firefox, and Internet Explorer.
Select the browser using the --browser_name command-line option.
Automated WebDriver installation and management with webdriver-manager.
2. Page Object Model (POM)
Clean and maintainable test scripts with POM design.
Each page has its own Python class, encapsulating locators and actions.
3. Pytest Framework
Simplified test execution with Pytest fixtures.
Centralized browser setup and teardown.
Custom hooks for embedding screenshots in HTML reports.
4. Detailed HTML Reporting
Generate detailed HTML reports for test runs.
Embed screenshots for failed test cases, making debugging easier.
