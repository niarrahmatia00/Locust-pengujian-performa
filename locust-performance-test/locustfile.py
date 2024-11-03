from locust import HttpUser, task, between

class WikipediaUser (HttpUser):
    wait_time = between(5, 10) # wakru tunggu antar setiap permintaan 

    @task
    def access_wikipedia(self):
        self.client.get("/")