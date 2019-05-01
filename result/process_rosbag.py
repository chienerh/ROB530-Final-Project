#!/usr/bin/python
import sys
import csv
import rosbag
import io
import os

def bag2csv(bag_name, target_name):  
    csv_name = bag_name.rstrip('.bag')
    
    # open bag file for read
    print("Reading " , bag_name)
    bag = rosbag.Bag(bag_name)
    bag_topics = bag.get_type_and_topic_info()[1].keys()

    # open csv file for write
    csvfile = open(target_name, 'w')
    #bag2csv = csv.writer(csvfile, delimiter=';', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
    bag2csv = csv.writer(csvfile, delimiter=',', quotechar='\'', quoting=csv.QUOTE_MINIMAL)

    for bag_topic in bag_topics:
        # write topic name
        print("Write " , bag_topic , " into csv file...")
        bag2csv.writerow([bag_topic])
        # set title_flag to 0
        title_flag = 0

        for topic, msg, t in bag.read_messages(topics=bag_topic):
            # split msg
            msg_list = str(msg).split('\n')
            value_list = []
            title_list = []

            for msg_pair in msg_list:
                split_pair = msg_pair.split(':')
                msg_title = split_pair[0]
                msg_value = split_pair[1]

                if title_flag == 0:
                    title_list.append(msg_title)
                value_list.append(msg_value)
            
            if title_flag == 0:
                bag2csv.writerow(title_list)
                title_flag = 1
            
            bag2csv.writerow(value_list)
        
        # insert a row between to topics
        bag2csv.writerow([])

    
    # close files
    csvfile.close()
    bag.close()
    return '../result/'+csv_name+'.csv'


if __name__ == '__main__':
    bag_name = './bag/simulation_res.bag'
    if(len(sys.argv) == 1):
        target_name = './csv/simulation_res.csv'
    else:
        target_name = './csv/'+sys.argv[1]
    filename = bag2csv(bag_name, target_name)
    
