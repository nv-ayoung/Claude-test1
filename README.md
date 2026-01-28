# Claude-test1

A simple "Hello World" Flask application.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

## Endpoints

- `GET /` - Returns "Hello, World!"
- `GET /health` - Health check endpoint
- `GET /time` - Returns current date and time in multiple formats

### Time Endpoint Response

The `/time` endpoint returns a JSON object with:
```json
{
  "timestamp": "2026-01-28T10:30:45.123456+00:00",
  "date": "2026-01-28",
  "time": "10:30:45",
  "timezone": "UTC",
  "human_readable": "Tuesday, January 28, 2026 at 10:30:45 AM"
}
```

## Testing

Run the test suite to verify the application is working correctly:

```bash
# Option 1: Run the test script
./run_tests.sh

# Option 2: Run tests directly with Python
python3 test_app.py
```

The test suite includes:
- Test for the main "Hello, World!" endpoint
- Test for the health check endpoint
- Test for the time/date endpoint
- Test for 404 error handling

## Development

The application runs in debug mode by default. To run in production, set `debug=False` in `app.py`.
