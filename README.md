# ERP / Accounting System (Test Task)

A robust Flask-based backend application for managing business operations, including document workflows, product movements, and basic accounting. This project is a demonstration of clean architecture, Pydantic validation, and SQLAlchemy ORM usage in a business-oriented context.

### Key Features
- **Document Workflow Management**: Complete lifecycle for Orders, Invoices, Goods Received/Delivery Notes, and Tax Invoices.
- **Inventory Tracking**: Automated product movement recording and status management.
- **Directory Services**: Management of Organizations, Counterparties, Warehouses, and Contracts.
- **Nomenclature**: Support for both Products and Services with detailed categorization.
- **Architecture**:
  - **Service-View-Model Pattern**: Decoupled business logic from API endpoints.
  - **Polymorphic Models**: Extensible document system using SQLAlchemy inheritance.
  - **Type Safety**: Strong validation via Pydantic schemas.

### Tech Stack
- **Framework**: Flask
- **ORM**: SQLAlchemy
- **Validation**: Pydantic
- **Database**: SQLite (default for development)
- **Environment**: Python 3.12+

### Quick Start

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment**:
   Create a `config.py` (or use the provided default) and ensure `SQLALCHEMY_DATABASE_URI` is set.

3. **Initialize Database**:
   The application automatically creates tables on startup:
   ```python
   from flaskr import init_app
   app = init_app()
   ```

4. **Run the server**:
   ```bash
   python ws.py
   ```

### API Structure
The API is organized into several blueprints:
- `/documents`: Order and document management.
- `/accounting`: Financial operations and product movements.
- `/directory`: Management of core business entities.
- `/nomenclature`: Product and service definitions.
- `/bank`: Bank accounts and currency management.
- `/reports`: Business analytics and reporting.
