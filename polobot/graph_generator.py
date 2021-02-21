class graph_generator():
    def __init__(self, debug):
        print("Starting Graph Generator")
        self.debug = debug
        self.files = {}
        
    def initialize_source(self, file, file_handle):
        # create empty array named "file_handle"
        f = open(file, 'w')
        f.write('{} = {{}};\n'.format(file_handle));
        f.close()
        # add file handle to files array
        self.files[file_handle] = file

    def generate_last_position(self, data, scope, pair, file_handle):
        f = open(self.files[file_handle], 'a')
        if scope == 'daily':
            num_elements = 1440
        if scope == 'weekly':
            num_elements = 10080
        if scope == 'monthly':
            num_elements = 43200
        final = ""
        final += 'last_position["{}"] = {{}};\n'.format(scope);
        final += 'last_position["{}"]["{}"] = {{}};\n'.format(scope, pair);
        final += 'last_position["{}"]["{}"]["labels"] = ["{}"];\n'.format(scope, pair, '","'.join(map(str, data['labels'][-num_elements:])))
        final += 'last_position["{}"]["{}"]["data"] = [{}];\n'.format(scope, pair,  ",".join(map(str, data['data_raw'][-num_elements:])))
        final += 'last_position["{}"]["{}"]["avg_hourly"] = [{}];\n'.format(scope, pair, ",".join(map(str, data['data_avg_hourly'][-num_elements:])))
        final += 'last_position["{}"]["{}"]["avg_daily"] = [{}];\n'.format(scope, pair,  ",".join(map(str, data['data_avg_daily'][-num_elements:])))
        final += 'last_position["{}"]["{}"]["avg_weekly"] = [{}];\n'.format(scope, pair, ",".join(map(str, data['data_avg_weekly'][-num_elements:])))
        if self.debug:
            print(final)
        f.write(final)
        f.close()