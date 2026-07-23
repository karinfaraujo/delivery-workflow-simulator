# 🍕 Delivery Workflow Simulator

A Python-based delivery assistant that simulates the workflow orchestration concepts of AWS Step Functions using a rule-based state machine. This project demonstrates how a delivery workflow can be implemented locally without relying on AWS services or external APIs.

---

## 📖 Overview

The **Delivery Workflow Simulator** is an educational project developed to demonstrate workflow orchestration concepts inspired by **AWS Step Functions**.

Instead of using cloud services, the application implements a simple rule-based state machine in Python that identifies user intents and routes requests to the appropriate module.

This approach makes the project lightweight, easy to understand, and ideal for learning software architecture fundamentals.

---

## ✨ Features

- Display the restaurant menu
- Create a new order
- Check an order status
- Cancel an existing order
- Detect user intent using keyword matching
- Simulate a workflow engine inspired by AWS Step Functions
- Fully offline (no cloud services or external APIs)

---

## 🏗️ Project Structure

```text
delivery-workflow-simulator/
│
├── src/
│   ├── app.py
│   ├── constants.py
│   ├── intent.py
│   ├── menu.py
│   ├── orders.py
│   └── workflow_engine.py
│
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

## 🔄 Workflow

```text
                 User
                   │
                   ▼
            process_message()
                   │
                   ▼
           detect_intent()
                   │
         ┌─────────┴─────────┐
         │                   │
         ▼                   ▼
     Workflow Engine     Unknown Intent
         │                   │
         ▼                   ▼
 ┌───────────────┬───────────────┐
 │               │               │
 ▼               ▼               ▼
Menu         Orders         Responses
```

---

## ⚙️ Technologies Used

- Python 3
- Rule-Based State Machine
- Modular Architecture
- Object-Oriented Design Principles
- Git & GitHub

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/karinfaraujo/delivery-workflow-simulator.git
```

### Navigate to the project folder

```bash
cd delivery-workflow-simulator
```

### Run the application

```bash
python src/app.py
```

---

## 💻 Example Usage

```text
==================================================
Delivery Workflow Simulator
==================================================

You: hello

Assistant:
Hello! 👋
Welcome to the Delivery Workflow Simulator.
How can I help you today?

You: show me the menu

Assistant:
🍕 MENU
--------------------
- Margherita Pizza: $35.00
- Pepperoni Pizza: $42.00
- Chicken Pizza: $40.00
- Cheese Pizza: $38.00
- Coca-Cola: $8.00
- Orange Juice: $10.00

You: I want a pepperoni pizza

Assistant:
Order #1 created successfully!
Item: Pepperoni Pizza
Status: Preparing

You: where is my order?

Assistant:
Order #1
Item: Pepperoni Pizza
Status: Preparing

You: cancel my order

Assistant:
Order canceled successfully.

You: bye

Assistant:
Goodbye! Have a great day!
```

---

## 🧠 Architecture

The project follows a modular architecture where each module has a single responsibility.

| Module | Responsibility |
|---------|----------------|
| **app.py** | Application entry point |
| **workflow_engine.py** | Workflow orchestration |
| **intent.py** | User intent detection |
| **menu.py** | Menu management |
| **orders.py** | Order management |
| **constants.py** | Shared constants and messages |

---

## 🎯 Learning Objectives

This project demonstrates:

- Modular software design
- Separation of concerns
- Workflow orchestration concepts
- State machine fundamentals
- Intent detection using rule-based logic
- Clean Python project organization

---

## 🔮 Future Improvements

Possible future enhancements include:

- Persist orders using SQLite
- Add unit tests
- Implement logging
- Replace keyword matching with an LLM
- Integrate AWS Step Functions
- Integrate Amazon Bedrock
- Build a web interface with Flask or FastAPI

---

## ☁️ Inspiration

This project was inspired by the workflow orchestration concepts of **AWS Step Functions**.

The goal was to recreate a simplified version of a delivery assistant locally, focusing on software architecture rather than cloud infrastructure.

No AWS services or external APIs are required to run this project.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

Developed by **Karin Araujo** as part of the **DIO AWS - AI Agents in the Field** learning journey.
