from gemini.job_requirements import extract_job_requirements


SAMPLE_JOB_DESCRIPTION="""
We are hiring a Junior Backend Engineer to join our growing team.

Required qualifications:
- Solid understanding of Python and object-oriented programming.
- Experience building and consuming REST APIs.
- Basic knowledge of SQL and relational databases.
- Familiarity with Git and version control workflows.
- Ability to write and debug unit tests.

Preferred qualifications:
- Experience with Docker and containerized applications.
- Exposure to CI/CD pipelines.
- Familiarity with cloud platforms such as AWS or GCP.
- Understanding of authentication and authorization concepts.

Responsibilities:
The candidate will design, build, and maintain backend services, collaborate
with frontend engineers on API contracts, write automated tests, and
participate in code reviews.
"""

result = extract_job_requirements(SAMPLE_JOB_DESCRIPTION)


for req in result.requirements:
    print(req.requirement_type, "-", req.category, "-", req.name)