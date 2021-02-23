## Set Up
This environment requires `docker` and specifically we will be using `docker-compose`. If your machine does not have it, download it here https://www.docker.com/get-started .
MacOS installation should be seamless. On Windows you will need WSL2. Sometimes WSL2 is not enabled in docker by default. The setting is located in docker under `Resources>WSL Integration`. Additionally, you may need to run docker-compose as sudo.

## Run

To build the 3 docker containers that will automatically initialize our postgresql database and python scripts:

first
```cd dockerbuild```
then
```docker-compose up```

When the program has completed you should see `dockerbuild_python_1 exited with code 0` this means that `./scripts/projection_cleanup.py` successfully ran.

scroll up in your terminal to find your jupyer notebook link.
Its the last line in `datascience-notebook-1` and it should look similar to this:

`datascience-notebook_1  |      or http://127.0.0.1:8888/?token=[your token]`

copy the link into your web browser.

Inside jupyter notebook there is a folder within root called work, this folder maps to `output` in this github repo.

Open `out.ipynb`

Press
`Kernel>Restart and Run All>Restart and Run All Cells`

The desired output should be in `output [8]`

The PostgreSQL db is exposed on the local machine on port 5433. Default postgres user and the password is stored in docker-compose.yml file.

--------------------------------------------------------------------------------------------------------------------------------------------------

## Introduction
Welcome to Aspen Capital's Data Engineering challenge. This assignment will help us better assess your technical skills. We recommend that you focus on the requirements listed below and if time permitting - work on any additional features (of your own choosing).

## Background
One aspect of this job is the forecasting of payments, and for this exercise, we need to create a payment schedule. Part of the schedule is projected, and the other is actual payments. We need to line up projection and actual payments given the provided database schema.

## Requirements
### High Level
* Given the provided scripts (./data/init.sql), create software that will display the following chart:

### Example (given sample data)
|Projection | Month/Year  | Activity   | Estimated | Actual | Estimated Balance
|---------- | ----------- | --------   | --------- | ------ | ----------------- |
|1|
|| April 2019  | Deposit: Insurance    | $54.95    |
||             | Withdrawal: Insurance | $-1.81   | $-2.04    | $214.85
|| May 2019    | Deposit: Insurance    | $54.95    |
||             | Withdrawal: Insurance | $-1.81   | $-2.27    | $267.99
|| June 2019   | Deposit: Insurance    | $54.95    |
||             | Withdrawal: Insurance | $-1.81   | $-2.18    | $321.13
|| July 2019   | Deposit: Insurance    | $54.95    |
||             | Withdrawal: Insurance | $-1.81   | $-2.26    | $374.27
|| August 2019 | Deposit: Insurance    | $54.95    |
||             | Withdrawal: Insurance | $-1.81   | $-9.38    | $427.41
||             | Withdrawal: Insurance |          | $-9.38    |
||             | Withdrawal: Insurance |          | $-9.38    |
||......|......|......|......
||......|......|......|......
|2|......|......|......|......
||......|......|......|......
||......|......|......|......

## Hints
* You can assume there are only 12 months of data in a single projection.
* This needs to work on a large number of rows (Only example data provided).
* It is ok to choose any database technology.
* Do your best with the information available.

## Bonus Points
* Provide the ability to run your solution.
* High level data injection design.
* Alternative solution to this type of schema and a possible path to migrate it.

## Submission
* Your submission should be accessible in a public git repository that includes a README.md with all the pertinent information of how to run your application. The expectation is that we can easily follow the steps provided and run the application without much leg/guesswork.
* If your submission does include additional artifacts that are not represented within the repository - the README should provide information on how to retrieve and access these items.
