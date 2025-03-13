# rdbs_benchmark_python
Just some RDBMSs benchmarks based on simple CRUD operations (but in Python)

## Table of contents
- [Requirements](#requirements)
- [Quick Start](#quick-start)
- [Built In - Technologies](#built-in---technologies)

## Requirements
- [MySQl](https://www.mysql.com/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [Python 3.12](https://www.python.org/downloads/)

## Quick Start
In order to begin benchmarking your databases, you will need to do the following:
- Startup both MySQL and PostgreSQL databases
- Create a new database <code>called rdbms_benchmark</code>
- Use the provided DDL scripts to create the tables (located under <code>/src/databasess</code>
- Add a virtual environment and install the modules using <code>pip3 install -r requirements.txt</code>
- Update your database connection info from the <code>.env.sample</code> file and rename it to just <code>.env</code>
- Get an API key from [Rapid API's public API](https://rapidapi.com/Glavier/api/spotify23) and place it in the your <code>.env</code> file
- Run your program!

## Built In - Technologies
- [Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
- [PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
- [MySQL](https://dev.mysql.com/doc/refman/8.4/en/)
