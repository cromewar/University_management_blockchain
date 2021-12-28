from brownie import Grades, accounts


def test_deploy():
    account = accounts[0]
    grade = Grades.deploy({"from": account})
    student_hash = "Hg2d2442"
    student_grade = 9
    final_grade = grade.evaluate(student_hash, student_grade, {"from": account})
    assert final_grade == student_grade
