import time

SECTION_PATTERN = r"([A-Z]{4}-\d{3}-.{1}\d{2})|([A-Z]{3}-\d{3}-.{1}\d{2})"
MONGODB_URI = "mongodb+srv://<Enter User>:<Enter Password>@cluster0.7tlekcd.mongodb.net/?retryWrites=true&w=majority"
DATABASE_NAME = "TAMUGrades"
PROCESS_FILE_PATH = 'GradePDFs/Process/'
SAVE_FILE_PATH = 'GradePDFs/Saved/'
FAIL_FILE_PATH = 'GradePDFs/Failed/'
START_TIME = time.time()
