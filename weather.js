const config = {
  apiKey: "xxxx", // Get an api Key here: https://api.openweathermap.org
  useNavigatorGeolocation: false,	location: { lat: 48.89, lon: 2.07 },
  maxForecasts:5
};

function unixToHHMM(unixTS) {
  return new Date(unixTS * 1000).toTimeString().slice(0, 5);
}

function unixToIso(unixTS) {
  return new Date(unixTS * 1000).toLocaleString().replace(" à", "");
}

function getWeatherIcon(x) {
  return `https://openweathermap.org/img/wn/${x}@2x.png`;
}

function getWeekDay(date) {
  return ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"][date.getDay()];
}

function applyPropertiesToDom(pties) {
  for (var key in pties) {
    if (typeof pties[key] == "object" || typeof pties[key] == "array")
      applyPropertiesToDom(pties[key]);
    else {
      var element = document.getElementById(key);
      if (element != undefined) {
  if (key == "dt") 
  	element.innerText = unixToIso(pties[key]);
        else if (key == "sunrise" || key == "sunset")
          element.innerText = unixToHHMM(pties[key]);
  else if (key == "icon") 
  	element.src = getWeatherIcon(pties[key]);
        else element.innerText = pties[key];

        if (key == "deg")
          document.getElementById("windir").style.transform = `rotate(${90 + pties[key]}deg)`;
} 
// else console.log(`Not found: ${key} ${pties[key]}`);
    }
  }
}

/*	https://openweathermap.org/api/weather-call-api */
function getCurrentWeather(data, callBack) {
  var weatherApiUrl = `https://api.openweathermap.org/data/2.5/weather?lat=${data.location.lat}&lon=${data.location.lon}&appid=${data.apiKey}&units=metric`;

  var xmlhttp = new XMLHttpRequest();
  xmlhttp.open("GET", weatherApiUrl, true);
  xmlhttp.withCredentials = false;

  xmlhttp.onreadystatechange = function () {
    if (xmlhttp.readyState == 4) {
      if (xmlhttp.status == 200) {
        var weather = JSON.parse(xmlhttp.responseText);
        callBack(weather);
      }
    }
  };
  xmlhttp.send(null);
}

/* https://openweathermap.org/forecast5 */
function getForecastWeather(data, callBack) {
  var weatherApiUrl = `https://api.openweathermap.org/data/2.5/forecast?lat=${data.location.lat}&lon=${data.location.lon}&appid=${data.apiKey}&units=metric&cnt=${data.maxForecasts}`;

  var xmlhttp = new XMLHttpRequest();
  xmlhttp.open("GET", weatherApiUrl, true);
  xmlhttp.withCredentials = false;

  xmlhttp.onreadystatechange = function () {
    if (xmlhttp.readyState == 4) {
      if (xmlhttp.status == 200) {
        var forecast = JSON.parse(xmlhttp.responseText);
        callBack(forecast);
      }
    }
  };
  xmlhttp.send(null);
}

function displayForecast(forecast) {
  const fragment = document.getElementById("forecastWidgetTemplate");
  const target = document.getElementById("forecast");

  forecast.list.map((wl) => {
    // Create an instance of the template content
    const instance = document.importNode(fragment.content, true);

    // Add relevant content to the template
    const dt = new Date(wl.dt * 1000);
    instance.querySelector("#dt").innerHTML = getWeekDay(dt);
    instance.querySelector("#dtTimeForecast").innerHTML = unixToHHMM(wl.dt);
    instance.querySelector("#temp_min").innerHTML = wl.main.temp_min;
    instance.querySelector("#temp_max").innerHTML = wl.main.temp_max;
    instance.querySelector("#pressure").innerHTML = wl.main.pressure;
    instance.querySelector("#humidity").innerHTML = wl.main.humidity;
    instance.querySelector("#speed").innerHTML = Math.floor((wl.wind.speed * 3600) / 1852); // m/s -> Kt
    instance.querySelector("#deg").innerHTML = wl.wind.deg;
    instance.getElementById("windir").style.transform = `rotate(${90+wl.wind.deg}deg)`;

    wl.weather.map((wt) => {
      instance.querySelector("#icon").src = getWeatherIcon(wt.icon);
      instance.querySelector("#description").innerHTML = wt.description;
    });

    // Append the instance ot the DOM
    target.appendChild(instance);
  });
}

function getWeather() {
  if (config.useNavigatorGeolocation && "geolocation" in navigator) {
    navigator.geolocation.getCurrentPosition(function (position) {
      config.location.lat = position.coords.latitude;
      config.location.lon = position.coords.longitude;
    });
  }

  getCurrentWeather(config, applyPropertiesToDom);
  getForecastWeather(config, displayForecast);
}

getWeather();