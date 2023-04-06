const API_URL = 'http://localhost:5000/api/data';

export async function fetchData() {
    const response = await fetch(`${API_URL}/data`);
    const data = await response.json();
    return data;

}