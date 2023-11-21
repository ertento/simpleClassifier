from irisclassifier import IrisClassifier

i = IrisClassifier()
i.ingestion()
i.segregation()
i.train()
print(i.evaluation())
