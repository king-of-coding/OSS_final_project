document.getElementById('search-button').addEventListener('click', async () => {
    const recipeInput = document.getElementById("recipe-input").value;

    if (recipeInput) {
        try {
            const response = await fetch(`/translate_and_search?recipe_name_ko=${encodeURIComponent(recipeInput)}`);
            const data = await response.json();
            displayRecipes(data.recipes);
        } catch (error) {
            console.error("Error:", error);
        }
    }
});

function displayRecipes(recipes) {
    const recipesContainer = document.getElementById("recipes");
    recipesContainer.innerHTML = "";

    if (recipes && recipes.length > 0) {
        recipes.forEach((recipe, index) => {
            const recipeDiv = document.createElement("div");
            recipeDiv.className = "recipe";
            recipeDiv.innerHTML = `
                <h3>${index + 1}. ${recipe.label}</h3>
                <img src="${recipe.image}" alt="${recipe.label}">
                <p><a href="${recipe.url}" target="_blank">레시피를 보려면 이곳을 클릭하세요</a></p>
            `;
            recipesContainer.appendChild(recipeDiv);
        });
    } else {
        recipesContainer.textContent = "검색 결과가 없습니다.";
    }
}

