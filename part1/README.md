# HBnB Evolution Project – Part 1: Technical Documentation

## 📘 Overview

This repository contains the technical documentation for Part 1 of the **HBnB Evolution Project**, a simplified version of an Airbnb-like application. The goal of this phase is to produce a comprehensive design reference that captures the architecture, data model, and system interactions in detail. This documentation provides the foundational blueprint to guide future implementation phases.

---

## 🎯 Objective

To document the architecture and business logic of the HBnB Evolution application, including:

* High-Level Package Diagram
* Detailed Class Diagram for the Business Logic Layer
* Sequence Diagrams for four key API interactions
* Explanatory notes describing design rationale, relationships, and interactions

---

## 🏗️ Application Structure

The application follows a **three-layered architecture**:

1. **Presentation Layer**: APIs and services users interact with.
2. **Business Logic Layer**: Core application models and validation logic.
3. **Persistence Layer**: Manages data access and interaction with the database.

Each component is designed to be modular, scalable, and follows object-oriented principles.

---

## 🧩 Key Features Documented

### ✅ 0. High-Level Package Diagram

* Diagram of the layered architecture
* Highlights communication between layers via the **Facade Pattern**

### ✅ 1. Business Logic Class Diagram

* UML Class diagram for core entities:

  * `User`
  * `Place`
  * `Review`
  * `Amenity`
* Attributes, methods, relationships, and business rules

### ✅ 2. Sequence Diagrams for API Calls

* Four API use cases documented:

  * **User Registration**
  * **Place Creation**
  * **Review Submission**
  * **Fetching a List of Places**
* Diagrams demonstrate the interaction between Presentation, Business Logic, and Persistence layers

### ✅ 3. Documentation Compilation

* All diagrams and notes compiled into a professional PDF document
* Available at: `[LINK TO PDF IN REPO]`

---

## 📁 Repository Structure

```
part1/
├── HBnb_MGarcia.pdf                  # Final compiled technical document
├── diagrams/                        
│   ├── package_diagram.png
│   ├── class_diagram.png
│   └── sequence_*.png
├── README.md                         # This file
```

---

## 📚 Business Rules Summary

* **Users**: Can register, update, delete. Identified by first name, last name, email, password, and admin status.
* **Places**: Owned by users. Have name, description, price, location, and amenities.
* **Reviews**: Tied to places and users. Include rating and comment.
* **Amenities**: Reusable features associated with places.
* All entities must support creation/update timestamps and unique IDs (UUID4).

---

## 🧠 Learning Resources Used

* Canvas for code-based UML diagrams
* [UML Class Diagrams Tutorial](https://www.uml-diagrams.org/class-diagrams-overview.html)
* [Sequence Diagrams Tutorial](https://www.uml-diagrams.org/sequence-diagrams.html)
* [Facade Design Pattern Overview](https://refactoring.guru/design-patterns/facade)
* Holberton Concept Pages on OOP and Layered Architecture

---

## 🔗 Repository Info

* **GitHub Repository**: [https://github.com/YOUR\_USERNAME/holbertonschool-hbnb](https://github.com/YOUR_USERNAME/holbertonschool-hbnb)
* **Project Directory**: `part1/`

---

## ✅ Deliverables Checklist

* [x] High-Level Package Diagram
* [x] Business Logic Class Diagram
* [x] Four API Sequence Diagrams
* [x] Compiled PDF Technical Document

---

## 📩 How to Share

To share the documentation with your reviewer:

1. Upload `HBnb_MGarcia.pdf` to your GitHub repo.
2. Copy the file URL (e.g. `https://github.com/YOUR_USERNAME/holbertonschool-hbnb/blob/main/part1/HBnb_MGarcia.pdf`)
3. Paste it into the required submission field in Intranet.

---

## 🛠️ Author

**Marivellisse Garcia**
Holberton School – Software Engineering Cohort

