from flask import Flask, redirect, render_template, request, url_for
from weather import get_curent_weather
from waitress import serve

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/weather", methods=["POST", "GET"])
def get_weather():
    city = request.values.get("city", "").strip()
    if not city:
        return redirect(url_for("index"))

    weather_data = get_curent_weather(city)

    if weather_data.get("cod") != 200:
        return render_template(
            "weather.html",
            title=city,
            status="City not found",
            temperature="N/A",
            feels_like="N/A",
            humidity="N/A",
        )
    return render_template(
        "weather.html",
        title=city,
        status=weather_data["weather"][0]["description"],
        temperature=weather_data["main"]["temp"],
        feels_like=weather_data["main"]["feels_like"],
        humidity=weather_data["main"]["humidity"],
    )


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)
