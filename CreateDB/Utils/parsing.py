import re
from PyPDF2 import PdfReader


# FIXME: update this to have future years
def get_semester_and_year(text, valid_semesters=["SPRING", "FALL", "SUMMER"], valid_years=["2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025"]):
    if not isinstance(text, list) and not isinstance(text, str):
        raise TypeError(
            "Text passed to get semester and year must be a list or a string")
    num_of_valid_semesters = 0
    num_of_valid_years = 0
    beginning_of_pdf_text = text[0:30]
    for valid_semester in valid_semesters:
        if valid_semester in beginning_of_pdf_text:
            num_of_valid_semesters += 1
            semester = valid_semester
    if num_of_valid_semesters == 0:
        print("No valid semester found in parsed text!")
    elif num_of_valid_semesters > 1:
        print("More than one valid semester found in parsed text!")
    for valid_year in valid_years:
        if valid_year in beginning_of_pdf_text:
            num_of_valid_years += 1
            year = valid_year
    if num_of_valid_years == 0:
        print("No valid year found in parsed text!")
    elif num_of_valid_years > 1:
        print("More than one valid year found in parsed text!")
    return semester, year


def is_section_tag(section_tag):
    from Utils.constants import SECTION_PATTERN
    return re.match(SECTION_PATTERN, section_tag)


def valid_section_tag(section_tag):
    if not isinstance(section_tag, str):
        raise TypeError("Section tag must be a string")
        return False
    if not is_section_tag(section_tag):
        print("Section tag did not match the pattern")
        return False
    return True


def parse_section_tag(section_tag):
    if not valid_section_tag(section_tag):
        return
    if (section_tag[4] == '-'):
        department = section_tag[0:4].upper()
        course = section_tag[5:8]
        section = section_tag[9:12]
    else:  # School of Law Exception
        department = section_tag[0:3].upper()
        course = section_tag[4:7]
        section = section_tag[8:11]
    return department, course, section


def get_professor_entry(text_list, section_tag_index, counter=18, in_loop_first_time=True):
    if not valid_section_tag(text_list[section_tag_index]):
        return
    professor = text_list[section_tag_index + counter]
    loop_exit_condition = 0
    while (loop_exit_condition <= 50):
        counter += 1
        text = text_list[section_tag_index + counter]
        # FIXME: section breakpoints function?
        if is_section_tag(text) or text == "COURSE" or text == "SECTION":
            break
        else:
            professor = professor + " " + text
        loop_exit_condition += 1
    return professor


def get_section_grades_list(section_tag_index, pdf_text):
    A = int(pdf_text[section_tag_index+1])
    B = int(pdf_text[section_tag_index+3])
    C = int(pdf_text[section_tag_index+5])
    D = int(pdf_text[section_tag_index+7])
    F = int(pdf_text[section_tag_index+9])
    I = int(pdf_text[section_tag_index+12])
    S = int(pdf_text[section_tag_index+13])
    U = int(pdf_text[section_tag_index+14])
    X = int(pdf_text[section_tag_index+15])
    Q = int(pdf_text[section_tag_index+16])
    grades = [A, B, C, D, F, I, S, U, X, Q]
    return grades


def get_section_tag_indices_and_retain_pdf_text(grade_file):
    reader = PdfReader(grade_file)
    pdf_text = []
    section_tag_indices = []
    for page_number in range(len(reader.pages)):
        page = reader.pages[page_number]
        text = page.extract_text().split()
        pdf_text.extend(text)
    for i, text in enumerate(pdf_text):
        if is_section_tag(text):
            section_tag_indices.append(i)
    return section_tag_indices, pdf_text


def populate_section_info(section_tag_indices, pdf_text, semester, year, section_documents_list):
    for i, section_tag_index in enumerate(section_tag_indices):
        section_tag = pdf_text[section_tag_index]
        department, course, section = parse_section_tag(section_tag)
        grades = get_section_grades_list(section_tag_index, pdf_text)
        professor = get_professor_entry(pdf_text, section_tag_index)
        # FIXME: Galveston and Qatar section id collisions fixed by appending GV and QT, need to automate this
        section_id = department + course + section + semester + year
        section_documents_list.append(
            {
                '_id': section_id,
                "Department": department,
                "Course": course,
                "Semester": semester,
                "Year": year,
                "Section": section,
                "Professor": professor,
                "Grades": grades
            }
        )
    return section_documents_list
