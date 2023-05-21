# AirQualityExplorer

AirQualityExplorer is a Flask API designed to fetch, process, and visualize real-time air quality data. The API utilizes Docker and a Postgres database to store and manage the air quality readings. This document provides instructions for setting up and running the API locally.

## Getting Started

To run the AirQualityExplorer API, follow the steps below:

1. Clone the repository from GitHub.

2. Install Docker on your machine. Refer to the Docker documentation for installation instructions specific to your operating system.

3. Once Docker is installed, open the command line or terminal and navigate to the cloned repository directory.

4. Run the following command to start the API and initialize the Postgres database:

   ```shell
   docker compose up
   ```

   This command will spin up the Postgres database and initialize it from scratch. Once the database is up and running, the Flask API will be launched. During the initialization process, any missing database tables will be created, and the API will start pulling real-time air quality data from OpenAQ every 5 seconds for Norway, Denmark, Sweden, Finland, and Iceland. The retrieved data will be stored in the Postgres database.

5. After the initialization is complete, you can access the API endpoints and test them using the Swagger documentation available at: [http://localhost:8888/apidocs](http://localhost:8888/apidocs).

6. Additionally, you can view a simple interactive map of the pollutant data from different countries gathered so far by visiting [http://localhost:8888](http://localhost:8888).

Certainly! Here's an updated version of the API endpoints section that includes the information about using the default credentials to access the Postgres database:

### API Endpoints

### Retrieve Measurements by Pollutant

- **Endpoint:** `/measurement/{pollutant}`
- **Method:** GET
- **Description:** Retrieves a list of measurements for the specified pollutant.
- **Parameters:**
  - `pollutant` (path parameter, required): The pollutant to retrieve measurements for.
- **Responses:**
  - `200 OK`: Returns a list of measurements for the given pollutant. Each measurement is represented by the `Measurement` object.
  - `404 Not Found`: Indicates that no measurements were found for the specified pollutant.

### Retrieve Measurements by Pollutant and Country

- **Endpoint:** `/measurement/{pollutant}/{country}`
- **Method:** GET
- **Description:** Retrieves a list of measurements for the specified pollutant in the specified country.
- **Parameters:**
  - `pollutant` (path parameter, required): The pollutant to retrieve measurements for.
  - `country` (path parameter, required): The country code (e.g., NO, DK, SE, IS, FI) to retrieve measurements for.
- **Responses:**
  - `200 OK`: Returns a list of measurements for the given pollutant in the specified country. Each measurement is represented by the `Measurement` object.
  - `404 Not Found`: Indicates that no measurements were found for the specified country.

### Retrieve Measurements by Pollutant, Country, and City

- **Endpoint:** `/measurement/{pollutant}/{country}/{city}`
- **Method:** GET
- **Description:** Retrieves a list of measurements for the specified pollutant in the specified city of the specified country.
- **Parameters:**
  - `pollutant` (path parameter, required): The pollutant to retrieve measurements for.
  - `country` (path parameter, required): The country code (e.g., NO, DK, SE, IS, FI) to retrieve measurements for.
  - `city` (path parameter, required): The city to retrieve measurements for.
- **Responses:**
  - `200 OK`: Returns a list of measurements for the given pollutant in the specified city. Each measurement is represented by the `Measurement` object.
  - `404 Not Found`: Indicates that no measurements were found for the specified city.

### Retrieve Measurements by Pollutant, Latitude, Longitude, and Radius

- **Endpoint:** `/measurement/{pollutant}/{latitude}/{longitude}/{radius}`
- **Method:** GET
- **Description:** Retrieves a list of measurements for the specified pollutant within the specified geographic area.
- **Parameters:**
  - `pollutant` (path parameter, required): The pollutant to retrieve measurements for.
  - `latitude` (path parameter, required): The decimal latitude of the center point of the area.
  - `longitude` (path parameter, required): The decimal longitude of the center point of the area.
  - `radius` (path parameter, required): The radius (in kilometers) around the center point to retrieve measurements for.
- **Responses:**
  - `200 OK`: Returns a list of measurements for the given pollutant in the specified area. Each measurement is represented by the `Measurement` object.
  - `404 Not Found`: Indicates that no measurements were found for the specified area.

### Accessing the Postgres Database

The Postgres database used by the AirQualityExplorer API can be accessed using the following default credentials:

- **Host:** localhost
- **Port:** 5432


- **Database Name:** aqe
- **Username:** postgres
- **Password:** postgres

To access the database using a database tool such as pgAdmin or DBeaver, follow these steps:

1. Install and open the database tool on your machine.

2. Create a new database connection or connection profile.

3. Configure the connection settings with the following details:

   - **Host:** localhost
   - **Port:** 5432
   - **Database Name:** aqe
   - **Username:** postgres
   - **Password:** postgres

4. Save the connection profile and establish a connection to the database.

Once connected, you can use the database tool to view and interact with the contents of the `measurement` table in the Postgres database.