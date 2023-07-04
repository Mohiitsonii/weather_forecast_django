# Weather Forecast App
## Description
The Weather Forecast App is a Django-based application that provides users with accurate and up-to-date weather information for their desired locations. It retrieves weather data from the OpenWeatherMap API and presents it in an intuitive and user-friendly manner.

## Features
- Current weather information for the specified location
- Hourly forecast for the next 48 hours
- Daily forecast for the next 7 days
- Support for multiple locations
- Integration with Google Maps for easy location selection
- Automatic data retrieval and caching to ensure data freshness
- Configurable time sensitivity for data updates
- Unit conversion for temperature and other measurements

## Installation
1. Clone the repository: `git clone https://github.com/your-username/weather-forecast-app.git`
2. Navigate to the project directory: `cd weather-forecast-app`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   - For Windows: `venv\Scripts\activate`
   - For Unix/macOS: `source venv/bin/activate`
5. Install the required dependencies: `pip install -r requirements.txt`
6. Set up the OpenWeatherMap API key in the Django settings file.
7. Apply the database migrations: `python manage.py migrate`
8. Start the development server: `python manage.py runserver`

## Usage
1. Access the application by visiting `http://localhost:8000` in your web browser.
2. Register an account or log in if you already have one.
3. Enter the latitude and longitude of the desired location or use the Google Maps plugin to select a location visually.
4. Choose the type of forecast detailing (e.g., minute, hourly, daily) from the available options.
5. Click on the "Get Forecast" button to retrieve and display the weather forecast.
6. Explore the different sections of the app to view current weather conditions and forecast details.

## Configuration
The following configuration options can be adjusted in the Django settings file (`settings.py`):
- `OPENWEATHERMAP_API_KEY`: The API key for accessing the OpenWeatherMap service.
- `DATA_CACHE_TIME`: The time sensitivity for data updates in minutes (default: 10).

## Contributing
Contributions to the Weather Forecast App are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgements
- The Weather Forecast App utilizes the [OpenWeatherMap API](https://openweathermap.org/api/one-call-api) for weather data.
- The project is built with the Django framework and follows best practices for Django development.

## Contact
For any inquiries or questions, feel free to contact the project maintainers:
- Mohit Soni: [GitHub](https://github.com/Mohitson112)
