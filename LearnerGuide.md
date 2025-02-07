# Learner Guide: Submitting Python Assignments via Fork & Pull Request on GitHub

Welcome to the assignment submission guide for the Python course! Follow these step-by-step instructions to submit your assignments using GitHub's Fork and Pull Request workflow.

---

## Table of Contents
1. [Introduction](#introduction)
2. [Step-by-Step Submission Guide](#step-by-step-submission-guide)
3. [Important Reminders](#important-reminders)
4. [Troubleshooting & FAQs](#troubleshooting--faqs)
5. [Additional Resources](#additional-resources)

---

## Introduction

This guide explains how to:
- Fork the main course repository.
- Clone your fork to your local machine.
- Create a new branch for your assignment.
- Commit and push your changes.
- Create a Pull Request (PR) to submit your assignment.

**Repository URL:**  
[https://github.com/LoordhuJeyakumar/python_course](https://github.com/LoordhuJeyakumar/python_course)

---

## Step-by-Step Submission Guide

### 1. Fork the Repository
- **Navigate to the repository:**  
  Go to [https://github.com/LoordhuJeyakumar/python_course](https://github.com/LoordhuJeyakumar/python_course)
- **Click "Fork":**  
  Click the **Fork** button in the top-right corner to create a copy in your GitHub account.



### 2. Clone Your Forked Repository
- **Access your fork:**  
Visit your forked repository (e.g., `https://github.com/[YourUsername]/python_course`).
- **Clone the repository:**
- Click the green **"Code"** button.
- Select HTTPS and copy the URL.
- Open your Terminal/Command Prompt and run:
  ```bash
  git clone [YOUR_FORK_URL]
  cd python_course
  ```

### 3. Create a New Branch for Your Assignment
- **Create a branch:**  
Use a branch name that identifies the assignment and your GitHub username.
```bash
git checkout -b assignment-[ASSIGNMENT_NUMBER]-[YOUR_GITHUB_USERNAME]
```
Example
```bash
git checkout -b assignment-1-john
```

### 4. Work on Your Assignment and Commit Changes
- **Edit Files:**
Open the project in your favorite code editor (e.g., VS Code, PyCharm) and complete your assignment.

- **Stage and commit:**
```bash
git add .
git commit -m "Submit assignment [ASSIGNMENT_NUMBER] - [Your Name] - [Brief description of work]"
```
**Example:**
```bash
git add .
git commit -m "Submit assignment 1 - john - Completed basic calculator program"
```

### 5. Push Your Branch to Your Fork
- **Push the branch:**
```bash
git push origin assignment-[ASSIGNMENT_NUMBER]-[YOUR_GITHUB_USERNAME]
```
**Example:**
```bash
git push origin assignment-1-john
```
### 6. Create a Pull Request (PR)
- **Navigate to your fork on GitHub.**
- **Initiate a PR:**
    - Click the "Compare & pull request" button.
    -  If not prompted, go to the Pull Requests tab and click "New pull request".
- **Ensure the following:**
    - **Base repository**: LoordhuJeyakumar/python_course
    - **Base branch**: main (or as instructed)
    - **Head repository**: Your fork and your assignment branch.
- **Submit the PR:**

    Provide a clear title and any additional comments, then click "Create pull request".


## Important Reminders
- **Work in Your Fork:**

    Always make changes in your own repository, not the main course repository.
- **Separate Branches:**

    Use a new branch for each assignment submission.
- **Do Not Push to Main Repo:**

    Do not push directly to LoordhuJeyakumar/python_course.
- **Automatic Updates:**

    Any new commits to your branch will update the PR automatically.
- **Ask for Help:**

    If you run into issues, contact your instructor for support.


## Troubleshooting & FAQs
- **I don't see the "Fork" button:**
    Ensure you're logged in to GitHub and have the correct permissions.
- **My PR isn’t updating:**
    Verify your branch name and push any new commits.
- **Merge conflicts occur:**
    Resolve them locally, then commit and push your changes.


## Additional Resources
- [GitHub Documentation](https://docs.github.com)
- [Git Tutorials](https://www.atlassian.com/git/tutorials)

> **Congratulations! Your assignment has been successfully submitted.**
