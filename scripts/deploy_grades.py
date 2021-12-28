from brownie import Grades, accounts


def deploy_grades():
    account = accounts[0]
    grades = Grades.deploy({"from": account})


def main():
    deploy_grades()
