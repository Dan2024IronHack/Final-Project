# Import python libraries
import streamlit as st
import pandas as pd
from googleapiclient.discovery import build

def cook():
    
    st.markdown(
    """
    <style>
    .main {
    background-color: #99ffcc
    }

    .block-container {
    background-color: #99ffcc;
    }
    .stHeader {
    background-color: #99ffcc;
    }

    </style>
    """,
    unsafe_allow_html=True,
    )

    st.image('images/fresh.jpg')
    st.title("Let's choose the ingredient")

    # Function to read recipe data from CSV file
    def load_recipe_data(file_path):
            return pd.read_csv(file_path)

    # Function to recommend a recipe based on a given ingredient
    def recommend_recipe_with_ingredient(df, ingredient):
        mask = df['item'].apply(lambda x: ingredient in x)
        if mask.any():
            recipes_with_ingredient = df[mask]
            recommended_recipe = recipes_with_ingredient.sample(1)[['title', 'ingredients', 'directions', 'cluster']]
            return recommended_recipe
        else:
            return None

    # Function to search for YouTube videos with a specific title
    def search_youtube_video(title, api_key):
        youtube = build('youtube', 'v3', developerKey=api_key)
        search_response = youtube.search().list(
            q=title,
            part='id',
            maxResults=1,
            type='video'
        ).execute()
        video_id = search_response['items'][0]['id']['videoId']
        video_link = 'https://www.youtube.com/watch?v=' + video_id
        return video_link

    st.title('Recipe Recommendation App')

    file_path = "data3.csv"

    if file_path:
        recipe = load_recipe_data(file_path)

        ingredient = st.text_input("Enter an ingredient (all lower caps)and then click Recommend Recipe ")

        if st.button('Recommend Recipe (click here)'):
            recommended_recipe = recommend_recipe_with_ingredient(recipe, ingredient)
            if recommended_recipe is not None:
                st.write("Good choice and let's make it")
                st.write("Recommended recipe containing", ingredient + ":")
                st.write("Recipe Name:", recommended_recipe['title'].iloc[0])
                st.write("No of Cluster:", recommended_recipe['cluster'].iloc[0])
                st.write("Ingredients to do:", recommended_recipe['ingredients'].iloc[0])
                st.write("How to make it :", recommended_recipe['directions'].iloc[0])
                st.image('./images/Luigigo.jpg',width=200)    
            
                with open("youtube.txt", "r") as file:
                    api_key = file.readline().split(':')[1].strip()
            
                video_link = search_youtube_video(recommended_recipe['title'].iloc[0], api_key)
                st.write("Let's watch the video to make it:", video_link)
            else:
                st.write("No recipes found with the ingredient:", ingredient)
               
            
                