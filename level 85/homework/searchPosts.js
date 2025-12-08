const searchForm = document.getElementById('search-form');
const searchInput = document.getElementById('search-input');
const resultsContainer = document.getElementById('results-container');
const API_URL_BASE = 'https://dummyjson.com/posts/search?q=';

async function fetchInfo(query) {
    resultsContainer.innerHTML = 'Loading...';
    const fullUrl = `${API_URL_BASE}${query}`;

    try {
        const response = await fetch(fullUrl);
        if (!response.ok) {
            throw new Error(`HTTP Error: ${response.status}`);
        }
        const data = await response.json();
        
        const filteredPosts = data.posts.filter(post => 
            post.title.toLowerCase().includes(query.toLowerCase())
        );

        renderInfo(filteredPosts, query);

    } catch (error) {
        resultsContainer.innerHTML = `<p>Error: ${error.message}</p>`;
    }
}

function renderInfo(posts, query) {
    resultsContainer.innerHTML = '';
    let outputHTML = '';

    if (posts.length === 0) {
        resultsContainer.innerHTML = `<p>${query}</p>`;
        return;
    }

    for (const post of posts) {
        const tagsList = post.tags.map(tag => `#${tag}`).join(', ');

        outputHTML += `
            <div>
                <h3>${post.title}</h3>
                <p><strong>Body:</strong> ${post.body.substring(0, 150)}...</p>
                <p><strong>Views:</strong> ${post.views.toLocaleString()}</p>
                <p><strong>Tags:</strong> ${tagsList}</p>
                <hr>
            </div>
        `;
    }
    
    resultsContainer.innerHTML = outputHTML;
}

searchForm.addEventListener('submit', (event) => {
    event.preventDefault();
    const query = searchInput.value.trim();

    if (query) {
        fetchInfo(query);
    } else {
        resultsContainer.innerHTML = '<p>Please enter a search keyword.</p>';
    }
});