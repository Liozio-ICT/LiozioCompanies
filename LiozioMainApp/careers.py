from datetime import date
from random import randint

openings = [
    {
        "title" : "STARTUP LEADERSHIP PROGRAM OFFICER",
        "availabilty" : "open",
        "date_published" : date.today(),
        "excerpt" : "",
        "description" : "As the Startup Leadership Program Officer, you will be responsible for recruiting and supporting startup leaders in the SLP Program. You will manage the online platform, coordinate program resources, and facilitate both online and physical classes. You will also work closely with mentors, ensuring effective mentoring relationships, and oversee the smooth operation of the program. Additionally, you will handle program evaluation, stakeholder management, and ensure compliance with relevant standards, all while fostering a culture of innovation and continuous improvement.\nAbout You \nYou have experience in program management, leadership development, coordinating online platforms and experience in mentorship programs and in networking. You challenge the status quo with ideas and a get-it-done mindset. You bring solutions to the table after identifying problems. You are entrepreneurial, and you work like it's your own business. Essentially, you have a passion for people engagement and startups."
    },
    {
            "title" : "PARTNERSHIP AND SPECIAL PROGRAMS OFFICER",
            "availabilty" : "open",
            "date_published" : date.today(),
            "excerpt" : "",
            "description" : "As the Startup Leadership Program Officer, you will be responsible for recruiting and supporting startup leaders in the SLP Program. You will manage the online platform, coordinate program resources, and facilitate both online and physical classes. You will also work closely with mentors, ensuring effective mentoring relationships, and oversee the smooth operation of the program. \nAdditionally, you will handle program evaluation, stakeholder management, and ensure compliance with relevant standards, all while fostering a culture of innovation and continuous improvement.\nAbout You\nYou are a strategic thinker with strong communication skills, highly proficient in project management and very result oriented. You are also skilled in negotiation and enjoy building interpersonal relationships with people. You challenge the status quo with ideas and a get-it-done mindset. You bring solutions to the table after identifying problems. You are entrepreneurial, and you work like it's your own business. Essentially, you have a passion for people engagement and startups."
        },
        {
            "title" : "Executive Assistant to the CEO",
            "availabilty" : "open",
            "date_published" : date.today(),
            "excerpt" : "",
            "description" : ""
        },
        {
            "title" : "Farm Technician(Fishery)",
            "availabilty" : "open",
            "date_published" : date.today(),
            "excerpt" : "",
            "description" : ""
        }

]

def create_slug(list_item):
    refined_openings = []

    for item in list_item:
        image_no = randint(1, 4)
        slug = "-".join(item["title"].split(' ')).lower()
        if "(" in slug:
            new_slug = slug.split("(")
            new_slug.pop(1)
            slug = "".join(new_slug)
        refined_openings.append({
            "slug": slug,
            "availabilty" : item["availabilty"],
            "date_published" : item["date_published"],
            "excerpt" : item["excerpt"],
            "title": item["title"],
            "description": item["description"],
            "image" : f"img/career{image_no}.png",
            "url" : "https://forms.gle/NAQXYSbcPrG7oYFAA"
        })
    return refined_openings

openings = create_slug(openings)