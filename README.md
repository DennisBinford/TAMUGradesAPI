The API to get any section, specific course, or specific professor from MongoDB Atlas of all TAMU courses from the Office of the Registrar PDFs except for professional colleges (work in progress)
Below are all the api routes followed by a colon followed by a description of the route
/ : gets all 94,082 entries inside the MongoDB database
/AERO : example gets AERO department, this works off of regular expression so AE would get AERO and BAEN and any other departments that have AE together
/AERO/201 : example gets all AERO 201 course sections, this works off of regular expression on both parameters as well
/professor/PROFESSORNAME : professor is required to then ask for a regular expression of a professor's name
