# Announcement API

This API is built using FastAPI and SQLAlchemy, and is designed to schedule and send announcements.

## Building the Announcement API Image
To build the API image, run the following command from the root directory of the project:

`docker build -t announcement-api .`

This will create a Docker image with the name `announcement-api`.

## Running the Announcement API Image
To run the API image, use the following command:

`docker run -p 8000:8000 announcement-api`

This will start the API server on port 8000.

## API Endpoints

Announcement API has three endpoints:

- `/schedule_announcement`: This endpoint allows employers to schedule an announcement. It accepts a JSON payload with the announcement content and scheduled time.
  - Example payload:
    ```json
    {
        "content": "This is a test announcement",
        "scheduled_time": "2021-09-01 12:00:00"
    }
    ```
  - Alternatively you can use the following command to schedule an announcement:
    ```bash
    curl -X POST "http://localhost:8000/schedule_announcement" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"content\":\"This is a test announcement\",\"scheduled_time\":\"2021-09-01 12:00:00\"}"
    ```
- `/send_announcements`: This endpoint simulates sending announcements to employees. It retrieves announcements from the database where the scheduled time is less than or equal to the current timestamp.
- `/scheduled_announcements`: This endpoint retrieves scheduled announcements from the database where the scheduled time is greater than or equal to the current timestamp.

## Tests Image
This image is built using Pytest and is designed to test the API endpoints.

### Building the Tests Image

To build the tests image, run the following command from the root directory of the project:

`docker build -f Dockerfile-tests -t my-app-tests .`

This will create a Docker image with the name tests-image.

### Running the Tests Image

To run the tests image, use the following command:

`docker run -it my-app-tests`

This will run the tests and report the results.
