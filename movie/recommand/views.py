from django.shortcuts import render
import os
from pathlib import Path
import pickle
from .utills import recommandor



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# files path
path=os.path.join(BASE_DIR,"files")




def movierecommandor(request):
    # loading the pickle file
    
    movie_name=[]
    movie_image=[]
    with open(os.path.join(path,"finaldf.pkl"),"rb") as df:
        df=pickle.load(df)
    
    title=df.title.unique()
    # print(title)
   
            
    
    if request.method=="POST":
        name=request.POST['moviename']
        movie_name,movie_image=recommandor(name,df)
        # print(movie_name)
        
        
        
        
        
    
    return render(request,"movie.html",{"title":title,"movie":zip(movie_name,movie_image)})
    
    
    


