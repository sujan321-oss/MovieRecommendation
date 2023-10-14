import pickle
from pathlib import Path
import os 
import requests
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# files path
path=os.path.join(BASE_DIR,"files")

import bz2
import pickle

# Load the pickled and compressed data
with bz2.BZ2File(os.path.join(path,"compressed.pbz2"), 'rb') as f:
    simalrity = pickle.load(f)

# with open(os.path.join(path,"similarity.pkl"),"rb") as file:
#         simalrity=pickle.load(file)



# url = "https://api.themoviedb.org/3/movie/192?api_key=56ab8834b086acdfa1e62f54db39608c"

def recommandor(name,df):
    path_of_fetchimages=[]
    recommandmovie=[]
    movieindex=df[df['title']==name].index[0]
    # print(movieindex)
    
    movie_to_recommand=sorted(list(enumerate(simalrity[movieindex])),key=lambda x:x[1],reverse=True)[1:7]
    # print(movie_to_recommand)
    
    # taking the poster path
    for i in movie_to_recommand:
        recommandmovie.append(df['title'][i[0]])
        
        url = f"https://api.themoviedb.org/3/movie/{df['id'][i[0]]}?api_key=56ab8834b086acdfa1e62f54db39608c"
        response=requests.get(url=url)
        response=response.json()
        # print(response['poster_path'])
        # print(df["id"][i[0]])
        image_path="http://image.tmdb.org/t/p/w500/"+response['poster_path']
        path_of_fetchimages.append(image_path)
        # print(image_path)
        
        
    
    
    

    
    
    return recommandmovie,path_of_fetchimages
    
    
    
    
    
    
    
    
   