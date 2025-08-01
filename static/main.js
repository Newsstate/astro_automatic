
async function fetchPanchang() {
    const date = document.getElementById('dateInput').value;
    const url = `/panchang?date=${date}`;
    const response = await fetch(url);
    const data = await response.json();
    document.getElementById('output').textContent = JSON.stringify(data, null, 2);
}
