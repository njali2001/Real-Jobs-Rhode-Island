from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

# from django.template import loader
from .models import Sector_Partnerships,Employers_Served,Industry_Sectors,New_Hire_Training_Activities,Incumbent_Worker_Training_Activities,Pipeline_Development_Activities,New_Hires_Placed,Incumbent_Workers_Upskilled,College_Internships_Completed,New_Career_Technial_High_School_Programs,High_School_Students_Completing_Internships,Performance_Finances

from .forms import UploadFileForm 

object_type = { 'Sector_Partnerships':Sector_Partnerships,
				'Employers_Served':Employers_Served,
				'Industry_Sectors':Industry_Sectors,

				'New_Hire_Training_Activities':New_Hire_Training_Activities,
				'Incumbent_Worker_Training_Activities':Incumbent_Worker_Training_Activities,
				'Pipeline_Development_Activities':Pipeline_Development_Activities,
					
				'New_Hires_Placed':New_Hires_Placed,
				'Incumbent_Workers_Upskilled':Incumbent_Workers_Upskilled,
				'College_Internships_Completed':College_Internships_Completed,
				'New_Career_Technial_High_School_Programs':New_Career_Technial_High_School_Programs,
				'High_School_Students_Completing_Internships':High_School_Students_Completing_Internships,
				'Performance_Finances':Performance_Finances}

def upload_csv(request):
    data = {}
    if "GET" == request.method:
        return render(request, "web/upload_csv.html", data)
    # if not GET, then proceed
    try:
        section = request.POST['section']
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            messages.error(request,'File is not CSV type')
            return HttpResponseRedirect(reverse("web:upload_csv"))
        
        file_data = csv_file.read().decode("utf-8")        
 
        lines = file_data.split("\n")

        object_type[section].objects.all().delete()

        #loop over the lines and save them in db. If error , store as string and then display
        for line in lines[1:]:                        
            fields = line.split(",")
            table = object_type[section]()
            columns = [f.name for f in table._meta.get_fields()[1:]]

            if fields[0] != '':
            	# for column in columns:
            		# table['column'] = fields[0]
            	# setattr(table,attr_type[columns[0]],fields[0])
            		# table.partnership = fields[0]

            	if section == 'Sector_Partnerships':
            		table.partnership_title = fields[0]
            		table.target_industry = fields[1]
            		table.lead_applicant_organization = fields[2]
            		table.organization_link = fields[3]
            		table.contact_name = fields[4]
            		table.comprehensive_plan = fields[5]
            		table.plan_link = fields[6]

            	elif section == 'Employers_Served':
            		table.employer = fields[0]
            		table.new_hire_training = fields[1]
            		table.incumbent_worker_training = fields[2]
            		table.partnerships = fields[3]

            	elif section == 'Industry_Sectors':
            		table.partnership = fields[0]

            	elif section == 'New_Hire_Training_Activities':
            		table.partnership = fields[0]
            		table.description_of_training_activities = fields[1]

            	elif section == 'Incumbent_Worker_Training_Activities':
            		table.partnership = fields[0]
            		table.description_of_training_activities = fields[1]

            	elif section == 'Pipeline_Development_Activities':
            		table.partnership = fields[0]

            	elif section == 'New_Hires_Placed':
            		table.partnership = fields[0]
            		table.new_hires_placed = fields[1]

            	elif section == 'Incumbent_Workers_Upskilled':
            		table.partnership = fields[0]
            		table.incumbent_workers_upskilled = fields[1]

            	elif section == 'College_Internships_Completed':
            		table.partnership = fields[0]
            		table.activity_description = fields[1]

            	elif section == 'New_Career_Technial_High_School_Programs':
            		table.partnership = fields[0]
            		table.CTE_progam_description = fields[1]

            	elif section == 'High_School_Students_Completing_Internships':
            		table.partnership = fields[0]
            		table.activity_description = fields[1]
            		table.high_school_internships_completed = fields[2]

            	elif section == 'Performance_Finances':
            		table.placement_rate = fields[0]
            		table.avreage_wage_after_placement = fields[1]
            		table.avreage_wage_gain = fields[2]
            		table.cost_per_individual = fields[3]
            		table.benchmark_cost = fields[4]

            	table.save()

    except Exception as e:
        pass
 
    

    context = {}

    return render(request,'web/upload_csv.html',context)
    

def upload_file(request):
	if request.method =='POST':
		form = UploadFileForm(request.POST, request.FILES)

		if forms.is_valid():

			return HttpResponseRedirect('/upload/')

	else:
		form = UploadFileForm()

	return render(request,'web/upload_csv.html',{'form':form})


def index(request):
#	template = loader.get_template('web/index.html')
#	context = {}
	# return HttpResponse("Hello, you're at the web index")
#	return HttpResponse(template.render(context,request))

	pf = Performance_Finances.objects.first()
	context = {	'Sector_Partnerships':Sector_Partnerships.objects.count(),
			  	'Employers_Served':Employers_Served.objects.count(),
			  	'Industry_Sectors':Industry_Sectors.objects.count(),
			  	
			  	'New_Hire_Training_Activities':New_Hire_Training_Activities.objects.count(),
			  	'Incumbent_Worker_Training_Activities':Incumbent_Worker_Training_Activities.objects.count(),
			  	'Pipeline_Development_Activities':Pipeline_Development_Activities.objects.count(),
			  	
			  	'New_Hires_Placed':New_Hires_Placed.objects.count(),
			  	'Incumbent_Workers_Upskilled':Incumbent_Workers_Upskilled.objects.count(),
			  	'College_Internships_Completed':College_Internships_Completed.objects.count(),
			  	'New_Career_Technial_High_School_Programs':New_Career_Technial_High_School_Programs.objects.count(),
			  	'High_School_Students_Completing_Internships':High_School_Students_Completing_Internships.objects.count(),

			  	'Placement_Rate': pf.placement_rate,
			  	'Avreage_Wage_After_Placement': pf.avreage_wage_after_placement,
			  	'Avreage_Wage_Gain': pf.avreage_wage_gain,
			  	'Cost_Per_Individual': pf.cost_per_individual,
			  	'Benchmark_Cost': pf.benchmark_cost,
			  	}
	return render(request,'web/index.html',context)
	
def page(request,section):

	model_name = section
	title = model_name.replace("_"," ")

	result = object_type[section].objects.all()
	fields = [f.name.replace("_"," ") for f in object_type[section]._meta.get_fields()[1:]]
	
	context = {'section':result, 'fields':fields,'model_name':model_name,'title':title}
	return render(request,'web/page.html',context)

def cal(request,id):
	response ="the number is %s"
	return HttpResponse(response % id)
