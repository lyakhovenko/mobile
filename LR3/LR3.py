from datetime import datetime
import csv
from fpdf import FPDF

PDF_FILE = 'payment.pdf'

def pdf_common_line(pdf, font_size, text):
    pdf.write(font_size / 2, text)
    pdf.ln(font_size / 2)

def create_pdf(bank_name, inn, kpp, bik, recipient, account_number1, account_number2, doc_number, date, provider,
               customer, reason):
    header = [['Банк получателя: ' + bank_name, 'БИК: ' + bik],
              ["ИНН: " + inn + "   " + "КПП: " + kpp, 'Сч. №' + account_number1],
              ['Получатель: ' + recipient, 'Сч. №' + account_number2]]
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.add_font('DejaVu', 'B', 'DejaVuSansCondensed-Bold.ttf', uni=True)

    pdf.set_font('DejaVu', '', 12)

    col_width = pdf.w / 2.2
    row_height = pdf.font_size
    spacing = 2
    for row in header:
        for item in row:
            pdf.cell(col_width, row_height * spacing,
                     txt=item, border=1)
        pdf.ln(row_height * spacing)

    font_size = 16
    pdf.set_font('DejaVu', 'B', font_size)
    pdf.ln(font_size / 2)
    pdf_common_line(pdf, font_size, "Счёт на оплату №{} от {}г.".format(doc_number, date))
    pdf_common_line(pdf, font_size, "_" * 74)

    font_size = 12
    pdf.ln(font_size)
    pdf.set_font('DejaVu', '', font_size)
    pdf_common_line(pdf, font_size, "Поставщик")
    pdf_common_line(pdf, font_size, "(Исполнитель): {}".format(provider))
    pdf_common_line(pdf, font_size, "")
    pdf_common_line(pdf, font_size, "Покупатель")
    pdf_common_line(pdf, font_size, "(Заказчик): {}".format(customer))
    pdf_common_line(pdf, font_size, "")
    pdf_common_line(pdf, font_size, "Основание: {}".format(reason))
    pdf_common_line(pdf, font_size, "")

    font_size = 10
    row_height = pdf.font_size
    pdf.set_font('DejaVu', '', font_size)

    table = [['№', "Товары (работы, услуги)", "Кол-во", "Ед.", "Сумма"]]
    counter = 1

    table.append([str(counter), "Звонок {} мин. ".format(number),"{} шт.".format(minut_call), "{} руб.".format(1), "{} руб.".format(minut_call)])
    counter += 1

    table.append([str(counter), "SMS для {}".format(number), "{} шт.".format(sms), "{} руб.".format(s), "{} руб.".format(coat_sms)])
    counter += 1

    table.append([str(counter), "Интернет трафик (за МБ)", "{} МБ".format(Q+1000), "{} руб.".format(k2),
                  "{} руб.".format(X)])

    table.append(['', "ВСЕГО", '', '', "{} руб.".format(sum)])

    one_part = pdf.w / 18
    for row in table:
        pdf.cell(one_part * 1, row_height * spacing, txt=row[0], border=1)  # number
        pdf.cell(one_part * 8, row_height * spacing, txt=row[1], border=1)  # title
        pdf.cell(one_part * 2, row_height * spacing, txt=row[2], border=1)  # count
        pdf.cell(one_part * 2, row_height * spacing, txt=row[3], border=1)  # cost per one
        pdf.cell(one_part * 3, row_height * spacing, txt=row[4], border=1)  # total cost
        pdf.ln(row_height * spacing)


    font_size = 16
    pdf.set_font('DejaVu', 'B', font_size)
    pdf_common_line(pdf, font_size, "Всего к оплате: {} руб.".format(sum))
    pdf_common_line(pdf, font_size, "")

    font_size = 8
    pdf.set_font('DejaVu', '', font_size)
    pdf_common_line(pdf, font_size, "HELLO!")
    pdf_common_line(pdf, font_size,
                    "Оплата данного счёта означает согласие с условиями поставки товара/предоставления услуг.")
    pdf_common_line(pdf, font_size, "")

    font_size = 16
    pdf.set_font('DejaVu', 'B', font_size)
    pdf.ln(font_size / 2)
    pdf_common_line(pdf, font_size, "_" * 74)
    font_size = 12
    pdf.set_font('DejaVu', '', font_size)
    pdf.ln(font_size / 2)
    pdf_common_line(pdf, font_size, "Руководитель " + "_" * 20 + " " * 25 + "Бухгалтер " + "_" * 20)

    pdf.output(name=PDF_FILE, dest='F').encode('utf-8')


if __name__ == "__main__":
    print("== Payment document ==")

    list_1 = []
    with open('data.csv') as data_file:
        reader = csv.reader(data_file)
        for a in reader:
            list_1.append(a)

    number = '915783624'
    k1 = 1
    s = 5
    minut_call = 0.0
    coat_sms = 0

    for i in range(9):
        if number in list_1[i][1]:
            if float(list_1[i][3]) > 10:
                minut_call += float(list_1[i][3]) - 10.0
                coat_sms += float(list_1[i][4])
            else:
                coat_sms += float(list_1[i][4])

    minut_call = round(minut_call, 2)
    sms = coat_sms
    coat_sms = coat_sms * s
    minut_call = minut_call * k1

    list_2 = []
    with open('dataset.csv') as data_file:
        reader = csv.reader(data_file)
        for a in reader:
            list_2.append(a)

    k2 = 0.5
    limit = 1000
    address = '192.168.250.39'
    Q = 0.0
    i = 0
    for i in range(17449):
        if address in list_2[i][3]:
            Q += float(list_2[i][12])

    Q -= 1000
    X = Q * k2
    sum = X * 1.2 + minut_call * 1.2 + coat_sms * 1.2
    nds = sum * 0.2


    print("Creating PDF file...")
    create_pdf(bank_name="JJJ Банк", inn='123456173', kpp='00001238', bik='666666', \
               recipient="JULILIY", account_number1="1234591", account_number2="1378923", \
               doc_number="1", date=datetime.now().strftime("%d.%m.%Y"), \
               provider="ООО СВЯЗЬ", customer="JULILIY ({}, {})".format(address, number), reason="ДОЛГ!")
