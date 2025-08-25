let map;

function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: -37.8136, lng: 144.9631 }, // Centered around Melbourne
        zoom: 10,
    });

    // Example data. Replace this with data from the spreadsheet.
    const locations = [
        { name: "Warrigal Road", suburb: "Oakleigh", lat: -37.88702019999997, lng: 145.0895205 }
    ];

    // Custom icon URL (replace with your own icon URL if desired)
    const customIcon = {
        url: "https://maps.google.com/mapfiles/kml/shapes/placemark_circle.png", // Replace with your custom icon URL
        scaledSize: new google.maps.Size(32, 32), // Adjust size if necessary
    };

    // Create an info window to display street name and suburb
    const infoWindow = new google.maps.InfoWindow();

    // Add a marker for each location
    locations.forEach((location) => {
        const marker = new google.maps.Marker({
            position: { lat: location.lat, lng: location.lng },
            map: map,
            icon: customIcon,
            title: `${location.name}, ${location.suburb}`,
        });

        // Add a hover event to open the info window
        marker.addListener("mouseover", () => {
            // Styled content for the info window
            const content = `
                <div style="
                    font-family: 'Arial', sans-serif; 
                    font-size: 14px;
                    text-align: center;">
                    <div style="
                        background-color: #4CAF50; 
                        color: white; 
                        border-radius: 10px 10px 0 0; 
                        padding: 8px 8px; 
                        font-size: 16px;
                        font-weight: bold;">
                        ${location.name}
                    </div>
                    <p style="
                        margin: 10px 0 0 0; 
                        color: #555;">
                        Suburb: <strong>${location.suburb}</strong>
                    </p>
                </div>
            `;
            infoWindow.setContent(content);

            // Open the info window
            infoWindow.open(map, marker);

            // Adjust InfoWindow layout after it's rendered
            google.maps.event.addListenerOnce(infoWindow, "domready", () => {
                const iwOuter = document.querySelector(".gm-style-iw");
                const iwBackground = iwOuter?.previousElementSibling;

                // Remove padding and margin for the content
                if (iwOuter) {
                    iwOuter.style.padding = "0";
                    iwOuter.style.margin = "0";
                }

                // Remove background shadow and borders
                if (iwBackground) {
                    Array.from(iwBackground.children).forEach((child) => {
                        child.style.display = "none";
                    });
                }

                // Remove unnecessary padding from content wrapper
                const iwContent = iwOuter?.querySelector(".gm-style-iw-c");
                if (iwContent) {
                    iwContent.style.padding = "0";
                    iwContent.style.margin = "0";
                }

                // Ensure no padding between InfoWindow and its content
                const iwContentWrapper = iwOuter?.querySelector(".gm-style-iw-d");
                if (iwContentWrapper) {
                    iwContentWrapper.style.padding = "0";
                    iwContentWrapper.style.margin = "0";
                }
            });
        });
        
        // Close the info window when the mouse is out
        marker.addListener("mouseout", () => {
            infoWindow.close();
        });
    });
}