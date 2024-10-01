#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    approved_jobs = [
        "Admin", "Customer Service", "Human Resources", "ITC", "Production",
        "Legal", "Finance", "Sales", "General Management", "Research & Development", "Marketing", "Purchasing"
    ]

    def _init_(self, name:str = "Unknown", job: str = "Unknown"):
        self.name = name
        self.job = job

    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, value:str):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self.name = value.title()
        else:
            print("Name must be a string between 1 and 25 characters.")

    @property
    def job(self):
        return self._job
    
    @job.setter
    def job(self, value:str):
        if value in self.approved_jobs:
            self.job = value
        else:
            print("Job must be in list of approved jobs.")
