from brownie import Grades, accounts


def test_deploy():
    account = accounts[0]
    grades = Grades.deploy({"from": account})
    grades.evaluate("778899", 9, {"from": account})
    student_grade = grades.viewGrades("778899")
    print(student_grade)
    assert student_grade == 9


def test_reviews():
    account = accounts[0]
    grades = Grades.deploy({"from": account})
    grades.evaluate("778899", 9, {"from": account})

    grades.askForReview("778899")
    reviews = grades.SeeReviews()
    print(reviews)
    assert reviews != None
