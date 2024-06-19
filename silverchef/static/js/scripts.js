document.getElementById('search-button').addEventListener('click', async () => {
    const recipeNameKo = document.getElementById('recipe-input').value;
    if (recipeNameKo) {
        const response = await fetch(`/translate_and_search?recipe_name=${encodeURIComponent(recipeNameKo)}`);
        const recipes = await response.json();
        displayRecipes(recipes);
    }
});

function displayRecipes(recipes) {
    const recipeList = document.getElementById('recipe-list');
    recipeList.innerHTML = '';
    recipes.forEach((recipe, index) => {
        const recipeDiv = document.createElement('div');
        recipeDiv.className = 'recipe';
        recipeDiv.innerHTML = `
            <h2>${index + 1}. ${recipe.label}</h2>
            <img src="${recipe.image}" alt="${recipe.label}">
            <p><a href="${recipe.url}" target="_blank">View Recipe</a></p>
        `;
        recipeList.appendChild(recipeDiv);
    });
}
