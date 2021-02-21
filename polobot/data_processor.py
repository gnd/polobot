# returns average value of any array 
def get_avg(data):
    sum = 0
    for line in data:
        sum += line
    return sum / len(data)

class data_processor():
    def __init__(self, debug):
        print("Starting Data Processor")
        self.debug = debug
                
    def process_rows(self, rows):
        # extract values
        timestamps = [a[0] for a in rows]
        values = [a[1] for a in rows]
        
        # prepare processed values
        output = {}
        output['labels'] = timestamps
        output['data_raw'] = values
        output['data_avg_hourly'] = []
        output['data_avg_daily'] = []
        output['data_avg_weekly'] = []
        
        # compute rolling averages
        index = 0
        for index in range(len(rows)):
            # rolling average for last hour
            slice_start = min(index, 60)
            output['data_avg_hourly'].append( get_avg(values[index-slice_start:index+1]) )
            # rolling average for last day
            slice_start = min(index, 1440)
            output['data_avg_daily'].append( get_avg(values[index-slice_start:index+1]) )
            # rolling average for last month
            slice_start = min(index, 43200)
            output['data_avg_weekly'].append( get_avg(values[index-slice_start:index+1]) )
            
        # return
        if self.debug:
            print("Data len: {}, AvgH: {}, AvgD: {}, AvgW: {}".format(len(output['data_raw']), len(output['data_avg_hourly']), len(output['data_avg_daily']), len(output['data_avg_weekly'])))
            #print(output)
        return output