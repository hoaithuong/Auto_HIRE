from Login import login
from Location import createlocation
from InviteUser import inviteuser
from Job import createjob
from Talent import createtalent
from Task import createtask
from Event import createevent
from Workflow import createworkflow
from InterviewForm import createinterview
from EmailTemplate import createtemplate
from ApplicantQuestionnaire import createquestionnaires
from EvaluationCriteria import updateevaluation
from Category import createcategory

def main():
    login()
    # createlocation()
    # inviteuser()
    # createjob()
    # createtalent()
    # createtask()
    # createevent()
    # createworkflow()
    # createinterview()
    # createtemplate()
    # createquestionnaires()
    # updateevaluation()
    createcategory()


main()
