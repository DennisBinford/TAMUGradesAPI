import os
import glob
import time

from Utils.constants import SECTION_PATTERN, MONGODB_URI, DATABASE_NAME, PROCESS_FILE_PATH, SAVE_FILE_PATH, FAIL_FILE_PATH, START_TIME
from Utils.pymongo import get_mongodb_collection
from Utils.parsing import *

if __name__ == "__main__":

    collection = get_mongodb_collection(
        "TAMUGrades", "AllSectionsTest", MONGODB_URI)
    grade_pdfs = glob.glob(os.path.join(PROCESS_FILE_PATH, '*.pdf'))
    section_documents_list = []
    file_count = 0
    skip_file = False

    # FIXME: Create the hash system for files

    for grade_pdf in grade_pdfs:
        print(time.time() - START_TIME)
        file_count += 1
        print(file_count, ":", grade_pdf)
        section_tag_indices, pdf_text = get_section_tag_indices_and_retain_pdf_text(
            grade_pdf)
        semester, year = get_semester_and_year(pdf_text)
        section_documents_list = populate_section_info(section_tag_indices, pdf_text,
                                                       semester, year, section_documents_list)
    try:
        print(time.time() - START_TIME)
        collection.insert_many(section_documents_list)
        section_documents_list = []
        print("Mass wrote successfully")
        for grade_pdf in grade_pdfs:
            os.replace(grade_pdf, SAVE_FILE_PATH + grade_pdf[-14:-1] + 'f')
    except Exception as e:
        print(e)
        print("ALERT: collection entry having problems")

# FIXME: Galveston (GV) and Qatar (QT) have duplicate keys as they use the same number for sections
# School of Law has an exception as it is LAW which violates section pattern
