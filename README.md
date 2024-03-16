# CCC - Python Programming Final Project
<p>Create Career College - Python Program Final Project by Henry Wat</p>

---

## Tutor: Jason Xu
## Submission Date: 8 Mar 2024

### Technologies:
- Python
- Django
- Software Development Life Cycle (SDLC)

---

# Online Alberta Driving Knowledge Test Platform

## Objective
To develop an online platform for administering the Alberta driving knowledge test. The system will allow users to take the exam, with immediate feedback on their results and progress tracking. The primary goal is to create an accessible, user-friendly interface that accurately simulates the exam environment, helping users to prepare effectively for the actual driving theory test.

## Problem Description
The current availability of preparation resources for the Alberta driving knowledge test is limited and costly, with few options for interactive, self-paced learning and assessment. The project aims to address this gap by providing a platform where users can:
- Take the driving knowledge test anonymously.
- Receive immediate feedback on their performance.
- Retake the exam multiple times for practice.
- Access the platform with learning progress and history.

## Requirements
- A simple, intuitive user interface without extensive styling.
- A database of multiple-choice questions.
- Randomized presentation of questions.
- Calculation and display of results upon exam completion.
- An option to retake the exam for continuous practice.

## Project Schedule
### Week 1: Specification and Learning
Objectives:
- Finalize project specifications.
- Research Django framework and best practices for web application development.
Tasks:
- Explore existing online exam systems for inspiration and best practices.
- Interviews with Class 7 learner license holders about the benefits and difficulties of studying driving test online.
- Define detailed project requirements and functionality.
- Deep dive into Django documentation and tutorials.

### Week 2: Design and Implementation
Objectives:
- Design the database schema and user interface.
- Begin implementation of the core functionalities.
Tasks:
- Day 1-2: Design the database model for questions and choices.
- Day 3-4: Implement the Django project and application setup.
- Day 5: Create Django models and admin interface for question-and-answer management.
- Day 6-7: Develop the views and templates for the index and test pages.

### Week 3: Testing, Refinement, and Deployment
Objectives:
- Complete the implementation.
- Perform thorough testing and debugging.
- Deploy the application.
Tasks:
- Day 1-2: Implement the result calculation and display logic.
- Day 3-4: Conduct persona test, user acceptance testing and bug fixes.
- Day 5: Finalize documentation and prepare for deployment.
- Day 6: Deploy the application to a production environment.
- Day 7: Post-deployment monitoring and readiness for immediate fixes.

## Methods
The project will be developed using the Django web framework, chosen for its robustness, scalability, and extensive documentation. The application will follow the MVC architecture pattern, with a focus on simplicity and functionality. User interaction will be recorded, relying on session management to track progress through the exam with requiring user registration or data persistence beyond the session's scope.

## Result
The expected outcome is a fully functional online platform where users can practice the Alberta driving knowledge test. Users will navigate through multiple series of multiple-choice questions, submit their answers, and receive immediate feedback on their performance, including the correct answers for educational purposes.

### Screenshot
![index](/proj_screenshot/index.png)
![Q1](/proj_screenshot/Q1.png)
![result](/proj_screenshot/result.png)
![admin_question_list](/proj_screenshot/admin_question_list.png)

## Resources
- Mdn web docs: [Django Web Framework (Python)](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)
- [Python Developer’s Guide](https://devguide.python.org/)
- CodeAstro: [Online Examination System in Python Django with Source Code](https://codeastro.com/online-examination-system-in-python-django-with-source-code/)
- Arrow Driving School: [Alberta Basic License Drivers Assessment](https://www.thearrowdrivingschool.com/wp-content/uploads/2018/11/Alberta-Basic-Licence-Drivers-Assessment.pdf)

## What's Next
Post-launch, the project will enter a maintenance phase, with potential future enhancements including:
- Expansion of the question database for greater variety.
- Introduction of user accounts for tracking progress over time.
- Implementation of additional study resources and exam preparation materials.
- Frequently persona and interviewee feedback.
- Accessibility enhancements to ensure the platform is usable by all potential test-takers.

This plan outlines a focused, achievable path to developing the Online Alberta Driving Test platform within a three-week timeframe, addressing a clear need with a structured approach to design, implementation, and deployment.

## Instruction to run this program
1. Create python environment and activate it.
```
python3 -m venv myvenv
source myvenv/bin/activate
```
2. Update pip and install the requirements.
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
3. Migrate database.
```
python manage.py makemigrations
python manage.py migrate
```
4. Create superuse if needed.
```
python3 manage.py createsuperuser
```
5. Execute the program.
```
python manage.py runserver
```
6. Vist the website URL.
```
http://127.0.0.1:8000
```
