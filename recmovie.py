import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFm

data=fetch_movielens(min_ratings=4.0)

print(repr(data['train']))
print(repr(data['test']))

model=LightFm(loss='warp') //waited approximate rank pairwise//
model.fit(data['train'],epochs=60,num_threads=2)


def sample_recommendations(model,data,user_ids):
 n_users,n_items=data['trains'].shape
  for user_id in user_ids:
      known_positives=data['items labels'][data['train'].tocsr()[user_id].indices
      
      scores=models.predict(user_id,np.arange(n_items))
      top_items=data['item labels'][np.argsort(-scores)]
      
      print("user %s" %user_id)
      print("      known positives:")
      
      for x in known_positives[:4]:
          print("      %s" %x)
       print("      recommend:")
      for x in top_items[:4]:
         print("     %s"%x)
  sample_recommendation(model,data,[12,43,234])

