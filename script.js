document.addEventListener("DOMContentLoaded", () => {
  const ipInfoDiv = document.getElementById("ip-info");

  const displayError = (message) => {
    ipInfoDiv.textContent = message;
  };

  const displayIpInfo = (data) => {
    ipInfoDiv.innerHTML = `
            <p><strong>IP Address:</strong> ${data.ip}</p>
            <p><strong>City:</strong> ${data.city}</p>
            <p><strong>Region:</strong> ${data.region}</p>
            <p><strong>Country:</strong> ${data.country_name}</p>
            <p><strong>ISP:</strong> ${data.org}</p>
        `;
  };

  const fetchIpInfo = async () => {
    try {
      const response = await fetch("/api/ipinfo");
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      const data = await response.json();
      if (data.error) {
        displayError(`Error: ${data.error}`);
      } else {
        displayIpInfo(data);
      }
    } catch (error) {
      displayError(`Error fetching IP information: ${error.message}`);
    }
  };

  fetchIpInfo();
});
