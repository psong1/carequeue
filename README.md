# CareQueue: Patient Triage Dashboard

CareQueue is a full-stack medical admission dashboard designed to streamline patient intake and triage. This application demonstrates a modern FastAPI + Vue 3 + PostgreSQL architechture with a focus on clean, modular code and healthcare domain efficiency.

## The Stack

- **Frontend**: Vue 3, TypeScript, Vite, Tailwind CSS v4
- **Backend**: FastAPI (Python 3.12+), SQLAlchemy, Pydantic
- **Database**: PostgreSQL
- **Dev Ops**: Concurrently for unified local development

## Key Features

- **Intelligent Traige**: Automates queue sorting based on medical priority (Critical > Moderate > Routine).
- **Real-time Admission**: A reactive check-in form that updates the queue without page refreshes.
- **Medical Resolve Flow**: A one-click "Resolve" action to clear patients from the PostgreSQL database once care is delivered.
- **Modern UI**: A clean interface utilizing Tailwind CSS features and scoped component styling.

## Installation & Setup

1. Prerequisites
   - Python 3.12+
   - Node.js 20+
   - PostgreSQL 16 (running on port 5432)

2. Database Setup
   Create a database name carequeue in PostgreSQL instance.
   Then, update the DATABASE_URL in backend/.env

```
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/carequeue
```

3. Quick Start
   From the root directory, run:

```
# Install all dependencies
npm install && npm install --prefix frontend

# Setup the Python environment
cd backend
python -m venv venv
venv/Scripts/pip install -r requirements.txt # On Windows
cd ..

# Start both frontend and backend concurrently
npm run dev
```

## Architecture Choices

- **Scoped Styling**: Used Vue's `<style scoped>` with Tailwind's `@reference` to ensure zero CSS leakage while maintaining a clean, descriptive template.
- **Type Safety**: Implemented shared TypeScript interfaces in the frontend to mirror Pydantic schemas in the backend, reducing runtime errors.
- **Dependency Injections**: Utilized FastAPI's `Depends` for database session management to ensure efficient connection pooling and clean teardowns.

## Future Roadmap

- **Quick-Change Triage**: Allow clinicians to cycle through priority statuses directly from the card.
- **Audit Logs**: Track when patients were resolved for clinical reporting.
- **WebSockets**: Move from polling to real-time pushes for high-traffic clinics.
