import mesa

class Agent(mesa.Agent):
    def __init__(self, id, location, model):
        super().__init__(id, model)

        self.location = location
        self.network = []
        self.TOD = -9999 # time of death
        self.DOB = -9999 # date of birth
        self.trapped = 0

        #agent properties
        self.matrixLocation = None
        self.visX = None
        self.visY = None
        self.wealth = None
        self.realizedUtility = None
        self.age = None
        self.gender = None
        
        #agent accumulated data
        self.network = None
        self.myIndexInNetwork = None
        self.accessCodesPaid = None
        self.bestPortfolios = None
        self.bestPortfolioValues = None
        self.knowsIncomeLocation = None
        self.incomeLayersHistory = None
        self.scratch = None
        self.overlap = None
        self.heardOpening = None
        self.expectedProbOpening = None
        self.timeProbOpeningUpdated = None
        self.percentIncomeLayersTest = None
        self.currentPortfolio = None
        self.firstPortfolio = None
        self.personalIncomeHistory = None
        self.currentSharedIn = None
        self.lastIntendedShareIn = None
        self.moveHistory = None
    
        #agent preferences
        self.incomeShareFraction = None
        self.shareCostThreshold = None
        self.knowledgeShareFrac = None
        self.pInteract = None
        self.pMeetNew = None
        self.pAddFitElement = None
        self.pChoose = None
        self.fDecay = None
        self.pGetLayer_informed = None
        self.pGetLayer_uninformed = None
        self.pRandomLearn = None
        self.countRandomLearn = None
        self.numBestLocation = None
        self.numBestPortfolio = None
        self.numRandomLocation = None
        self.numRandomPortfolio = None
        self.numPeriodsEvaluate = None
        self.numPeriodsMemory = None
        self.discountRate = None
        self.rValue = None
        self.bList = None
        self.prospectLoss = None