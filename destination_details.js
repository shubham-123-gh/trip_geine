document.addEventListener("DOMContentLoaded", function () {
    // Get destination ID from URL
    const urlParams = new URLSearchParams(window.location.search);
    const destinationId = urlParams.get("id");

    if (destinationId) {
        fetch(http://127.0.0.1:5000/destination/${destinationId})
            .then(response => response.json())
            .then(data => {
                document.getElementById("destination-name").textContent = data.name;
                document.getElementById("destination-description").textContent = data.description;

                populateList("hotels-list", data.hotels);
                populateList("restaurants-list", data.restaurants);
                populateList("places-list", data.places);
            })
            .catch(error => console.error('Error fetching destination details:', error));
    } else {
        document.getElementById("destination-name").textContent = "Invalid Destination";
    }
});

function populateList(listId, items) {
    let listElement = document.getElementById(listId);
    listElement.innerHTML = ""; // Clear previous content

    if (items.length > 0) {
        items.forEach(item => {
            let listItem = document.createElement("li");
            listItem.textContent = item;
            listElement.appendChild(listItem);
        });
    } else {
        listElement.innerHTML = "<li>No data available</li>";
    }
}
