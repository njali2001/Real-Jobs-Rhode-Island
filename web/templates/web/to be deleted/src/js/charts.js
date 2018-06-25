(function(){

	Highcharts.setOptions({
			lang: {
					thousandsSep: ','
			},
			backgroundColor: 'rgba(255, 255, 255, 0)',
			colors: ['#507EBE', '#D48F1E', '#7D0010', '#63A51A', '#570B9A', '#D6C818']
	});


	Highcharts.chart('gender', {
		chart: {type: 'bar'},
		credits: {enabled: false},
		exporting: {enabled: false},
		title: {text: 'Gender'},
		plotOptions: {
			bar: {
				animation: false,
				stacking: 'percent', 
				dataLabels: {
					enabled: true,
					format: '<b>{point.name}</b><br>{point.percentage:.1f} %',
					style: {textOutline: 'none'},
				}
			}
		},	
		series: [{
			name: 'Male',
			data: [1128, 503635],
			index: 1
		}, {
			name: 'Female',
			data: [652, 544684], 
			index: 2
		}],
		xAxis: {
			categories: ['RJRI New Hires', '2015 RI Census'],
		}, 
		yAxis: {
			labels: {enabled: false},
			reversedStacks: false,
			title: {enabled: false}
		}
	});


	Highcharts.chart('education', {
		chart: {type: 'bar'},
		credits: {enabled: false},
		exporting: {enabled: false},
		title: {text: 'Education Level'},
			plotOptions: {
			bar: {
				animation: false,
				stacking: 'percent', 
				dataLabels: {
					enabled: true,
					format: '<b>{point.name}</b><br>{point.percentage:.1f} %',
					style: {textOutline: 'none'},
				}
			}
		},	
		series: [{
			name: 'Less than HS Diploma',
			data: [210, 99747],
			index: 1
		},{
			name: 'High School Diploma or Equivalency',
			data: [676, 196988],
			index: 2
		},{
			name: 'Some college, no degree',
			data: [359, 133029],
			index: 3
		},{
			name: 'Associates Degree',
			data: [110, 61060],
			index: 4
		},{
			name: 'Bachelors Degree or Higher',
			data: [286, 137505],
			index: 5
		},{
			name: 'Vocational College or Other',
			data: [94],
			index: 6
		}],
		xAxis: {categories: ['RJRI New Hires', '2014 RI Census']}, 
		yAxis: {
			labels: {enabled: false},
			reversedStacks: false,
			title: {enabled: false}
		}
	});

	Highcharts.chart('ethnicity', {
		chart: {type: 'bar'},
		credits: {enabled: false},
		exporting: {enabled: false},
		title: {text: 'Race/Ethnicity'},
			plotOptions: {
			bar: {
				animation: false,
				stacking: 'percent', 
				dataLabels: {
					enabled: true,
					format: '<b>{point.name}</b><br>{point.percentage:.1f} %',
					style: {textOutline: 'none'},
				}
			}
		},	
		series: [{
			name: 'White',
			data: [1044, 856869],
			index: 1
		},{
			name: 'African American',
			data: [263, 60189],
			index: 2
		},{
			name: 'Latino (any race)',
			data: [304, 130655],
			index: 3
		},{
			name: 'American Indian/Alaskan Native',
			data: [19, 6058],
			index: 4
		},{
			name: 'Asian',
			data: [67, 30457],
			index: 5
		},{
			name: 'Hawaiian/Pacific Islander',
			data: [5,0.1],
			index: 6
		},{
			name: 'Two or More Races',
			data: [54, 34787],
			index: 7
		},{
			name: 'Did Not Disclose',
			data: [327],
			index: 8,
			visible: false
		}],
		xAxis: {categories: ['RJRI New Hires', '2015 RI Census']}, 
		yAxis: {
			labels: {enabled: false},
			reversedStacks: false,
			title: {enabled: false}
		}
	});

})();
