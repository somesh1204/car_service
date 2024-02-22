import math
from typing import List, Any
from operator import itemgetter

from geopy.distance import distance

# Global Variables:-
STARTING_TIME = 5
INFINITY = 1000 * 1000 * 1000
VELOCITY = 1.5  # meter per sec.
TIME_REQUIRED_FOR_BASEMENT_CHANGE = 90  # meter per sec.
skipped_jobs = []
tenant_data = None

'''def getTimeRequired(t1, t2):
    # returns time required in seconds
    global tenant_data
    # print(tenant_data)
    # Distance = distance((location1['latitude'],location1['longitude']), (location2['latitude'],location2['longitude'])).m
    Distance = distance((tenant_data['tenantBlocks'][t1]['locationCoordinates']['latitude'], tenant_data['tenantBlocks'][t1]['locationCoordinates']['longitude']),(tenant_data['tenantBlocks'][t2]['locationCoordinates']['latitude'], tenant_data['tenantBlocks'][t2]['locationCoordinates']['longitude'])).m
    return Distance / VELOCITY
'''
def getTimeRequired(t1, b1, t2, b2):
    # returns time required in seconds
    global tenant_data
    # Calculate travel time between towers
    tower_travel_time = distance((tenant_data['tower_location'][t1]['latitude'], tenant_data['tower_location'][t1]['longitude']), (tenant_data['tower_location'][t2]['latitude'], tenant_data['tower_location'][t2]['longitude'])).m / VELOCITY
    # Calculate travel time between basements
    if b1 == b2:  # Same basement
        basement_travel_time = 0
    else:  # Different basements
        basement_travel_time = abs(int(b2[1]) - int(b1[1])) * BASEMENT_TRAVEL_TIME
    # Total travel time is the sum of tower travel time and basement travel time
    return tower_travel_time + basement_travel_time

def timeRequired(jobA, jobB):
    # indA = tower_index[jobA.tower]
    # indB = tower_index[jobB.tower]
    # time = travellingTimes[indA][indB]
    time = getTimeRequired(jobA.tenantBlockId, jobB.tenantBlockId)
    time += TIME_REQUIRED_FOR_BASEMENT_CHANGE * abs(int(jobA.basement[1]) - int(jobB.basement[1]))
    return time / 3600

def assignJobs(tenant, jobs, workers):
    global tenant_data
    tenant_data = tenant
    di=dict()
    for i in jobs:
        di[i.id]=abs(int(i.deadline[-3:-5:-1][::-1]))
    di = dict(sorted(di.items(), key=itemgetter(1, 0)))
    print(di)
    l=len(workers)
    #for i,j in di.items():
    #    if 
    '''Your assigning logic goes here
    This method has to return a dictionay where the key is the worker_id and the value contains a list of jobs basis sorted by the assigning order
    '''
    return jobs