### Aggregate a Phd
Simple api/web app which will aggregate the results of several different Phd/job listing websites to help students/academics find positions. Initially this will be developed specifically for Physics but Potentially be expanded to cover a larger range of subjects in the future.

### Research
Sample of sites which will be used in the search API.
* [Jobs.ac.uk](http://jobs.ac.uk/phd)
    * [Physics](https://www.jobs.ac.uk/search/?keywords=&location=&placeId=&activeFacet=subDisciplineFacet&resetFacet=&sortOrder=1&pageSize=1000&startIndex=1&academicDisciplineFacet%5B0%5D=physical-and-environmental-sciences&subDisciplineFacet%5B0%5D=physics-and-astronomy&jobTypeFacet%5B0%5D=phds)
* [Find a Phd](http://findaphd.com/)
    * [Physics](https://www.findaphd.com/phds/united-kingdom/physics/?h0M7Wc10&Show=M)
    * Fitlered to only show latest PhDs
* [Research Gate](https://www.researchgate.net/jobs?regions=&page=1)
    * [Physics](https://www.researchgate.net/jobs/Physics-jobs)
* [Academic Position](https://academicpositions.com/find-jobs/)
    * [Physics](https://academicpositions.com/find-jobs?positions[0]=phd&fields[0]=physics&locations[0]=europe)
* [Euaxess](https://euraxess.ec.europa.eu/jobs/search)
    * [Physics](https://euraxess.ec.europa.eu/jobs/search/field_research_field/physics-344)
* [Postgraduate Studentships](https://www.postgraduatestudentships.co.uk/)
    * [Physics](https://www.postgraduatestudentships.co.uk/funding-opportunities/study/phd-other-doctoral-study-funding/applicant/all/organisation/all/subject/physics/region/all/pn/1/)

### Technology / Project Description
API will query these websites along with a query if the website allows it, otherwise the API will filter the results based on the chosen query (will try to obtain all from the category then filter). Then the API will return these to the API requester in a JSON format, each with a url to the post, title, location etc all the data that was available from the sites.

There will be a very simple Flask backend to act as the API with a single endpoint which will take a query parameter and then check all the sites, either by using their APIs if available or will scrape them using Requests and BeautifulSoup4. 

Frontend will be a very basic application, either in Vue or even just pure JavaScript and HTML/CSS. It only requires a few fields and then will make a request to the Flask server and display the results. Potentially allowwing the user to bookmark listing for later by storing them in local storage.

* Basic search input field to send request to API
* Display results in a readable format
* Filters and sorting for the results