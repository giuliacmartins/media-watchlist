const search_title = document.getElementById('search-title');
const search_list = document.getElementById('search-list');
const results = document.getElementById('results');

/* access the API */
async function load_reference (search_term) 
{
    const url = `http://www.omdbapi.com/?s=${search_term}&apikey=17068f89`;
    const resp = await fetch(`${url}`);
    const data = await resp.json();

    if (data.Response == "True")
    {
        display_list(data.Search);
    }
}

/* function to find the references that was typed in */
function find_reference() 
{
    let search_term = (search_title.value).trim();

    if (search_term.length > 0) 
    {
        search_list.classList.remove('hide-search-list');
        load_reference(search_term);
    } 
    else 
    {
        search_list.classList.add('hide-search-list');
    }
}

/* display the references from user search */
function display_list(reference) 
{
    search_list.innerHTML = "";

    for (let i = 0; i < reference.length; i++)
    {
        let list_item = document.createElement('div'); // create new div 
        list_item.dataset.id = reference[i].imdbID; 
        list_item.classList.add('search-list-item');

        /* if poster is avaibale assign to variable otherwise no image found */
        if (reference[i].Poster != "N/A")
        {
            reference_poster = reference[i].Poster;
        }
        else 
        {
            reference_poster = "image_not_found.png";
        }
        
        /* search elements */
        list_item.innerHTML = `
        <div class="search-item-img">
            <img src="${reference_poster}">
        </div>
        <div class = "search-item-info">
            <h3>${reference[i].Title}</h3>
            <p>${reference[i].Year}</p>
        </div>`;
        search_list.appendChild(list_item);
    }
    load_ref_details(); // call funciton to load the reference details 
}

function load_ref_details()
{
    const search_reference = search_list.querySelectorAll('.search-list-item') // return the document elements 
    search_reference.forEach(ref => {
        ref.addEventListener('click', async () => {
            search_list.classList.add('hide-search-list');
            search_title.value = "";

            const result = await fetch(`http://www.omdbapi.com/?i=${ref.dataset.id}&apikey=17068f89`);
            const details = await result.json();
            display_details(details);
        });
    });
}

// documentation provided by OMDB
function display_details(ref_details)
{
    const title = ref_details.Title.replace(/'/g, "\\'")

    results.innerHTML = `
    <div class="reference-poster">
        <img id="reference-img" src="${(ref_details.Poster != "N/A") ? ref_details.Poster : "image_not_found.png"}" alt="movie poster">
    </div>
    <div class="reference-info">
        <h2 class="reference-title">${ref_details.Title}</h2>
        <ul class="reference-misc-info">
            <li class="year">Year: ${ref_details.Year}</li> 
            <li class="rated">Ratings: ${ref_details.Rated}</li>
            <li class="released">Released: ${ref_details.Released}</li>
        </ul>
        <p class = "genre"><b>Genre:</b> ${ref_details.Genre}</p>
        <p class = "writer"><b>Writer:</b> ${ref_details.Writer}</p>
        <p class = "actors"><b>Actors: </b>${ref_details.Actors}</p>
        <p class = "plot"><b>Plot:</b> ${ref_details.Plot}</p>
        <p class = "language"><b>Language:</b> ${ref_details.Language}</p>
        <p class = "awards"><b><i class="fas fa-award"></i></b> ${ref_details.Awards}</p>
    </div>
    <div class="list-button-class">
        <input type="button" id="add-media-button" value="Add to Movie/TV Show List" onClick="addToMediaList('${title}', '${ref_details.Poster}', '${ref_details.Year}', '${ref_details.Genre}')"> 
        <input type="button" id="add-anime-button" value="Add to Anime List" onClick="addToAnimeList('${title}', '${ref_details.Poster}', '${ref_details.Year}', '${ref_details.Genre}')"> 
    </div>`;
}

window.addEventListener('click', (event) => {
    if (event.target.className != "form-control")
    {
        search_list.classList.add('hide-search-list');
    }
});

function getCsrfToken() {
    const cookieString = document.cookie;
    const csrfTokenName = 'csrftoken=';
    const decodedCookie = decodeURIComponent(cookieString);
  
    const cookieArray = decodedCookie.split(';');
    for (let i = 0; i < cookieArray.length; i++) {
      let cookie = cookieArray[i];
      while (cookie.charAt(0) === ' ') {
        cookie = cookie.substring(1);
      }
      if (cookie.indexOf(csrfTokenName) === 0) {
        return cookie.substring(csrfTokenName.length, cookie.length);
      }
    }
    return null;
}
  
const csrftoken = getCsrfToken();

function addToMediaList(title, poster, year, genre) {
    const formData = new FormData();
    formData.append('title', title);
    formData.append('poster', poster);
    formData.append('year', year);
    formData.append('genre', genre);

    clearMessages();
  
    fetch('/api/addmedia', {
      method: 'POST',
      body: formData,
      headers: {
        'X-CSRFToken': csrftoken
      }
    })
    .then(response => response.json())
    .then(data => {
      if (data.status === 'success') {
        console.log('Media added to your list!');
        showMessage('success', data.message);
        setTimeout(() => {
            clearMessages();
        }, 5000);
        //window.location.href = '/search/';
      } else if (data.status === 'error') {
        console.error('Media already added to your list.');
        showMessage('error', data.message);
        setTimeout(() => {
            clearMessages();
        }, 5000);
      }
    })
    .catch(error => {
      console.error('Error:', error);
      console.error('An error occurred while adding the media to your list.');
      showMessage('error', 'An error occurred while adding the media to your list.');
    });
}

function addToAnimeList(animetitle, animeposter, animeyear, animegenre) {
    const formData = new FormData();
    formData.append('animetitle', animetitle);
    formData.append('animeposter', animeposter);
    formData.append('animeyear', animeyear);
    formData.append('animegenre', animegenre);

    clearMessages();
  
    fetch('/api/addanime', {
      method: 'POST',
      body: formData,
      headers: {
        'X-CSRFToken': csrftoken
      }
    })
    .then(response => response.json())
    .then(data => {
      if (data.status === 'success') {
        console.log('Anime added to your list!');
        showMessage('success', data.message);
        setTimeout(() => {
            clearMessages();
        }, 5000);
        //window.location.href = '/search/';
      } else if (data.status === 'error') {
        console.error('Anime already added to your list.');
        showMessage('error', data.message);
        setTimeout(() => {
            clearMessages();
        }, 5000);
      }
    })
    .catch(error => {
      console.error('Error:', error);
      console.error('An error occurred while adding the anime to your list.');
      showMessage('error', 'An error occurred while adding the anime to your list.');
    });
}

function showMessage(type, message) {
    const alertContainer = document.getElementById('alert-container');
    const alertDiv = document.createElement('div');
    alertDiv.classList.add('alert', `alert-${type}`);
    alertDiv.textContent = message;
    alertContainer.appendChild(alertDiv);
}
  
function clearMessages() {
    const alertContainer = document.getElementById('alert-container');
    alertContainer.innerHTML = ''; // Clear the contents of the alert container
}

// filter click 
document.addEventListener('DOMContentLoaded', function() {
    const filterIcon = document.querySelector('.filter-icon');
    const filterForm = document.querySelector('.genre-filter-form');
  
    filterIcon.addEventListener('click', function() {
      filterForm.classList.toggle('show');
    });
});

// star
// document.addEventListener('click', function(event) {
//   if (event.target.classList.contains('fa-star')) {
//     const icon = event.target;
//     const title = icon.dataset.title;
//     const poster = icon.dataset.poster;
//     const year = icon.dataset.year;
//     const genre = icon.dataset.genre;

//     const priorityWatchElement = document.createElement('div');
//     priorityWatchElement.classList.add('media-element');

//     priorityWatchElement.innerHTML = `
//       <img src="${poster}" alt="poster" class="poster">
//       <div class="overlay">
//         <h1 class="card-title">${title}</h1>
//         <p class="card-sub-title">${year} <br> ${genre}</p>
//       </div>
//     `;

//     const priorityWatchDiv = document.getElementById('priority-watch');
//     priorityWatchDiv.appendChild(priorityWatchElement);

//     icon.remove();
//   }
// });
  