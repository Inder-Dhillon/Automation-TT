import decimal
import PySimpleGUI as sg
import slate3k as slate
import csv
import numpy as np
from sys import exit
while True:
    layout = [[sg.Text('Crossing Invoices', size=(30, 1), font=("Helvetica", 25), text_color='blue')],
              [sg.Text('Select type of border/toll:')],
              [sg.InputCombo(['BlueWater USD', 'BlueWater CAD', 'Ambassador Bridge', 'EZ Pass'], size=(30, 4))],
              [sg.Text('Source File', size=(8, 1), auto_size_text=False, justification='right'),
               sg.InputText('Source', key='_file_'),
               sg.FileBrowse()],
              [sg.RButton('Submit',button_color=('white', 'green')), sg.Exit()]]

    event, values = sg.Window('Crossing Invoices', auto_size_text=True, default_element_size=(40, 1)).Layout(layout).Read()
    if event is None or event == 'Exit':
        exit()
    # Global variables
    final = 'Trucks : Total\n'
    dict = {
        '12590000514': '068',
        '12590000522': '070',
        '206601': '070',
        '12590000530': '079',
        '206602': '079',
        '12590000548': '086',
        '206611': '086',
        '12590000555': '087',
        '206609': '087',
        '12590000316': '091',
        '218771': '091',
        '12590000324': '092',
        '206605': '092',
        '12590000332': '093',
        '206604': '093',
        '12590000340': '094',
        '206606': '094',
        '12590000357': '095',
        '206607': '095',
        '12592134600': '096',
        '206592': '096',
        '12590000365': '097',
        '206594': '097',
        '12590000415': '106',
        '268444': '106',
        '12590000126': '108',
        '206629': '108',
        '12590000167': '109',
        '206595': '109',
        '12592134642': '110',
        '206593': '110',
        '12590000381': '111',
        '206591': '111',
        '12590000399': '113',
        '206627': '113',
        '12590000134': '118',
        '206624': '118',
        '12590000142': '119',
        '206623': '119',
        '12590000159': '120',
        '206622': '120',
        '12590000431': '121',
        '206628': '121',
        '12590000217': '122',
        '206185': '122',
        '12592134584': '123',
        '206621': '123',
        '12590000456': '124',
        '206600': '124',
        '12590000464': '127',
        '206620': '127',
        '12592134634': '128',
        '206608': '128',
        '12590000480': '130',
        '206619': '130',
        '12590000498': '131',
        '206618': '131',
        '12590000506': '132',
        '206596': '132',
        '12590000225': '134',
        '206599': '134',
        '12590000241': '136',
        '206612': '136',
        '12590000233': '137',
        '206613':'137',
        '12590000266':'138',
        '206617':'138',
        '12590000274':'139',
        '206615':'139',
        '12590000241':'142',
        '244977':'142',
        '12590000290':'143',
        '244978':'143',
        '12590000308':'144',
        '244979':'144',
        '12590000142':'145',
        '244976':'145',
        '12590000613':'146',
        '244975':'146',
        '206613': '137',
        '2141PS': '052',
        '2142PS': '053',
        '4588PY': '068',
        '5095PT': '070',
        '4622PY': '079',
        '7637PV': '086',
        '7701PV': '087',
        '4276PW': '091',
        '7153PW': '092',
        '7154PW': '093',
        '8748PW': '094',
        '1455PZ': '095',
        '1477PT': '096',
        '9997PW': '097',
        '9998PW': '106',
        '8505PX': '108',
        '9517PX': '109',
        '2751PY': '110',
        '3759PY': '111',
        '3930PY': '113',
        '4685PY': '118',
        '4686PY': '119',
        '5741PY': '120',
        '6487PY': '121',
        '6488PY': '122',
        '6489PY': '123',
        '6574PY': '124',
        '9223PY': '127',
        '9374PY': '128',
        '5435PZ': '130',
        '2488PY': '131',
        '3791PZ': '132',
        '2630PZ': '133',
        '6513PZ': '134',
        '7045PZ': '135',
        '7197PZ': '136',
        '8638PZ': '137',
        '8884PZ': '138',
        '2630PZ': '139',
        'PA11121' : '142',
        '7197PZ' : '143',
        'PA11122' : '144',
        '8638PZ': '145',
        'PA12710' : '146',
    }




    if values[0] == 'BlueWater USD':
        with open(values['_file_'], 'rb') as f:
            extracted_text = slate.PDF(f)

        pdfstr = str(extracted_text)
        pdflist = pdfstr.split('\\n')
        print(pdflist)
        countlist = 3
        codelist = []
        pricelist = []
        for i in pdflist:
            countlist = countlist + 1
            if i == " 1 ":
                pricelist.append(pdflist[countlist][1:])
            if i == "Toll Posting":
                codelist.append(pdflist[countlist - 2][2:])
        clunique = list(set(codelist))
        plunique = []
        codelist = codelist[:]
        print(codelist)
        print(pricelist)
        for x in clunique:
            if codelist.count(x) > 1:
                vals = np.array(codelist)
                repeats = np.where(vals == x)[0]
                num = 0
                for z in repeats:
                    num = num + decimal.Decimal(pricelist[z])
                plunique.append(num)
            else:
                plunique.append(pricelist[codelist.index(x)])
        for j in range(0, len(clunique)):
            if clunique[j] in dict:
                final = final + (dict[clunique[j]] + "      : " + str(plunique[j]) + " USD\n")
            else:
                final = final + (clunique[j] + " : " + str(plunique[j]) + " USD\n")





    elif values[0] == 'BlueWater CAD':
        with open(values['_file_'], 'rb') as f:
            extracted_text = slate.PDF(f)

        pdfstr = str(extracted_text)
        pdflist = pdfstr.split('\\n')
        count = 0
        codelist = []
        pricelist = []
        while True:
            try:
                pdflist.remove("")
            except ValueError:
                break
        for x in pdflist:
            if pdflist.index(x) > pdflist.index("CARD NUMBER") and pdflist.index(x) < pdflist.index("PAYMENT/TOLL"):
                codelist.append(x)
            if pdflist.index(x) > pdflist.index("BALANCE") and pdflist.index(x) < pdflist.index("PREPAID TOLL BALANCE"):
                pricelist.append(x[:-5])
        for x in codelist:
            if x == 'Payment of Pre-Paid Toll':
                num = codelist.index(x)
                del codelist[num]
                del pricelist[num]
        plunique = []
        final = ''
        clunique = list(set(codelist))
        for x in clunique:
            if codelist.count(x) > 1:
                vals = np.array(codelist)
                repeats = np.where(vals == x)[0]
                num = 0
                for z in repeats:
                    num = num + decimal.Decimal(pricelist[z])
                plunique.append(num)
            else:
                plunique.append(pricelist[codelist.index(x)])
        for j in range(0, len(clunique)):
            if clunique[j] in dict:
                final = final + (dict[clunique[j]] + "      : " + str(plunique[j]) + " CAD\n")
            else:
                final = final + (clunique[j] + " : " + str(plunique[j]) + " CAD\n")
    elif values[0] == 'Ambassador Bridge':
        codelist = []
        pricelist = []
        with open(values['_file_'], mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                codelist.append(row["Card No./Plate"].strip())
                pricelist.append(row["Charges"])
        clunique = list(set(codelist))
        plunique = []
        for x in clunique:
            if codelist.count(x) > 1:
                vals = np.array(codelist)
                repeats = np.where(vals == x)[0]
                num = 0
                for z in repeats:
                    num = num + decimal.Decimal(pricelist[z])
                plunique.append(num)
            else:
                plunique.append(pricelist[codelist.index(x)])
        for j in range(0, len(clunique)):
            if clunique[j] in dict:
                final = final + (dict[clunique[j]] + "      : " + str(plunique[j]) + " USD\n")
            else:
                final = final + (clunique[j] + " : " + str(plunique[j]) + " USD\n")
    else:
        with open(values['_file_'], 'rb') as f:
            extracted_text = slate.PDF(f)

        pdfstr = str(extracted_text)
        pdflist = pdfstr.split('\\n')
        while True:
            try:
                pdflist.remove("")
            except ValueError:
                break
        codelist = []
        pricelist = []
        for x in range(0, len(pdflist)):
            if pdflist[x] == 'BUSINESS':
                pricelist.append(pdflist[x + 2][1:])
            if "/19" in pdflist[x] and "/19" in pdflist[x + 1]:
                if pdflist[x + 2] != 'Prepaid Toll Payment' and pdflist[x + 2] != 'Lease Tag Fee-INT':
                    codelist.append(pdflist[x + 2])
        plunique = []
        final = ''
        clunique = list(set(codelist))
        for x in clunique:
            if codelist.count(x) > 1:
                vals = np.array(codelist)
                repeats = np.where(vals == x)[0]
                num = 0
                for z in repeats:
                    num = num + decimal.Decimal(pricelist[z])
                plunique.append(num)
            else:
                plunique.append(pricelist[codelist.index(x)])
        for j in range(0, len(clunique)):
            final = final + (clunique[j] + " : " + str(plunique[j]) + "USD\n")
    sg.PopupScrolled(final)
