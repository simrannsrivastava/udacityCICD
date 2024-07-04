import time
from locust import HttpUser, task, between
 
class WebsiteTestUser(HttpUser):
   host = 'https://flask-ml-service.azurewebsites.net/'
   wait_time = between(0.5, 3.0)
   
   @task
   def get_html(self): 
      self.client.get("/") 
      
   @task
   def post_prediction(self):
     self.client.post("/predict")
