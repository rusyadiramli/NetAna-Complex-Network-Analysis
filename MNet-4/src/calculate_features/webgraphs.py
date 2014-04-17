'''
This scipt generates the feature vectors for the many features for all the network data.

mari wahl @ 2014
'''

from helpers import constants, running

NUM_SAMPLES = constants.NUMBER_OF_RANDOM_SAMPLES 

PATH_2_GRAPHS = constants.PATH_2_GRAPH_SAMPLED
PATH_2_OUTPUT = constants.PATH_2_FEATURES_SAMPLED 


# change here for type of net:
NETWORK_FILES_DIR = constants.NETWORK_FILES_DIR_WEBGRAPHS
TYPE_NET_DIR = "webgraphs/"



def main():

    running.running_dir(NETWORK_FILES_DIR, NUM_SAMPLES, PATH_2_GRAPHS, TYPE_NET_DIR, PATH_2_OUTPUT)


    print("All features for " + TYPE_NET_DIR + " are processed. The end! \n")



if __name__ == '__main__':
    main()