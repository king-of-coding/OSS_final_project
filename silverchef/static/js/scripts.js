document.getElementById('search-button').addEventListener('click', async () => { // 버튼을 누르면 함수 실행
    const recipeInput = document.getElementById("recipe-input").value; // 사용자가 입력한 레시피 저장

    if (recipeInput) {
        try {
            const response = await fetch(`/translate_and_search?recipe_name_ko=${encodeURIComponent(recipeInput)}`);// fetch api를 사용하여 서버에 요청 보냄
            const data = await response.json();
            displayRecipes(data.recipes);
        } catch (error) {
            console.error("Error:", error);
        }
    }
});

function displayRecipes(recipes) { // 레시피 목록을 화면에 표시하는 함수
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

