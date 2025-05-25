class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_info(self):
        print(f"User Name: {self.name}")
        print(f"Email: {self.email}")

class Instructor(User):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject

    def upload_content(self, content_title):
        print(f"Instructor {self.name} uploaded content: {content_title}")

    def display_info(self):
        super().display_info()
        print(f"Subject Expertise: {self.subject}")

class CourseCreator(Instructor):
    def __init__(self, name, email, subject):
        super().__init__(name, email, subject)
        self.courses = {}

    def create_course(self, course_name, modules):
        self.courses[course_name] = modules
        print(f"Course '{course_name}' created with modules: {', '.join(modules)}")

    def display_info(self):
        super().display_info()
        print("Role: Course Creator")
        print(f"Courses Created: {', '.join(self.courses.keys()) if self.courses else 'None'}")
creator = CourseCreator("Dr. Smith", "smith@example.com", "Data Science")
creator.display_info()
creator.upload_content("Introduction to Python")
creator.create_course("Python Basics", ["Syntax", "Variables", "Loops"])
creator.display_info()