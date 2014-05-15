sample = (4569,4517,4523,4535,4539,4545,4547,4549,4563,4565,4567)
PlatformSmokeTest = ['1086', '215', '212', '1235', '194', '197', '191', '218', '1088', '1084', '3299', '3295', '176', '772', '3297', '173', '170', '1424', '1428', '699', '182', '209', '1038', '221', '188', '814', '1103', '200', '203', '1237', '1091', '206', '465', '467', '1130', '461', '463', '108', '73', '70', '79', '906', '781', '1461', '1863', '35', '1456', '1451', '1009']
iOS5PortTestPlan = ['4672', '4664', '4660', '4609', '4668', '4531', '4633', '4571', '4631', '4573', '4637', '4575', '4635', '4348', '4611', '4579', '4613', '4670', '4615', '4543', '4617', '4551', '4519', '4539', '4678', '4535', '4537', '4517', '4533', '4593', '4591', '4597', '4595', '4639', '4599', '4652', '4563', '4561', '4623', '4567', '4625', '4565', '4627', '4541', '4629', '4569', '4350', '4603', '4547', '4601', '4577', '4549', '4649', '4545', '4529', '4654', '4527', '4643', '4666', '4641', '4523', '4647', '4662', '4645', '4658', '4674', '4656', '4589', '4676', '4585', '4587', '4581', '4583']


import TestLinkAPI
TL = TestLinkAPI.TestlinkAPIClient("http://qa.incenergy.com/testlink/lib/api/xmlrpc.php", "2f3832a3642ca031a15ae72413e900e5")

entry = []
def GetList():
    return sample

def GetCases(planid):
    Cases = TL.getTestCasesForTestPlan(planid)
    return Cases

def GetPlatforms(planid):
    Platforms = TL.getTestPlanPlatforms(planid)
    return Platforms

def GetProjects():
    Projects = TL.getProjects()
    return Projects

def GetTestPlans(projectid):
    TestPlans = TL.getProjectTestPlans(projectid)
    return TestPlans

def UpdateResult(caseid, planid, status, platform):
    update = TL.reportTCResult(caseid, planid, status, platform)
    return update



