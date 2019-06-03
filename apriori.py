#!/usr/bin/env python
import itertools
import logging



class SupermarketOptimization:
    '''
    Class for supermarket optimization using association which is typically used for market-basket
    analysis, objective would be to locate trends within the data i.e. technique will attempt to
    find groups of items that are commonly found together and thus can be used to determine which
    items are commonly bought together or whether transaction is out of ordinary.
    The rule X => Y holds with support s if s% os transactions in D contains X U Y and rules that
    have a s greater than user-specified support is said to have minimum support as per Agrawal
    et al., 1983.
    '''

    def __init__(self, frequent_items_set_size = 3):
        '''
        Initializer of a class
        '''
        self.data = []
        self.min_set_size_reduction = frequent_items_set_size

    def __del__(self):
        pass

    def __repr__(self):
        return ""

    def load_data(self, path):
        '''
        load_data() uses the path and reads the file in dict - gets all transactions
        :param path: path of the input file
        :return:
        '''
        try:
            if self.data is not None:
                with open(path, 'r') as file_handler:
                    for line in file_handler:
                        transaction = []
                        for item in line.rstrip().split(' '):
                            transaction.append(item)
                        self.data.append(transaction)
        except Exception as e:
            logging.error(e)
        return self.data

    @staticmethod
    def get_inputs_from_cmd(parser, default_filename, default_support, default_output):
        """
        parse the arguments as switches to run this program.
        :param parser:
        :return:
        """
        parser.add_option('-f', '--filename', type='string', help='file name',
                          dest='file')
        parser.add_option('-s', '--support', type='int', help='minimum support',
                          dest='support')
        parser.add_option('-o', '--output', type='string', help='output file name',
                          dest='output')
        (options, args) = parser.parse_args()
        if not options.file:
            logging.warning('Filename is not sent across using command prompt, falling to default')
            filename = default_filename
        else:
            filename = options.file
        if not options.support:
            logging.warning('Support level not provided, default to 4 as asked in exercise.')
            support = default_support
        else:
            support = options.support
        if not options.output:
            logging.warning('Output file not provided, default to some output filename')
            outputfile = default_output
        else:
            outputfile = options.output
        return filename, support, outputfile

    def create_list(self):
        '''
        Create a list of candidate item sets of size one.
        uses self.data which has been populated from input file to generate list of candidate
        items sets of size one.
        reduce actual data to reduced candidates which does not meet support
        :return:
        '''
        frequent_min_item_set_size = 3
        logging.debug('Starting to run candidates list')
        individual_candidates = []
        longest_tran = 5
        for transaction in self.data:
            for item_set_size in range(frequent_min_item_set_size, longest_tran+1):
                for item in set(itertools.combinations(transaction, item_set_size)):
                    if not [item] in individual_candidates:
                        individual_candidates.append([item])
        individual_candidates.sort()
        # frozenset because it will be a key of a dictionary.
        return individual_candidates

    def candidate_exist(self, candidate, transaction):
        found_counter = 0
        for can in candidate[0]:
            for tran in transaction:
                if can == tran:
                    found_counter += 1

        if found_counter == len(candidate[0]):
            return True

        return False

    def scan_dataset(self, dataset, candidates, min_support):
        '''
        Returns all candidates that meets a minimum support level and items set size
        :param dataset:
        :param candidates:
        :param min_support:
        :return:
        '''
        candidate_counts_map = {}
        for tran_id in dataset:
            for candidate in candidates:
                if self.candidate_exist(candidate, tran_id):
                    candidate_counts_map.setdefault(candidate[0], 0)
                    candidate_counts_map[candidate[0]] += 1

        #num_items = float(len(self.data))
        retlist = []
        support_data = {}
        for key in candidate_counts_map:
            support = candidate_counts_map[key]
            if support >= min_support:
                retlist.insert(0, key)
            support_data[key] = support
        return retlist, support_data

    def generate_apriori(self, freq_sets, k):
        """
        Generate the joint transactions from candidate sets
        Basically dedup (38, 39,41) to (38, 41, 39)
        """
        return_list = []
        length = len(freq_sets)
        for i in range(length):
            for j in range(i + 1, length):
                L1 = list(freq_sets[i])
                L2 = list(freq_sets[j])
                L1.sort()
                L2.sort()
                if L1 == L2:
                    return_list.append(freq_sets[i] | freq_sets[j])
        return return_list

    def apriori_run(self, minsupport):
        """
        Generate a list of candidate item sets
        """
        C1 = self.create_list()
        dataset = list(map(set, self.data))
        L1, support_data = self.scan_dataset(dataset, C1, minsupport)
        scanned_reduced_list = [L1]
        k = 2
        while len(scanned_reduced_list[k - 2]) > 0:
            Ck = self.generate_apriori(scanned_reduced_list[k - 2], k)
            Lk, supK = self.scan_dataset(dataset, Ck, minsupport)
            support_data.update(supK)
            scanned_reduced_list.append(Lk)
            k += 1
        return scanned_reduced_list, support_data

    @staticmethod
    def write_output(final_list, support_data, output_file):
        """
        Creates final output in the format
        :param final_map:
        :return: nothing to return.
        """
        with open(output_file, "w") as fw:
            fw.write("<item set size(N)>, <co-occurance frequency>, <item 1 id>, <item 2 id>, "
                     "<item 3 id>" +"\n")
            for items in final_list:
                print(items)
                for tup in items:
                    print(tup)
                    list_form = list(tup)
                    fw.write((str(len(tup))) + "," + str(support_data[tup]) + "," + str(list_form) +
                             "\n")
