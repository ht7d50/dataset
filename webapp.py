from flask import Flask, request, render_template, flash
from markupsafe import Markup
from datetime import datetime

import os
import json

app = Flask(__name__)

@app.route('/')
def render_about():
    return render_template('graduationdata.html')

@app.route('/leveleducationmajor')
def render_leveleducationmajor():
    options = ""
    with open('graduates.json') as graduates_data:
        majors = json.load(graduates_data)
    
    
    
    
    if "major" in request.args:
        major = request.args['major']
        bachelors = 0
        doctorates = 0
        masters = 0
        professionals = 0
        for i in majors:
            if i["Education"]["Major"] == major:
                bachelors1 = i["Education"]["Degrees"]["Bachelors"]
                doctorates1 = i["Education"]["Degrees"]["Doctorates"]
                masters1 = i["Education"]["Degrees"]["Masters"]
                professionals1 = i["Education"]["Degrees"]["Professionals"]
        options = get_dropdown_options_majors()
        return render_template('leveleducationmajorresponse.html', options=options, bachelors = bachelors1, doctorates = doctorates1, masters = masters1, professionals = professionals1)
   
   
   
    options = get_dropdown_options_majors()
    
    return render_template('leveleducationmajor.html',options = options)
   
@app.route('/occupationstatus')
def render_occupation():
    with open('graduates.json') as graduates_data:
        occupations = json.load(graduates_data)
    options = get_dropdown_options_majors()
    if "occupation" in request.args:
        occupation = request.args['occupation']
        BusinessIndustry = 0
        EducationalInstitution = 0
        Government = 0
        for i in occupations:
            if i["Education"]["Major"] == occupation:
                BusinessIndustry1 = i["Employment"]["Employer Type"]["Business/Industry"]
                EducationalInstitution1 = i["Employment"]["Employer Type"]["Educational Institution"]
                Government1 = i["Employment"]["Employer Type"]["Government"]
        return render_template('occupationstatusresponse.html', options = options, BusinessIndustry=BusinessIndustry1, EducationalInstitution = EducationalInstitution1, Government = Government1)
    return render_template('occupationstatus.html', options = options)
   
@app.route('/salary')
def render_salary():
    with open('graduates.json') as graduates_data:
        salary = json.load(graduates_data)
    options = get_dropdown_options_majors()
    if "salary" in request.args:
        salaries = request.args['salary']
        Highest = 0
        Lowest = 0
        Mean = 0
        Median = 0
        Quantity = 0
        StandardDeviation = 0
        for i in salary:
            if i["Salaries"] == salaries:
                Highest = i["Salaries"]["Highest"]
                Lowest = i["Salaries"]["Lowest"]
                Mean = i["Salaries"]["Mean"]
                Median = i["Salaries"]["Median"]
                Quantity = i["Salaries"]["Quantity"]
                StandardDeviation = i["Salaries"]["Standard Deviation"]
        return render_template('salaryresponse.html', options = options, Highest = Highest, Lowest = Lowest, Mean = Mean, Median = Median, Quantity = Quantity, StandardDeviation = StandardDeviation)
    return render_template('salary.html', options = options)
   
def get_dropdown_options_majors():
    options = ""
    with open('graduates.json') as graduates_data:
        majors = json.load(graduates_data)
    for m in majors:
        options += Markup("<option value=\"" + m["Education"]["Major"]+ "\">" + m["Education"]["Major"] + "</option>")
    return options
   
   
def is_localhost():
    """ Determines if app is running on localhost or not
    Adapted from: https://stackoverflow.com/questions/17077863/how-to-see-if-a-flask-app-is-being-run-on-localhost
    """
    root_url = request.url_root
    developer_url = 'http://127.0.0.1:5000/'
    return root_url == developer_url


if __name__ == '__main__':
    app.run(debug=True)