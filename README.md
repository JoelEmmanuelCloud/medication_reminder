# Healthcare Chatbot with Medication Reminder System (Django Version)

## Overview

This project encompasses the development of a sophisticated healthcare chatbot integrated with a Medication Reminder System. The aim is to revolutionize patient care and support within the healthcare industry by leveraging Artificial Intelligence (AI) and user-friendly interfaces. The chatbot provides immediate, reliable medical information, while the Medication Reminder System assists users in managing their medication schedules effectively.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [System Architecture](#system-architecture)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Healthcare Chatbot:**
  - AI-powered conversational agent for providing medical information and assistance.
  - Natural Language Processing (NLP) for effective communication.
  - Integration with healthcare databases for reliable medical information.
  - Adherence to patient privacy regulations, such as HIPAA.

- **Medication Reminder System:**
  - User authentication and registration for secure access.
  - View medication list with details like drug names and dosages.
  - Add medication reminders based on year, day, and time.
  - Track medication completion status (pending or complete).
  - Chat with Chat_Bot for interactive health recommendations.
  - Add new drug medications with details like drug name and dosage.

## Technologies Used

- **Frontend Development:**
  - HTML, CSS, JavaScript

- **Backend Development:**
  - Python
  - Django Framework

- **Database Management:**
  - PostgreSQL (or your preferred database)

- **User Authentication:**
  - Django Authentication System

## System Architecture

The system follows a modular architecture, including User Interface (UI), Natural Language Processing (NLP), Intent Recognition, Backend Integration, Database, and Security modules. The integration of Medication Reminder System adds functionalities such as medication tracking and reminders.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/JoelEmmanuelCloud/medication_reminder.git

2. Navigate to the project directory:  

    ```bash
    cd reminder
    ``````

3. Install dependencies:

    ```bash 
    pip install -r requirements.txt
    ``````

4. Apply migrations:
    ```bash
    python manage.py migrate
    ``````
5. Run the Django development server:
    ```bash
    python manage.py runserver
    ```
6. Access the application in your web browser:
    ```
    http://localhost:8000
    ```

### Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to enhance the project.

### License
This project is licensed under the MIT License.