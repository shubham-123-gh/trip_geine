document.addEventListener("DOMContentLoaded", function () {
    // Hide welcome screen after 3 seconds and show main content
    setTimeout(() => {
        document.getElementById("welcome-screen").style.display = "none";
        document.getElementById("main-content").style.display = "block";
    }, 3000);

    const tabs = document.querySelectorAll(".tab-link");
    const sections = document.querySelectorAll(".tab-content");

    // Tab switching functionality
    tabs.forEach(tab => {
        tab.addEventListener("click", function (event) {
            event.preventDefault();

            // Hide all sections
            sections.forEach(section => section.style.display = "none");

            // Get the section ID corresponding to the clicked tab
            const activeTab = this.getAttribute("data-tab");

            // Show the corresponding section
            document.getElementById(activeTab).style.display = "block";

            // Fetch and display destinations data when the "Destinations" tab is clicked
            if (activeTab === "destinations") {
                fetchDestinations();  // Call the function to fetch all destinations
            }

            // Add active class to the clicked tab
            tabs.forEach(tab => tab.classList.remove('active'));
            this.classList.add('active');
        });
    });

   

    // Fetch Destinations Data from the API
    // Function to fetch and display destinations
function fetchDestinations() {
    const url = 'http://127.0.0.1:5000/destinations'; // Your API endpoint

    fetch('http://127.0.0.1:5000/destinations')

        .then(response => response.json())
        .then(data => {
            let destinationsList = document.getElementById("destinations-list");
            destinationsList.innerHTML = ""; // Clear previous results

            data.forEach(destination => {
                let listItem = document.createElement('li');
                listItem.innerHTML = <a href="#" class="destination-link" data-id="${destination.id}">${destination.name}</a>;
                destinationsList.appendChild(listItem);
            });

            // Add event listener to each destination link
            document.querySelectorAll(".destination-link").forEach(link => {
                link.addEventListener("click", function (event) {
                    event.preventDefault();
                    const destinationId = this.getAttribute("data-id");
                    window.location.href = destination.html?id=${destinationId}; // Redirect to new page with ID
                });
            });
        })
        .catch(error => console.error('Error fetching destinations:', error));
}



    // Get the search input and button elements
    const searchInput = document.getElementById('search-bar');
    const searchButton = document.getElementById('search-btn');
    const searchResults = document.getElementById('search-results');

    
    function displaySearchResults(destinations) {
        const searchResults = document.getElementById('search-results');
        searchResults.innerHTML = '';
    
        if (destinations.length > 0) {
            destinations.forEach(destination => {
                const listItem = document.createElement('div');
                listItem.classList.add('result-item');
                listItem.innerHTML = <h3><a href="destination_details.html?name=${encodeURIComponent(destination.name)}">${destination.name}</a></h3>;
                searchResults.appendChild(listItem);
            });
        } else {
            searchResults.innerHTML = '<p>No destinations found.</p>';
        }
    }
    
    function handleSearch() {
        const searchQuery = searchInput.value.trim();
        if (searchQuery) {
            fetch(http://127.0.0.1:5000/api/search/${searchQuery})
                .then(response => response.json())
                .then(data => {
                    searchResults.innerHTML = "";
                    data.forEach(destination => {
                        const listItem = document.createElement('div');
                        listItem.classList.add('result-item');
                        listItem.innerHTML = <h3>${destination.name}</h3><p>${destination.description}</p>;
                        searchResults.appendChild(listItem);
                    });
                })
                .catch(error => {
                    console.error('Error fetching data:', error);
                    document.getElementById('destinations-list').innerHTML = '<p>Something went wrong! Please try again later.</p>';
                });
        } else {
            searchResults.innerHTML = '<p>Please enter a destination to search.</p>';
        }
    }

    searchButton.addEventListener('click', handleSearch);
    searchInput.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            handleSearch();
        }
    });

    // Preferences
const preferencesBtn = document.getElementById("save-preferences");
if (preferencesBtn) {
    preferencesBtn.addEventListener("click", function () {
        let selectedPreferences = [];
        document.querySelectorAll("input[name='preferences']:checked").forEach(checkbox => {
            selectedPreferences.push(checkbox.value);
        });
        localStorage.setItem("tripPreferences", JSON.stringify(selectedPreferences));
        alert("Preferences saved!");
    });
}
// Handle deep linking via URL hash
const currentHash = window.location.hash.slice(1); // remove '#'
if (currentHash && document.getElementById(currentHash)) {
    document.querySelector([data-tab="${currentHash}"])?.click();
}else{
     // Initially show the "Home" section
     document.getElementById("home").style.display = "block";
     document.querySelector('[data-tab="home"]').classList.add('active');
}

    
});
