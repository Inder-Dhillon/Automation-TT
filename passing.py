import decimal
import PySimpleGUI as sg
import slate3k as slate
import csv
import numpy as np
layout = [[sg.Text('Crossing Invoices', size=(30, 1), font=("Helvetica", 25), text_color='blue')],
[sg.Text('Select type of border/toll:')],
[sg.InputCombo(['BlueWater USD', 'BlueWater CAD', 'Ambassador Bridge', 'EZ Pass(WIP)'], size=(30, 4))],
[sg.Text('Source File', size=(8, 1), auto_size_text=False, justification='right'), sg.InputText('Source', key='_file_'),
 sg.FileBrowse()],
[sg.Submit(button_color=('white','green')), sg.Cancel()]]

event, values  = sg.Window('Crossing Invoices', auto_size_text=True, default_element_size=(40, 1)).Layout(layout).Read()
#Global variables
final = ''
dict = {'12590000415':'106',
        '12590000126':'108',
        '12590000167':'109',
        '12592134642':'110',
        '12590000381':'111',
        '12590000399':'113',
        '12590000134':'118',
        '12590000142':'119',
        '12590000159':'120',
        '12590000431':'121',
        '12590000217':'122',
        '12592134584':'123',
        '12590000456':'124',
        '12590000464':'127',
        '12592134634':'128',
        '12590000480':'130',
        '12590000498':'131',
        '12590000506':'132',
        '12590000225':'134',
        '12590000241':'136',
        '12590000514':'68',
        '12590000522':'70',
        '12590000530':'79',
        '12590000548':'86',
        '12590000555':'87',
        '12590000316':'91',
        '12590000324':'92',
        '12590000332':'93',
        '12590000340':'94',
        '12590000357':'95',
        '12592134600':'96',
        '12590000365':'97'}

if values[0]=='BlueWater USD':
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
    for j in range(0,len(clunique)):
        final = final + (dict[clunique[j]] + " : " + str(plunique[j]) + " USD\n")
elif values[0]=='BlueWater CAD':
    with open(values['_file_'], 'rb') as f:
        extracted_text = slate.PDF(f)

    pdfstr = str(extracted_text)
    pdflist = pdfstr.split('\\n')
    count = 0
    codelist = []
    pricelist = []
    for x in pdflist:
        if pdflist.index(x) > pdflist.index("CARD NUMBER") and pdflist.index(x) < pdflist.index("PAYMENT/TOLL"):
            codelist.append(x)
        if pdflist.index(x) > pdflist.index("AMOUNT") and pdflist.index(x) < pdflist.index("BALANCE"):
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
            final = final + (dict[clunique[j]] + " : " + str(plunique[j]) + " CAD\n")
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
        final = final + (clunique[j] + " : " + str(plunique[j]) + " CAD\n")
else:
    final = ''
sg.Popup(final)


