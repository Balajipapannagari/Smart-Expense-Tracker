## AI Usage Notes

# Introduction

I chose to use AI tools for this project because I had only 48 hours to complete the assignment. My primary career interest is in becoming a Data Analyst, but I am confident that I can quickly learn new technologies based on a company's project requirements.

I enjoy learning new tools and can work independently on projects. When needed, I can adapt to new technologies in a short period of time.

For this project, I mainly used **Claude** because it can handle larger codebases and generate the complete project structure in a single ZIP file, which helped me work more efficiently.

I also used **ChatGPT** to understand the code and concepts better. Its explanations are clear, step by step, and easy to understand, especially for beginners. It helped me review the implementation and improve my understanding of the project.

## 1. What was AI-generated vs. written by me
### AI-assisted
Generated the initial FastAPI project structure.
Generated the initial implementation of the REST API endpoints.
Generated the initial unit test examples using pytest.
Suggested the README structure and project organization.
### Written and modified by me
Reviewed and understood every endpoint before using it.
Adjusted the project structure to match the required submission format.
Verified the API routes and tested them locally.
Fixed minor issues and formatting where necessary.
Added and organized files according to the assignment requirements.

## 2. What I validated, tested, or changed, and why

After generating the initial code with AI, I:

Installed all required dependencies and verified the project runs successfully.
Tested every endpoint using the FastAPI Swagger UI.
Verified that:
Expenses can be added.
All expenses are returned correctly.
Filtering by category works.
Total expense calculations are correct.
Deleting an expense removes it from the list.
Ran the provided unit tests using pytest.
Reviewed the generated code to ensure it met the assignment requirements.

## 3. AI suggestions I didn't use, and why

I chose not to implement several additional suggestions because they were outside the required scope of the assignment, including:

Database integration (SQLite/PostgreSQL)
User authentication
ORM libraries such as SQLAlchemy
Complex project architecture with multiple services
Additional third-party packages that were not necessary

Instead, I kept the implementation simple by storing data in memory, as allowed in the assignment description.
