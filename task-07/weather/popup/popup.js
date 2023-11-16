document.addEventListener('DOMContentLoaded', documentEvents  , false);

function myAction(input) { 
    console.log("input value is : " + input.value);
    var place = (input.value);
    place = place.toUpperCase();
    
    var url = "https://api.openweathermap.org/data/2.5/weather?q="+ input.value + "&appid=f9e03161fec370dbe7096a914113c7fd";
    
    function renderWeather(weather) {
        if (weather){
            c = weather.main.temp - 273
            var ans = document.getElementById('ans');
            ans.innerHTML = (Math.round(c))+ "&degC";
            document.getElementById("placeName").innerHTML = (place);
            container = document.getElementById("container");
            heading = document.getElementById("heading");
            if (c<15){
              container.style.backgroundColor = "blue";
              heading.style.color = "white";
            }
            else if(c>=15 && c<35){
              container.style.backgroundColor = "orange";
              heading.style.color = "white";
            }
            else{
              container.style.backgroundColor = "red";
              heading.style.color = "white";
            }

        }
        else {
            console.log("data not found!!!");
            document.getElementById("placeName").innerHTML = "data not found!!!"
        }
        
    }

    fetch(url)
        .then((response) => response.json())
        .then((data) => renderWeather(data))
    
    
}

function documentEvents() {    
  document.getElementById('myBtn').addEventListener('click', 
    function() { myAction(document.getElementById('place'));
  });

  // you can add listeners for other objects ( like other buttons ) here 
}
