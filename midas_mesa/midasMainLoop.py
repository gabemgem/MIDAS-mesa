import mesa 
import readParameters
import buildWorld
import numpy as np

class MidasModel(mesa.Model):
    def __init__(self, inputs, runName):
        # Mesa scheduler will control the activation of individual agents
        self.schedule = mesa.time.RandomActivation(self)

        self.agentParameters, self.modelParameters, self.networkParameters, self.mapParameters = readParameters(inputs)
        self.agentList, self.aliveList, self.modelParameters, self.agentParameters, self.mapParameters, self.utilityVariables, self.mapVariables, self.demographicVariables, self.agentLocations = buildWorld(self.modelParameters, self.mapParameters, self.agentParameters, self.networkParameters, self, self.schedule)

        self.numLocations = len(self.mapVariables.locations)
        self.numLayers = len(self.utilityVariables.utilityLayerFunctions)
        self.sizeArray = len(self.utilityVariables.utilityHistory)

        self.outputs = {
            'countAgentsPerLayer': np.zeros((self.numLocations, self.numLayers, self.modelParameters['timeSteps'])),
            'averageExpectedOpening': np.zeros((self.numLocations, self.numLayers, self.modelParameters['timeSteps'])),
            'averageWealth': np.zeros((self.modelParameters['timeSteps'])),
            'migrations': np.zeros((self.modelParameters['timeSteps'])),
            'outMigrations': np.zeros((self.numLocations, self.modelParameters['timeSteps'])),
            'inMigrations': np.zeros((self.numLocations, self.modelParameters['timeSteps'])),
            'migrationMatrix': np.zeros(self.numLocations),
            'portfolioHistory': {},
            'trappedHistory': np.zeros((len(self.agentList), self.modelParameters['timeSteps']))
        }



# function [outputs] = midasMainLoop(inputs, runName)
# %runMigrationModel.m main time loop of migration model


# close all;

# tic;

# outputs = [];
# [agentParameters, modelParameters, networkParameters, mapParameters] = readParameters(inputs);

# [agentList, aliveList, modelParameters, agentParameters, mapParameters, utilityVariables, mapVariables, demographicVariables] = buildWorld(modelParameters, mapParameters, agentParameters, networkParameters);
    
# numLocations = size(mapVariables.locations,1);
# numLayers = size(utilityVariables.utilityLayerFunctions,1);

# sizeArray = size(utilityVariables.utilityHistory);

# %create any other outcome variables of interest
# countAgentsPerLayer = zeros(numLocations, numLayers, modelParameters.timeSteps);
# averageExpectedOpening = countAgentsPerLayer;
# averageWealth = zeros(modelParameters.timeSteps ,1);
# migrations = zeros(modelParameters.timeSteps,1);
# outMigrations = zeros(numLocations, modelParameters.timeSteps);
# inMigrations = zeros(numLocations, modelParameters.timeSteps);
# migrationMatrix = zeros(numLocations);
# portfolioHistory = cell(numLocations, modelParameters.timeSteps);
# trappedHistory = zeros(length(agentList),modelParameters.timeSteps);
        
        self.agentLayers = np.zeros((len(self.agentList), len(self.utilityVariables['utilityLayerFunctions'])))

# %create a list of shared layers, for use in choosing new link
# agentLayers = zeros(length(agentList),size(utilityVariables.utilityLayerFunctions,1));
        ???? agentLayers(:) = vertcat(agentList.currentPortfolio);


        # Added agentLocations array output to build world because they should just be initialized at agent creation
# agentLocations = ones(1,length(agentList));
# agentLocations(aliveList) = [agentList(aliveList).matrixLocation];

        ####    This ends model initialization code adapted from MIDAS      ####
        ####    The remaining initialization code is for Mesa               ####
        
        # currently no Mesa initialization besides the scheduler and whatever is handled in the build world function

        
    def step(self):
        ''' Advance the model one step '''

        # update the social network links, cap any that are above 1 or below 0
        net = self.mapVariables['network']
        net[net > 1] = 1
        net = net - self.networkParameters['decayPerStep']
        net[net < 0] = 0

        # run each agent's step function
        self.schedule.step()
        indexT = self.schedule.steps



# for indexT = 1:modelParameters.timeSteps
    
#     %update the social network links ... cap any that swelled above 1 in
#     %the last loop, and allow all to decay to no less than 0
#     mapVariables.network(mapVariables.network ~= 0) = min(1,mapVariables.network(mapVariables.network ~= 0));
#     mapVariables.network(mapVariables.network ~= 0) = max(0,mapVariables.network(mapVariables.network ~= 0) - networkParameters.decayPerStep);
        
    # livingAgents = agentList(aliveList);
    # currentRandOrder = randperm(length(livingAgents));

                        # %update agent age, information and preferences, looping across agents
                        # for indexA = 1:length(currentRandOrder)
                            
                        #     currentAgent = livingAgents(currentRandOrder(indexA));
                            
                        #     %age the agent
                        #     currentAgent.age = currentAgent.age + modelParameters.cyclesPerTimeStep;
                            
                        #     %draw number to see if agent survives to this timestep
                        #     agentSurvives = rand() < interp1(demographicVariables.agePointsSurvival, demographicVariables.survivalRate(currentAgent.matrixLocation,:,currentAgent.gender), currentAgent.age);
                        #     if(~agentSurvives)

                        #         %don't delete the agent, because we get into a re-indexing
                        #         %nightmare.  just mark it dead, and force all network links to
                        #         %0
                        #         mapVariables.network(currentAgent.id, [currentAgent.network(:).id]) = 0;
                        #         mapVariables.network([currentAgent.network(:).id],currentAgent.id) = 0;
                        #         currentAgent.TOD = indexT;
                        #         aliveList(currentAgent.id) = false;
                        #         continue;
                        #     end
                            
                        #     %update any age-specific agent parameters
                    
                        #     %agent expectations on openings are all updated based on how old
                        #     %they are, with formula p = f(t) * A + (1 - f(t)) * B * rand(); f(t) =
                        #     %f_init * (1 - d) ^ t ... A is the best case expectation with new
                        #     %information, and B is the best case expectation in the absence of
                        #     %any information.  As information gets older, expectation shifts
                        #     %from based in A to mostly B
                        #     temp_f =  (1 - currentAgent.fDecay).^(indexT - currentAgent.timeProbOpeningUpdated);
                        #     currentAgent.expectedProbOpening = currentAgent.pGetLayer_informed * currentAgent.heardOpening .* temp_f + currentAgent.pGetLayer_uninformed * rand(size(temp_f)) .* (1 - temp_f);
                            
                            
                        #     %agent gets updated knowledge of any openings available in layers
                        #     %that it occupies
                        #     currentAgent.heardOpening(currentAgent.matrixLocation,currentAgent.currentPortfolio) = utilityVariables.hasOpenSlots(currentAgent.matrixLocation,currentAgent.currentPortfolio);
                        #     currentAgent.timeProbOpeningUpdated(currentAgent.matrixLocation,currentAgent.currentPortfolio) = indexT;
                    
                        #     %draw number to see if (for female agents) agent gives birth
                        #     if(currentAgent.gender == 2 && currentAgent.age >= modelParameters.ageDecision)
                        #         agentGivesBirth = rand() < interp1(demographicVariables.agePointsFertility, demographicVariables.fertilityRate(currentAgent.matrixLocation,:), currentAgent.age);
                        #         if(agentGivesBirth)
                        #             gender = 2 - (rand() > 0.5);  %let it be equally likely to be 1 or 2
                        #             age = 0;
                        #             %newBaby = initializeAgent(agentParameters, utilityVariables, age, gender, currentAgent.location, agentList(agentParameters.currentID));
                        #             newBaby = initializeAgent(agentParameters, utilityVariables, age, gender, currentAgent.location);
                        #             newBaby.id = agentParameters.currentID;
                        #             agentList(agentParameters.currentID) = newBaby;
                        #             agentParmameters.currentID = agentParameters.currentID + 1;
                        #             newBaby.matrixLocation = currentAgent.matrixLocation;
                        #             newBaby.DOB = indexT;
                        #             newBaby.moveHistory = [indexT currentAgent.matrixLocation currentAgent.visX currentAgent.visY];
                        #             newBaby.visX = currentAgent.visX;
                        #             newBaby.visY = currentAgent.visY;
                                    
                        #             newBaby.network = currentAgent;
                        #             newBaby.myIndexInNetwork(1) = length(currentAgent.network)+1;
                        #             currentAgent.network(end+1) = newBaby;
                        #             currentAgent.myIndexInNetwork(end+1) = 1;
                        #             currentAgent.lastIntendedShareIn(end+1) = 0;
                                    
                        #             newBaby = assignInitialLayers(newBaby, utilityVariables);
                                    
                        #             mapVariables.network(newBaby.id, currentAgent.id) = 1;
                        #             mapVariables.network(currentAgent.id, newBaby.id) = 1;
                        #             aliveList(newBaby.id) = true;
                                                    
                        #             %update this line in the array used to choose new links
                        #             agentLayers(newBaby.id,:) = newBaby.currentPortfolio;
                        #             agentLocations(newBaby.id) = newBaby.matrixLocation;
                                    
                        #         end
                        #     end
                            
                        #     %draw number to see if agent meets a new agent
                        #     if(rand() < currentAgent.pMeetNew)
                        #         %%the next bit of code sets up input to the application-specific
                        #         %%function that generates likelihoods for new links.  may need to be
                        #         %%adjusted depending on application
                                
                        #         %the REASON it isn't totally exported to an
                        #         %application-specific function is that passing the large
                        #         %network matrix around can be costly
                                
                        #         %create a list of 'shared weighted connections' with other agents;
                        #         connectionsWeight = mapVariables.network(currentAgent.id,1:length(agentList))*mapVariables.network(1:length(agentList), 1:length(agentList));
                        #         %connectionsWeight = mapVariables.network(currentAgent.id,[livingAgents.id])*mapVariables.network([livingAgents.id], [livingAgents.id]);
                                
                        #         %make a list of existing connections and dead agents, who
                        #         %should not have any weight in the calculations
                        #         currentConnections = mapVariables.network(currentAgent.id,:) > 0;
                        #         %currentConnections2 = mapVariables.network(currentAgent.id,:) > 0;
                        #         %currentConnections([agentList.TOD] > 0 | [agentList.DOB] < 0) = true;
                        #         %currentConnections2(~aliveList) = true;
                                
                            
                        #         currentConnections(currentAgent.id) = true;
                                
                        #         %create a list of distances to other agents, based on their location
                        #         distanceWeight = mapVariables.distanceMatrix(currentAgent.matrixLocation,agentLocations);

                                
                        #         %create a list of shared layers (in same location) using
                        #         %agentLayers            
                        #         sameLocation = agentLocations == currentAgent.matrixLocation;
                        #         layerWeight = sparse(ones(sum(sameLocation),1),find(sameLocation), currentAgent.currentPortfolio * agentLayers(sameLocation,:)', 1, length(agentList));

                        #         %identify the new network link using the appropriate function for this
                        #         %simulation
                        #         newAgentConnection = chooseNewLink(networkParameters, connectionsWeight, distanceWeight, layerWeight, currentConnections, aliveList);
                        #         connectedAgent = agentList((newAgentConnection));
                                
                        #         %now update all network parameters
                        #         strength = rand();
                        #         mapVariables.network(currentAgent.id, connectedAgent.id) = strength;
                        #         mapVariables.network(connectedAgent.id, currentAgent.id) = strength;
                                
                        #         currentAgentNetworkSize = length(currentAgent.network);
                        #         partnerAgentNetworkSize = length(connectedAgent.network);
                        #         currentAgent.myIndexInNetwork(currentAgentNetworkSize+1) = partnerAgentNetworkSize+1;
                        #         connectedAgent.myIndexInNetwork(partnerAgentNetworkSize+1) = currentAgentNetworkSize+1;
                        #         currentAgent.lastIntendedShareIn(end+1) = 0;
                        #         connectedAgent.lastIntendedShareIn(end+1) = 0;
                        #         currentAgent.network(end+1) = connectedAgent;
                        #         connectedAgent.network(end+1) = currentAgent;
                                
                        #     end
                            
                        #     %draw number to see if agent has social interaction with existing
                        #     %network
                        #     if(rand() < currentAgent.pInteract && currentAgent.age >= modelParameters.ageLearn)
                        #         if(~isempty(currentAgent.network))
                                    
                        #             %can't talk to dead people
                        #             potentialPartners = currentAgent.network([currentAgent.network.TOD] < 0);
                        #             if(~isempty(potentialPartners))
                        #                 %choose an agent in social network and exchange
                                        
                        #                 %have to name currentAgent and partner as outputs of the
                        #                 %function, otherwise MATLAB simply creates a copy of them
                        #                 %inside the function to do writing, and doesn't write to
                        #                 %the original
                        #                 partner = potentialPartners(randperm(length(potentialPartners),1));
                                        
                        #                 [currentAgent, partner] = interact(currentAgent, partner, indexT);
                                        
                                        
                                        
                        #                 currentAgent.knowsIncomeLocation = any(currentAgent.incomeLayersHistory,3);
                        #                 partner.knowsIncomeLocation = any(partner.incomeLayersHistory,3);
                                        
                        #                 mapVariables.network(currentAgent.id, partner.id) = mapVariables.network(currentAgent.id, partner.id) + networkParameters.interactBump;
                        #                 mapVariables.network(partner.id, currentAgent.id) = mapVariables.network(partner.id, currentAgent.id) + networkParameters.interactBump;
                        #             end
                        #         end
                        #     end
                            
                        #     %draw number to see if agent learns anything randomly new about
                        #     %income in the world around it
                        #     if(rand() < currentAgent.pRandomLearn && currentAgent.age >= modelParameters.ageLearn)
                        #         currentAgent.incomeLayersHistory(randperm(prod([sizeArray(1:2) indexT]),currentAgent.countRandomLearn)) = true;
                        #         temp = randperm(prod(size(utilityVariables.hasOpenSlots)), currentAgent.countRandomLearn);
                        #         currentAgent.heardOpening(temp) = utilityVariables.hasOpenSlots(temp);
                        #         currentAgent.timeProbOpeningUpdated(temp) = indexT;
                        #     end
                        #     clear temp;
                            

                        #     %draw number to see if agent updates preferences on where to
                        #     %be/what to do
                        #     if(rand() < currentAgent.pChoose && indexT > modelParameters.spinupTime && currentAgent.age >= modelParameters.ageDecision)
                        #         [currentAgent, moved] = choosePortfolio(currentAgent, utilityVariables, indexT, modelParameters, mapParameters, demographicVariables, mapVariables);
                                
                                
                        #         if(~isempty(moved))
                        #             migrations(indexT) = migrations(indexT) + 1;
                        #             inMigrations(moved(2), indexT) = inMigrations(moved(2), indexT) + 1;
                        #             outMigrations(moved(1), indexT) = outMigrations(moved(1), indexT) + 1;
                        #             migrationMatrix(moved(1),moved(2)) = migrationMatrix(moved(1),moved(2)) + 1;
                        #             currentAgent.moveHistory = [currentAgent.moveHistory; indexT currentAgent.matrixLocation currentAgent.visX currentAgent.visY];
                        #         end
                                
                        #         %update these line in the arrays used to choose new links
                        #         agentLayers(currentAgent.id,:) = currentAgent.currentPortfolio;
                        #         agentLocations(currentAgent.id) = currentAgent.matrixLocation;
                        #     end
                        
                            
                        # end %for indexA = 1:currentRandOrder
        

        if indexT % self.modelParameters['incomeInterval'] == 0:
            # save counts of agents occupying each layer
            for agent in self.schedule.agents():
                currentPortfolio = agent.currentPortfolio
                self.outputs['countAgentsPerLayer'][agent.matrixLocation, currentPortfolio, indexT] += 1

            # add income layer to history
            self.utilityVariables = updateHistory(self.utilityVariables, self.modelParameters, indexT, self.outputs['countAgentsPerLayer'])

            # TODO: figure out how to apply income functions
            # %income functions are of the form f(k,m,nExpected,n_actual, base)
            # % - note that this may change depending on the simulation - 
            # %be sure that whatever your income functions are, the cellfun input
            # %matches appropriately
            # %         for indexL = 1:numLayers
            # %             utilityVariables.utilityHistory(:,indexL, indexT) = arrayfun(utilityVariables.utilityLayerFunctions{indexL}, ...
            # %                 mapVariables.locations.locationX, ...
            # %                 mapVariables.locations.locationY, ...
            # %                 ones(numLocations,1)*indexT, ...
            # %                 countAgentsPerLayer(:,indexL, indexT), ...
            # %                 utilityVariables.utilityBaseLayers(:,indexL,indexT));
            # %         end

            # make payments and transfers as appropriate to all agents and update knowledge
            for agent in self.schedule.agents():
                location = agent.matrixLocation
                currentPortfolio = agent.currentPortfolio
                incomeForms = currentPortfolio[self.utilityVariables['incomeForms']]
                agentIncomeForms = incomeForms[currentPortfolio]
                newIncome = np.sum(self.utilityVariables['utilityHistory'][location,agentIncomeForms, indexT])
                newIncome += agent.currentSharedIn
                agent.currentSharedIn = 0
                agent.personalIncomeHistory[indexT] = newIncome

                agent.incomeLayersHistory[location, currentPortfolio, indexT] = True
                agent.knowsIncomeLocation[location, currentPortfolio] = True

                # TODO: Not entirely sure what how this should work in python, but it's used in a couple of places
                agentNetwork = agent.network[:]

                # estimate the gross intention of sharing out across network
                amountToShare = newIncome * agent.incomeShareFraction
                networkStrengths = self.mapVariables['network'][agent.id, [agentNetwork.id]]

                potentialAmounts = (networkStrengths / np.sum(networkStrengths)) * amountToShare

                # calculate costs associated with those shares
                remittanceFee = self.mapVariables['remittanceFee'][location, [agentNetwork.matrixLocation]]
                remittanceRate = self.mapVariables['remittanceRate'][location, [agentNetwork.matrixLocation]]
                remittanceCost = (remittanceFee + remittanceRate / 100) * potentialAmounts

                # discard any potential transfers that exceed agent's threshold for
                # costs (i.e. agent stops making transfers if the transaction costs 
                # are too much of the overall cost)
                feasibleTransfers = remittanceCost . potentialAmounts < agent.shareCostThreshold
                actualAmounts = (potentialAmounts - remittanceCost) * feasibleTransfers
                actualPayments = potentialAmounts * feasibleTransfers

            
            
            

    
    
    if (mod(indexT, modelParameters.incomeInterval) == 0)
        
        # %construct the current counts of the number of agents occupying
        # %each layer
        # agentCityIndex = [livingAgents(:).matrixLocation]';
        # for indexA = 1:length(livingAgents)
        #     currentPortfolio = livingAgents(indexA).currentPortfolio;
        #     countAgentsPerLayer(agentCityIndex(indexA), currentPortfolio, indexT) = countAgentsPerLayer(agentCityIndex(indexA), currentPortfolio, indexT) + 1;
        # end
        
        # %add income layer to history
        # utilityVariables = updateHistory(utilityVariables, modelParameters, indexT, countAgentsPerLayer);
        
#         %income functions are of the form f(k,m,nExpected,n_actual, base)
#         % - note that this may change depending on the simulation - 
#         %be sure that whatever your income functions are, the cellfun input
#         %matches appropriately
# %         for indexL = 1:numLayers
# %             utilityVariables.utilityHistory(:,indexL, indexT) = arrayfun(utilityVariables.utilityLayerFunctions{indexL}, ...
# %                 mapVariables.locations.locationX, ...
# %                 mapVariables.locations.locationY, ...
# %                 ones(numLocations,1)*indexT, ...
# %                 countAgentsPerLayer(:,indexL, indexT), ...
# %                 utilityVariables.utilityBaseLayers(:,indexL,indexT));
# %         end
        
        # %make payments and transfers as appropriate to all agents, and
        # %update knowledge
        # for indexA = 1:length(livingAgents)
        #     currentAgent = livingAgents(indexA);
            
        #     %find out how much the current agent made, from each layer, and
        #     %update their knowledge

        #     newIncome = sum(utilityVariables.utilityHistory(currentAgent.matrixLocation,currentAgent.currentPortfolio(utilityVariables.incomeForms(currentAgent.currentPortfolio)), indexT));

            
        #     %add in any income that has been shared in to the agent, to
        #     %include in sharing-out decision-making
        #     newIncome = newIncome + currentAgent.currentSharedIn;
        #     currentAgent.currentSharedIn = 0;
        #     currentAgent.personalIncomeHistory(indexT) = newIncome;
            
            # currentAgent.incomeLayersHistory(currentAgent.matrixLocation,currentAgent.currentPortfolio,indexT) = true;
            # currentAgent.knowsIncomeLocation(currentAgent.matrixLocation, currentAgent.currentPortfolio) = true;
            
            
            # %estimate the gross intention of sharing out across network
            # amountToShare = newIncome * currentAgent.incomeShareFraction;
            # networkStrengths = mapVariables.network(currentAgent.id, [currentAgent.network(:).id]);

            # potentialAmounts = (networkStrengths ./ sum(networkStrengths)) * amountToShare;
            
            # %calculate costs associated with those shares
            # remittanceFee = mapVariables.remittanceFee(currentAgent.matrixLocation, [currentAgent.network(:).matrixLocation]);
            # remittanceRate = mapVariables.remittanceRate(currentAgent.matrixLocation, [currentAgent.network(:).matrixLocation]);
            # remittanceCost = remittanceFee + remittanceRate / 100 .* potentialAmounts;
            
            # %discard any potential transfers that exceed agent's threshold
            # %for costs (i.e., agent stops making transfers if the
            # %transaction costs are too much of the overall cost)
            # feasibleTransfers = remittanceCost ./ potentialAmounts < currentAgent.shareCostThreshold;
            # actualAmounts = (potentialAmounts - remittanceCost) .* feasibleTransfers;
            # actualPayments = potentialAmounts .* feasibleTransfers;
            
            %share across network and keep the rest
            for indexN = 1:size(currentAgent.network,2)
                currentConnection = currentAgent.network(indexN);
                try
                currentConnection.lastIntendedShareIn(currentAgent.myIndexInNetwork(indexN)) = potentialAmounts(indexN);
                catch
                    f=1;
                end
                if(actualAmounts(indexN) > 0)
                    
                    %income shared in is held separate until that agent
                    %comes around to their own income loop
                    currentConnection.currentSharedIn = currentConnection.currentSharedIn + actualAmounts(indexN);
                    
                    mapVariables.network(currentAgent.id, currentConnection.id) = mapVariables.network(currentAgent.id, currentConnection.id) + networkParameters.shareBump;
                    mapVariables.network(currentConnection.id, currentAgent.id) = mapVariables.network(currentConnection.id, currentAgent.id) + networkParameters.shareBump;
                    
                end
            end
            currentAgent.wealth = currentAgent.wealth + newIncome - sum(actualPayments);
        end
    end %if (mod(indexT, modelParameters.incomeInterval) == 0)
    
    %ANY ACTIONS NECESSARY FOR NEXT TIMESTEP, TO OCCUR AFTER INCOME UPDATED
    %update the system-wide record of whether a layer has open slots or not
    utilityVariables.hasOpenSlots = countAgentsPerLayer(:,:,indexT) < utilityVariables.nExpected & utilityVariables.hardSlotCountYN | ~utilityVariables.hardSlotCountYN;

    %update our time path of trapped agents
    trappedHistory([agentList(:).trapped] > 0,indexT) = 1;
   
    if (modelParameters.visualizeYN & mod(indexT, modelParameters.visualizeInterval) == 0)
        
        mapVariables.indexT = indexT;
        mapVariables.cycleLength = modelParameters.cycleLength;
        %visualize the map
        [mapHandle] = visualizeMap(livingAgents, mapVariables, mapParameters, modelParameters);
            set(gcf,'Position',mapParameters.position)
        drawnow();
        fprintf([runName ' - Map updated.\n']);
        if(modelParameters.saveImg)
           print('-dtiff','-painters','-r100', [mapParameters.saveDirectory modelParameters.shortName num2str(10000+indexT) '.tif']); 
           fprintf([runName ' - Map saved.\n']);                
        end

    end
    
%     averageWealth(indexT) = mean([livingAgents(:).wealth]);
%     temp = reshape(cell2mat({livingAgents.expectedProbOpening}), size(livingAgents(1).expectedProbOpening, 1), size(livingAgents(1).expectedProbOpening,2), length(livingAgents));
%     averageExpectedOpening(:,:,indexT) = mean(temp,3);
%     clear temp;

    %%%%
    %averageExpectedOpening(:,:,indexT) = 0;
    for indexI = 1:length(livingAgents)
        averageExpectedOpening(:,:,indexT) = averageExpectedOpening(:,:,indexT) + livingAgents(indexI).expectedProbOpening;        
    end
    averageExpectedOpening(:,:,indexT) = averageExpectedOpening(:,:,indexT) / indexI;
    %%%%
    
    if(modelParameters.listTimeStepYN)
        fprintf([runName ' - Time step ' num2str(indexT) ' of ' num2str(modelParameters.timeSteps) ' - ' num2str(migrations(indexT)) ' migrations.\n']);
    end

    
    %%update portfolioHistory
    for indexJ = 1:numLocations
       portfolioHistory{indexJ, indexT} = {(agentList([agentList.matrixLocation] == indexJ).currentPortfolio)};
    end
end %for indexT = 1:modelParameters.timeSteps

%prepare outputs
outputs.averageWealth = averageWealth;
outputs.countAgentsPerLayer = countAgentsPerLayer;
outputs.migrations = migrations;
outputs.locations = mapVariables.locations;
outputs.inMigrations = inMigrations;
outputs.outMigrations = outMigrations;
outputs.migrationMatrix = migrationMatrix;
outputs.averageExpectedOpening = averageExpectedOpening;
outputs.utilityHistory = utilityVariables.utilityHistory;
outputs.portfolioHistory = portfolioHistory;
outputs.trappedHistory = trappedHistory;

agentList = agentList(1:agentParameters.currentID-1);
agentSummary = table([agentList(:).id]','VariableNames',{'id'});
agentSummary.wealth = [agentList(:).wealth]';
agentSummary.location = [agentList(:).location]';
agentSummary.pInteract = [agentList(:).pInteract]';
agentSummary.pChoose = [agentList(:).pChoose]';
agentSummary.pRandomLearn = [agentList(:).pRandomLearn]';
agentSummary.countRandomLearn = [agentList(:).countRandomLearn]';
agentSummary.numBestLocation = [agentList(:).numBestLocation]';
agentSummary.numBestPortfolio = [agentList(:).numBestPortfolio]';
agentSummary.numRandomLocation = [agentList(:).numRandomLocation]';
agentSummary.numRandomPortfolio = [agentList(:).numRandomPortfolio]';
agentSummary.numPeriodsEvaluate = [agentList(:).numPeriodsEvaluate]';
agentSummary.numPeriodsMemory = [agentList(:).numPeriodsMemory]';
agentSummary.discountRate = [agentList(:).discountRate]';
agentSummary.rValue = [agentList(:).rValue]';
agentSummary.bList = [agentList(:).bList]';
agentSummary.TOD = [agentList(:).TOD]';
agentSummary.trapped = [agentList(:).trapped]';



tempCurrentPortfolio = cell(length(agentList),1);
tempFirstPortfolio = cell(length(agentList),1);
tempNetwork = cell(length(agentList),1);
tempMove = cell(length(agentList),1);
tempAccess = cell(length(agentList),1);
for indexI = 1:length(agentList)
    tempCurrentPortfolio{indexI} = agentList(indexI).currentPortfolio;
    tempFirstPortfolio{indexI} = agentList(indexI).firstPortfolio;
    try
    tempNetwork{indexI} = [agentList(indexI).network(:).id];
    catch
        f=1;
    end
    tempMove{indexI} = [agentList(indexI).moveHistory];
    tempAccess{indexI} = [agentList(indexI).accessCodesPaid];
end
agentSummary.currentPortfolio = tempCurrentPortfolio;
agentSummary.firstPortfolio = tempFirstPortfolio;
agentSummary.network = tempNetwork;
agentSummary.moveHistory = tempMove;
agentSummary.accessCodes = tempAccess;

outputs.agentSummary = agentSummary;

for indexI = length(agentList):-1:1
    delete(agentList(indexI));
end
clear agentList;
clear mapVariables;
clear utilityVariables;
clear *Parameters;
%pack;

fprintf([runName '- completed.\n']);

toc;
end

