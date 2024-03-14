# Final-Project-IronHack 2024

# Recipe Recommendation App

This is a simple web application built with Streamlit that recommends recipes based on user input ingredients. 
The app also provides links to related YouTube videos for the recommended recipes.

## Getting Started

1. Data found at https://recipe-search.typesense.org
2. Data cleaning would be to know how much we can do the data for making a model
3. Data Exploration would be to chek  on the ingredienst to be able to make a cluster based on the ingredients input from the users
4. Data scaler is dne after the data divided into 2 dataframe, one for recipe and how to make it, the second daframe would be the ingredients that can ba change into numerical by grouping it and scaled by using Standard scaler. 
5. Data Clustering is done from chosing the elbow and give the possible cluster of 13 from 2000 receipe available
6. Data Modeling are done by making a function to input from the users and chosing the cluster that have the ingredient and porposing the recipe along with the ingredients composition and direction on how to making the dishes. 
7. Data API is done by searching video content from Youtube and connect it using API based on the Dishes Title. 
8. Data visualizatiion is done by conneting the Python file to Streamlit so the apps can be more easily to understand

## Usage

1. Open the Streamlit the show **Recipe Recomendattion App**
2. There is **Home, Let's Cook Today &  End** button in the left side
3. Enter **an ingredient** in **the input box.**
4. Click **"Recommend Recipe"** to get a recommended recipe.
5. To view recipe vieo in **YouTube** then **click video link**.

PS: Sometime the video did not really match as it take the title that at least contains the dishes name 

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is done to complete Data Analyst Bootcamp IronHack - Amsterdam 2024.