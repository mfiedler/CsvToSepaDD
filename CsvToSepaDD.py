#!/usr/bin/env python

import argparse
import pprint


DEFAULT_CONFIG_FILE_NAME = 'CsvToSepaDD.config'
DEFAULT_CURRENCY = 'EUR'



def csvToSepa(args):
    '''
    [TODO] Converts the SEPA direct debit data from a given CSV file to SEPA XML
    '''
    pass




def createConfig(args):
    '''Interactively creates a configuation file'''

    fileName = raw_input('configuration file name [%s]: ' % DEFAULT_CONFIG_FILE_NAME)
    if not fileName:
        fileName = DEFAULT_CONFIG_FILE_NAME
    name = raw_input('your name: ')
    iban = raw_input('your IBAN: ')
    bic = raw_input('your BIC: ')
    creditorId = raw_input('your creditor id: ')
    currency = raw_input('your currency [%s]: ' % DEFAULT_CURRENCY)
    if not currency:
        currency = DEFAULT_CURRENCY

    config = {
            'name': name,
            'iban': iban,
            'bic':  bic,
            'creditor_id': creditorId,
            'currency': currency,
    }

    with open(fileName, 'w') as f:
        pprint.pprint(config, stream=f, indent=4)

    print 'Configuration written to %s. ' \
          'You can edit this file with a text ' \
          'editor if you need to change something later.' % fileName




if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Create SEPA XML direct debit files from CSV')
    subparsers = parser.add_subparsers()
    genConfigParser = subparsers.add_parser('genconfig', help='generate a configuration file')
    genConfigParser.set_defaults(func=createConfig)
    genConfigParser.add_argument('config', help='name of the configuration file')
    convertParser = subparsers.add_parser('convert', help='convert a CSV file to a SEPA XML file')
    convertParser.set_defaults(func=csvToSepa)
    convertParser.add_argument('config', help='configuration file to use')
    convertParser.add_argument('input', help='input file or - for stdin')
    convertParser.add_argument('output', help='output file or - for stdout')

    args = parser.parse_args()
    args.func(args)
