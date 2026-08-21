const apiUrl = "https://pxkr6pde27.execute-api.us-east-1.amazonaws.com/Prod/get-count/";

async function updateVisitorCount() {
  try {
    const response = await fetch(apiUrl);
    const data = await response.json();
    document.getElementById("visitor-count").innerText = data.views;
  } catch (error) {
    console.error("Error fetching visitor count:", error);
  }
}

updateVisitorCount();
