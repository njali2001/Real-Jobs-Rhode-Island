from django.db import models

# Create your models here.
class Sector_Partnerships(models.Model):
	partnership_title = models.CharField(max_length=200)
	target_industry = models.CharField(max_length=100)
	lead_applicant_organization = models.CharField(max_length=200)
	organization_link = models.URLField(max_length=200,null=True,blank=True)
	contact_name = models.CharField(max_length=100)
	comprehensive_plan = models.CharField(max_length=200)
	plan_link = models.URLField(max_length=200,null=True,blank=True)

class Employers_Served(models.Model):
	employer = models.CharField(max_length=100)
	new_hire_training = models.CharField(max_length=10,null=True,blank=True)
	incumbent_worker_training = models.CharField(max_length=10,null=True,blank=True)
	partnerships = models.CharField(max_length=100)

class Industry_Sectors(models.Model):
	partnership = models.CharField(max_length=100)

class New_Hire_Training_Activities(models.Model):
	partnership = models.CharField(max_length=100)
	description_of_training_activities = models.TextField()

class Incumbent_Worker_Training_Activities(models.Model):
	partnership = models.CharField(max_length=100)
	description_of_training_activities = models.TextField()

class Pipeline_Development_Activities(models.Model):
	partnership = models.CharField(max_length=100)

class New_Hires_Placed(models.Model):
	partnership = models.CharField(max_length=100)
	new_hires_placed = models.IntegerField()

class Incumbent_Workers_Upskilled(models.Model):
	partnership = models.CharField(max_length=100)
	incumbent_workers_upskilled = models.IntegerField()

class College_Internships_Completed(models.Model):
	partnership = models.CharField(max_length=100)
	activity_description = models.TextField()
	college_internships_completed = models.IntegerField(null=True, default=0)

class New_Career_Technial_High_School_Programs(models.Model):
	partnership = models.CharField(max_length=100)
	CTE_progam_description = models.TextField()

class High_School_Students_Completing_Internships(models.Model):
	partnership = models.CharField(max_length=100)
	activity_description = models.TextField()
	high_school_internships_completed = models.IntegerField()

class Performance_Finances(models.Model):
	placement_rate = models.CharField(max_length=10)
	avreage_wage_after_placement = models.CharField(max_length=10)
	avreage_wage_gain = models.CharField(max_length=10)
	cost_per_individual = models.CharField(max_length=10)
	benchmark_cost = models.CharField(max_length=10)
