from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

# from django.template import loader
from .models import Sector_Partnerships,Employers_Served,Industry_Sectors,New_Hire_Training_Activities,Incumbent_Worker_Training_Activities,Pipeline_Development_Activities,New_Hires_Placed,Incumbent_Workers_Upskilled,College_Internships_Completed,New_Career_Technial_High_School_Programs,High_School_Students_Completing_Internships,Performance_Finances

# from .forms import UploadFileForm 	# To be deleted

from django.urls import reverse

import openpyxl		# used for import xlsx file

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
        object_type[section].objects.all().delete()			# delete existing data, if switch to append, this line can be removed
        excel_file = request.FILES["csv_file"]
        wb = openpyxl.load_workbook(excel_file)

        if not excel_file.name.endswith('.xlsx'):			# Valid the suffix of file
            messages.error(request,'File is not xlsx type')
            return HttpResponseRedirect(reverse("web:upload_csv"))
        
        worksheet = wb.active
        message = str(excel_file) +  ' has been uploaded'
        
        row_ind = 0											# row_ind used for skip the header line in the file
        for row in worksheet.iter_rows():
	        if row_ind > 0:
	        	table = object_type[section]()
	        	columns = [f.name for f in table._meta.get_fields()[1:]]	# Read the filed name dynamically
	        	if row[0].value != '':
	        		ind = 0
	        		for column in columns:
	        			setattr(table,column,row[ind].value) 				# assign the value to the attribute
	        			ind += 1
	        		table.save()
	        row_ind += 1


############################################################
#
#	Working with CSV File, if the filed contains comma, the 
#	result will incorrect
#
############################################################

#		 section = request.POST['section']
#        csv_file = request.FILES["csv_file"]
#        message = csv_file.name + ' has been uploaded'

#        if not csv_file.name.endswith('.csv'):
#            messages.error(request,'File is not CSV type')
#            return HttpResponseRedirect(reverse("web:upload_csv"))
        
#        file_data = csv_file.read().decode("utf-8")        
#        lines = file_data.split("\n")

#        message = str(len(lines)-2) + ' records have been uploaded'

#        object_type[section].objects.all().delete()

        #loop over the lines and save them in db. If error , store as string and then display
#        for line in lines[1:]:    
#            fields = line.split(",")
#            table = object_type[section]()
#            columns = [f.name for f in table._meta.get_fields()[1:]]

#            if fields[0] != '':
#            	ind = 0
#            	for column in columns:
#            		setattr(table,column,fields[ind]) 
#            		ind += 1
            	
#            	table.save()

    except Exception as e:
    	message = "System Error: " + repr(e)
    	pass
 
    context = {'message':message}		# return the process result

    return render(request,'web/upload_csv.html',context)


def index(request):

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
