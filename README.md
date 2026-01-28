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
- Test for 404 error handling

## Development

The application runs in debug mode by default. To run in production, set `debug=False` in `app.py`.
