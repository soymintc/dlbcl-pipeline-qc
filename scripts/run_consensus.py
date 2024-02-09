import parse_lumpy
import parse_destruct
import consensus

# input 
lumpy_path = '../data/breakpoints/HCM-BROD-0011-C71-01A_lumpy.vcf'
destruct_path = '../data/breakpoints/HCM-BROD-0011-C71-01A_destruct_breakpoints.tsv'

# config
config = {
    'chromosomes': list(map(str, range(1, 23))) + ['X'],
    'lumpy_paths': {
        'extractSplitReads_BwaMem': 'lumpy_extractSplitReads_BwaMem',
        'samtools': 'samtools',
        'lumpyexpress': 'lumpyexpress',
    },
    'parse_lumpy': {
        'deletion_size_threshold': 0,
        'tumour_read_support_threshold': 0,
    },
    'parse_destruct': {
        'deletion_size_threshold': 1000,
        'foldback_threshold': 30000,
        'readsupport_threshold': 4,
        'breakdistance_threshold': 30
    },
    'consensus': {
        'confidence_interval_size': 500,
    },
}

# parse and filter lumpy
lumpy_output_path = '../data/breakpoints/HCM-BROD-0011-C71-01A_filtered_lumpy.csv'
vcfdata = parse_lumpy.parse_vcf(lumpy_path)
vcfdata = parse_lumpy.parse_vcf_group(vcfdata)
vcfdata = parse_lumpy.create_data(vcfdata)
vcfdata = parse_lumpy.convert_to_df(vcfdata)
vcfdata = parse_lumpy.filter_calls(vcfdata, config['parse_lumpy'])
parse_lumpy.write(lumpy_output_path, vcfdata)

# parse and filter destruct
destruct_output_path = '../data/breakpoints/HCM-BROD-0011-C71-01A_filtered_destruct.csv'
parse_destruct.parser(destruct_path, destruct_output_path, config['parse_destruct'], foldback_threshold=config['parse_destruct']['foldback_threshold'])

# make consensus csv
consensus_path = '../data/breakpoints/HCM-BROD-0011-C71-01A_filtered_consensus_calls.csv'
consensus.consensus(
    destruct_output_path, lumpy_output_path, consensus_path, confidence_interval=config['consensus']['confidence_interval_size']
)