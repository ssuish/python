## ---

**1\. Finalized Project Requirements Document (PRD)**

### **Core Objective**

To provide a low-friction attendance solution for K-12 teachers that uses temporary session codes to prevent "buddy-punching" and offers real-time monitoring of student arrivals.

### **Functional Requirements**

- **Dynamic Session Tokens:** \* Educators generate a 6-character code (e.g., XY82K1) that expires after a set grace period (e.g., 15 mins).
  - System rejects check-ins after expiry or if the student isn't in the class roster.
- **Real-Time Educator Dashboard:**
  - **Live Grid:** Displays all ACTIVE students.
  - **Short Polling:** Dashboard auto-refreshes every 5–10 seconds.
  - **Manual Overrides:** One-click status changes (Present, Late, Absent, Excused, Sick).
  - **Bulk Actions:** "Mark All Remaining as Absent" button.
- **Student Self-Service:**
  - No-login check-in using the Session Code and Student ID.
  - Submit **Correction Requests** (e.g., "Phone was dead") for teacher approval.
- **Administrative Management:**
  - **Soft Delete:** Mark students as DROPPED to hide them from live views while keeping historical data.
  - **Historical Filters:** Review and edit attendance by Date, Class, and Subject.
  - **CSV Export:** Export filtered data for gradebook integration.

## ---

**2\. System Architecture**

Since you are an advanced beginner using **TypeScript (Next.js)** and **Python (FastAPI)**, we will use a **Client-Server Architecture** with a relational database.

- **Frontend (Next.js/TS):** Handles the Educator Dashboard (Admin) and Student Portal (Guest). Uses **SWR** for the polling logic.
- **Backend (FastAPI/Python):** Manages the "Time Engine" logic, session token generation, and database queries.
- **Database (PostgreSQL):** Stores relational data. Using a relational DB is non-negotiable here because of the complex links between Students, Classes, and Schedules.

## ---

**3\. API Specification**

The API will follow RESTful principles. All timestamps are sent/received in **ISO 8601 UTC**.

### **A. Session Management**

| Method | Endpoint                    | Description                                                            |
| :----- | :-------------------------- | :--------------------------------------------------------------------- |
| POST   | /sessions/start             | Creates a new 6-char code for a subject; returns token and expires_at. |
| GET    | /sessions/active/{class_id} | Returns the current active token for a class (if any).                 |

### **B. Attendance & Live Dashboard**

| Method | Endpoint                      | Description                                                                                   |
| :----- | :---------------------------- | :-------------------------------------------------------------------------------------------- |
| POST   | /attendance/checkin           | Student submits student_id and session_code. Returns success/failure.                         |
| GET    | /attendance/live/{session_id} | **(Polled)** Returns a list of all active students and their current status for that session. |
| PATCH  | /attendance/log/{log_id}      | Educator manually updates a student's status or notes.                                        |

### **C. Student Management**

| Method | Endpoint                      | Description                         |
| :----- | :---------------------------- | :---------------------------------- |
| POST   | /students/import              | Bulk upload students via JSON/CSV.  |
| PATCH  | /students/{student_id}/status | Update status to ACTIVE or DROPPED. |

### **D. Correction Requests**

| Method | Endpoint                       | Description                                                                      |
| :----- | :----------------------------- | :------------------------------------------------------------------------------- |
| POST   | /requests/submit               | Student submits a correction request.                                            |
| POST   | /requests/{request_id}/approve | Educator approves; system automatically updates the corresponding AttendanceLog. |

## ---

**4\. Data Model (Database Schema)**

- **Students:** id, external_id (School ID), name, class_id, status (Active/Dropped).
- **Subjects:** id, name, start_time, end_time, grace_period_mins.
- **AttendanceLogs:** id, student_id, subject_id, timestamp, status (Present/Late/Absent/Excused/Sick), is_manual (Boolean).
- **SessionTokens:** id, subject_id, code, expires_at.
