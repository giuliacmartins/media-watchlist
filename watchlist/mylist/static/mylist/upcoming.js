// // apikey=17068f89
// // tmdb: 62a4a3b710649252ad7094ec0596a769
var today = new Date();
var todayString = today.toISOString().split("T")[0]; 

async function fetchUpcomingMovies() {
  var apiKey = "62a4a3b710649252ad7094ec0596a769";
  var url = `https://api.themoviedb.org/3/movie/upcoming?api_key=${apiKey}&language=en-US`;

  var response = await fetch(url);
  var data = await response.json();

  if (response.ok) {
    var movies = data.results || [];
    var filteredMovies = movies.filter(function (movie) {
      var releaseDate = new Date(movie.release_date);
      return releaseDate > today;
    });
    return filteredMovies;
  } else {
    throw new Error(data.status_message);
  }
}

async function fetchMovieDetails(movieId) {
  var apiKey = "62a4a3b710649252ad7094ec0596a769";
  var url = `https://api.themoviedb.org/3/movie/${movieId}?api_key=${apiKey}&language=en-US`;

  var response = await fetch(url);
  var data = await response.json();

  if (response.ok) {
    return data;
  } else {
    throw new Error(data.status_message);
  }
}

function createMovieElement(movie) {
  var posterURL = `https://image.tmdb.org/t/p/w300${movie.poster_path}`;

  return `
    <div id="upcoming-movie" class="toast show animated-fade-in">
        <div class="toast-header">
            <strong class="me-auto">UPCOMING: Releasing ${movie.release_date}</strong>
            <button type="button" class="btn-close" data-bs-dismiss="toast"></button>
        </div>
        <div class="toast-body">
            <h5 id="upcoming-info">${movie.title}</h5>
            <button type="button" id="upcoming-info" class="upcoming-info" data-bs-toggle="modal" data-bs-target="#movieModal${movie.id}" onClick="loadMovieDetails(${movie.id})">
                <i class="fa-solid fa-circle-info"></i>
            </button>
            <!--<img class="upcoming-poster" src="${posterURL}" alt="${movie.title}" />-->
            <div>
                <!--<h1>${movie.title}</h1>-->
                <!--<p>Released Date: ${movie.release_date}</p>-->
                <!--<p>Year: ${movie.release_date.split("-")[0]}</p>-->
            </div>
        </div>
    </div>

    <!-- Modal -->
    <div class="modal fade" id="movieModal${movie.id}" tabindex="-1" aria-labelledby="movieModal${movie.id}Label" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="movieModal${movie.id}Label">Movie Info</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div clas="modal-poster">
                        <img class="upcoming-poster" src="${posterURL}" alt="${movie.title}" />
                    </div> 
                    <div clas="modal-content">
                        <h2><span id="movieTitle${movie.id}"></span></h2>
                        <p>Release Date: <span id="movieReleaseDate${movie.id}"></span></p>
                        <p>Overview: <span id="movieOverview${movie.id}"></span></p>
                        <p>Genre: <span id="movieGenre${movie.id}"></span></p>
                    </div> 
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary" onClick="addUpcomingToList('${movie.title}', '${posterURL}', '${movie.release_date.split("-")[0]}', '${movie.id}')">Add to List</button>
                </div>
            </div>
        </div>
    </div>
  `;
}

async function fetchAndDisplayMovies() {
  try {
    var movies = await fetchUpcomingMovies();

    var upcomingMoviesElement = document.getElementById("upcoming-movies");
    var movieHTML = movies.map(createMovieElement).join("");
    upcomingMoviesElement.innerHTML = `<ul>${movieHTML}</ul>`;
  } catch (error) {
    console.log("Error fetching movies:", error);
  }
}

fetchAndDisplayMovies();

function getCsrfToken() {
  const cookieString = document.cookie;
  const csrfTokenName = "csrftoken=";
  const decodedCookie = decodeURIComponent(cookieString);

  const cookieArray = decodedCookie.split(";");
  for (let i = 0; i < cookieArray.length; i++) {
    let cookie = cookieArray[i];
    while (cookie.charAt(0) === " ") {
      cookie = cookie.substring(1);
    }
    if (cookie.indexOf(csrfTokenName) === 0) {
      return cookie.substring(csrfTokenName.length, cookie.length);
    }
  }
  return null;
}

const csrftoken = getCsrfToken();

function addUpcomingToList(title, poster, year, genre) {
  const formData = new FormData();
  formData.append("title", title);
  formData.append("poster", poster);
  formData.append("year", year);
  formData.append("genre", genre);

  clearMessages();

  fetch("/api/addmedia", {
    method: "POST",
    body: formData,
    headers: {
      "X-CSRFToken": csrftoken,
    },
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.status === "success") {
        console.log("Upcoming Media added to your list!");
        showMessage("success", data.message);
        setTimeout(() => {
          clearMessages();
        }, 5000);
        //window.location.href = '/search/';
      } else if (data.status === "error") {
        console.error("Upcoming Media already added to your list.");
        showMessage("error", data.message);
        setTimeout(() => {
          clearMessages();
        }, 5000);
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      console.error(
        "An error occurred while adding the upcoming media to your list."
      );
      showMessage(
        "error",
        "An error occurred while adding the upcoming media to your list."
      );
    });
}

function showMessage(type, message) {
  const alertContainer = document.getElementById("alert-container");
  const alertDiv = document.createElement("div");
  alertDiv.classList.add("alert", `alert-${type}`);
  alertDiv.textContent = message;
  alertContainer.appendChild(alertDiv);
}

function clearMessages() {
  const alertContainer = document.getElementById("alert-container");
  alertContainer.innerHTML = "";
}

async function loadMovieDetails(movieId) {
  try {
    var movieDetails = await fetchMovieDetails(movieId);

    // Update the modal with the movie details
    document.getElementById(`movieTitle${movieId}`).textContent = movieDetails.title;
    document.getElementById(`movieReleaseDate${movieId}`).textContent = movieDetails.release_date;
    document.getElementById(`movieOverview${movieId}`).textContent = movieDetails.overview;
    document.getElementById(`movieGenre${movieId}`).textContent = movieDetails.genres.map(genre => genre.name).join(", ");
  } catch (error) {
    console.log("Error fetching movie details:", error);
  }
}

