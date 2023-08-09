# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"B61z.00","system":"readv2"},{"code":"B61z.11","system":"readv2"},{"code":"B61zz00","system":"readv2"},{"code":"BBj0.00","system":"readv2"},{"code":"BBjz.00","system":"readv2"},{"code":"ZV10711","system":"readv2"},{"code":"100423.0","system":"med"},{"code":"101530.0","system":"med"},{"code":"101715.0","system":"med"},{"code":"104291.0","system":"med"},{"code":"104484.0","system":"med"},{"code":"104743.0","system":"med"},{"code":"104895.0","system":"med"},{"code":"105472.0","system":"med"},{"code":"105841.0","system":"med"},{"code":"106349.0","system":"med"},{"code":"106597.0","system":"med"},{"code":"106911.0","system":"med"},{"code":"107032.0","system":"med"},{"code":"107804.0","system":"med"},{"code":"108775.0","system":"med"},{"code":"108886.0","system":"med"},{"code":"110563.0","system":"med"},{"code":"19140.0","system":"med"},{"code":"20710.0","system":"med"},{"code":"2462.0","system":"med"},{"code":"29178.0","system":"med"},{"code":"29876.0","system":"med"},{"code":"31537.0","system":"med"},{"code":"31741.0","system":"med"},{"code":"38939.0","system":"med"},{"code":"40508.0","system":"med"},{"code":"40561.0","system":"med"},{"code":"42198.0","system":"med"},{"code":"42461.0","system":"med"},{"code":"42769.0","system":"med"},{"code":"43415.0","system":"med"},{"code":"44196.0","system":"med"},{"code":"49605.0","system":"med"},{"code":"51285.0","system":"med"},{"code":"53397.0","system":"med"},{"code":"55303.0","system":"med"},{"code":"56041.0","system":"med"},{"code":"57225.0","system":"med"},{"code":"58684.0","system":"med"},{"code":"59755.0","system":"med"},{"code":"59778.0","system":"med"},{"code":"61149.0","system":"med"},{"code":"61662.0","system":"med"},{"code":"61997.0","system":"med"},{"code":"63054.0","system":"med"},{"code":"63625.0","system":"med"},{"code":"64036.0","system":"med"},{"code":"64343.0","system":"med"},{"code":"65483.0","system":"med"},{"code":"65489.0","system":"med"},{"code":"65584.0","system":"med"},{"code":"67506.0","system":"med"},{"code":"67703.0","system":"med"},{"code":"68039.0","system":"med"},{"code":"68330.0","system":"med"},{"code":"71142.0","system":"med"},{"code":"73532.0","system":"med"},{"code":"89230.0","system":"med"},{"code":"91900.0","system":"med"},{"code":"92245.0","system":"med"},{"code":"93951.0","system":"med"},{"code":"94005.0","system":"med"},{"code":"94279.0","system":"med"},{"code":"94407.0","system":"med"},{"code":"95049.0","system":"med"},{"code":"95338.0","system":"med"},{"code":"96183.0","system":"med"},{"code":"97746.0","system":"med"},{"code":"97863.0","system":"med"},{"code":"98840.0","system":"med"},{"code":"98909.0","system":"med"},{"code":"99012.0","system":"med"},{"code":"99200.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('hodgkin-lymphoma-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["hodgkin-lymphoma---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["hodgkin-lymphoma---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["hodgkin-lymphoma---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
