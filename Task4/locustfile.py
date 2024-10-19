from locust import HttpUser, task

class UnstableUser(HttpUser):
    @task
    def unstable(self):
        self.client.get("/unstable")

    @task
    def inverse(self):
        self.client.post("/inverse",json={"key1":"value1"})