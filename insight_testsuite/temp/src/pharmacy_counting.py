import csv, sys
from collections import Counter, defaultdict


def write_file(output_filename, drugs):
    with open(output_filename, 'w') as f:
        w = csv.DictWriter(f, ('drug_name', 'num_prescriber', 'total_cost'))
        w.writeheader()
        w.writerows({
            'drug_name': drug_name,
            'num_prescriber': len(prescriber_totals),
            'total_cost': sum(prescriber_totals.values()),
        }
            for drug_name, prescriber_totals in drugs.items()
        )


def read_file(input_filename):
    drugs = defaultdict(Counter)
    with open(input_filename) as f:
        for row in csv.DictReader(f):
            drugs[row['drug_name']][row['id']] += float(row['drug_cost'])
    return drugs


def main(input_filename, output_filename):
    write_file(output_filename, read_file(input_filename))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
