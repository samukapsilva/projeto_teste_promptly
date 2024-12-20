
### Section Explanation:

1. **PROMPTLY TEST PROJECT**:
- The promptly test project aims to ingest raw data from different sources, transform this data and save it in a rich format to serve interested areas, create data products, dashboards, among others.

2. **Project Structure**:
- The project is structured in independent modules, including the **extraction**, **transformation**, **loading** and **orchestration** parts.

3. **Requirements and Installation**:
- To install the dependencies, run the `requirements.txt` file.

4. **Project Execution**:
- To run the project manually, run the main.py file, to automate the process, run the promptly_orquestration.py file, configuring the necessary services (PostgreSQL, MinIO, Airflow), which can be done in the config.properties file.

5. **Directory Structure**:
- The files related to data ingestion are in the 'ingestion' folder
- The files related to data transformation are in the 'transformation' folder
- The file related to project orchestration is in the orchestration folder
- A knowledge base to help with common problems is in the project root folder with the name knowledge_base.md

6. **Final Considerations and TODO**:
- The entire logging part was done only in the main class, but the idea is to expand it to the rest of the project and then work on them with elasticsearch, monitor in grafana, etc.

7. **License**:
- Created only for exercise and granted to promptly without any copyright requirement.
