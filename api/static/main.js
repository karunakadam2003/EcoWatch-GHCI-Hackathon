const world = Globe()
  .globeImageUrl('//unpkg.com/three-globe/example/img/earth-blue-marble.jpg')
  .bumpImageUrl('//unpkg.com/three-globe/example/img/earth-topology.png')
  .backgroundColor("#ffffff00")
  .width(600)
  .height(600)
  (document.getElementById('globeViz'));

const globeMaterial = world.globeMaterial();
globeMaterial.bumpScale = 10;

const marker = { lat: 0, lng: 0, size: 0.5, color: 'red' };

// Initial marker setup
world
  .pointsData([marker])
  .pointAltitude(d => d.size)
  .pointColor(d => d.color);

// Track the drag with globe click
world.onGlobeClick(({ lat, lng }) => {
    marker.lat = lat;
    marker.lng = lng;
    world.pointsData([marker]);
    console.log(`Marker set to Latitude: ${lat}, Longitude: ${lng}`);
});

// "Set" button click event to send coordinates to the backend
document.getElementById("setButton").addEventListener("click", () => {
    console.log(`Set button clicked with Latitude: ${marker.lat}, Longitude: ${marker.lng}`);
    
    // Send coordinates to the backend
    fetch('/set-location', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ lat: marker.lat, lng: marker.lng })
    })
    .then(response => response.json())
    .then(data => {
        console.log("Location set:", data);

        // Display the message box with coordinates
        const messageBox = document.getElementById("messageBox");
        messageBox.style.display = 'block';
        messageBox.textContent = `Coordinates added successfully! Latitude: ${data.latitude}, Longitude: ${data.longitude}`;

        // Hide the message box after a few seconds (optional)
        setTimeout(() => {
            messageBox.style.display = 'none';
        }, 5000);  // Hide after 5 seconds
    })
    .catch(error => console.error("Error:", error));
});
