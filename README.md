# Final Weather

A simple Flask web application that fetches and displays current weather
conditions for a city using the OpenWeatherMap API.

## Features

- Search for the current weather by city name.
- Display the weather description, temperature, feels-like temperature, and
  humidity.
- Render HTML pages with Jinja templates.
- Serve CSS from Flask's `static` directory.
- Use environment variables for the OpenWeatherMap API key.
- Run with Flask's development server or Waitress.

## Tech Stack

- Python
- Flask
- Jinja2
- Requests
- python-dotenv
- Waitress
- HTML and CSS
- OpenWeatherMap API

## Project Structure

```text
Final Weather/
├── server.py             # Flask application and routes
├── weather.py            # OpenWeatherMap API integration
├── requirements.txt      # Python dependencies
├── .env                  # Local environment variables (not committed)
├── static/
│   └── style.css         # Application styles
└── templates/
    ├── index.html        # City search page
    └── weather.html      # Weather results page
```

## Prerequisites

- Python 3.10 or newer
- An OpenWeatherMap account
- An OpenWeatherMap API key

You can create an API key from the
[OpenWeatherMap API keys page](https://home.openweathermap.org/api_keys).

## Installation

### 1. Clone the repository

```powershell
git clone <your-github-repository-url>
cd "Final Weather"
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
py -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, either allow scripts for the current
user or use the virtual environment's Python executable directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Configure the API key

Create a file named `.env` in the project root:

```env
API_KEY=your_openweathermap_api_key
```

Do not commit `.env` or share your API key. The file is excluded by
`.gitignore`.

## Running the Application

### Flask development server

```powershell
py -m flask --app server run
```

Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in a browser.

If the `py` launcher is not using the virtual environment, run:

```powershell
.\.venv\Scripts\python.exe -m flask --app server run
```

### Waitress server

The application also includes a Waitress entry point:

```powershell
python server.py
```

The app will listen on port `5000` on all interfaces.

## How to Use

1. Open the home page.
2. Enter a city name, such as `London` or `Nagpur`.
3. Select **Get Weather**.
4. Review the current weather results.

Opening `/weather` without a city redirects back to the home page. A city can
also be supplied directly with a query string:

```text
http://127.0.0.1:5000/weather?city=London
```

## Application Routes

| Method | Route | Description |
| --- | --- | --- |
| `GET` | `/` | Displays the city search form |
| `GET` | `/index` | Alias for the city search form |
| `GET`, `POST` | `/weather` | Retrieves and displays weather for a city |

## API Integration

The application uses two OpenWeatherMap endpoints:

1. Geocoding API to convert the city name into latitude and longitude.
2. Current Weather API to retrieve weather data using those coordinates.

Temperatures are requested in metric units, so the result is displayed in
degrees Celsius.

## Troubleshooting

### `Method Not Allowed`

Start from the home page instead of opening `/weather` directly. The search
form submits a `POST` request to `/weather`, and the route supports both
`GET` and `POST`.

### `City not found`

Check the spelling of the city and confirm that `API_KEY` is present in `.env`.

### API key errors

- Confirm that the variable is named exactly `API_KEY`.
- Restart the server after creating or changing `.env`.
- Confirm that the API key is active in OpenWeatherMap.
- Make sure `.env` is located beside `server.py` and `weather.py`.

### CSS is not loading

Confirm that `static/style.css` exists and that the templates use Flask's
static URL helper:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

Refresh the browser with `Ctrl+F5` after changing the stylesheet.

## Security Notes

- Keep the OpenWeatherMap API key in `.env`.
- Never commit `.env` to GitHub.
- Do not hard-code API keys in Python, HTML, or CSS files.
- For production, run behind a properly configured reverse proxy and use
  HTTPS.
