from xlrd import open_workbook

import client

# xl_workbook = open_work9book("teaching_timetable.xls")
xl_workbook = open_workbook("AUGUST_SEMESTER_2016.xls", formatting_info=True)


def get_days(sheet):
    temp = {}
    for col in range(sheet.ncols):
        value = sheet.cell(1, col).value
        if value:
            if value not in temp:
                temp[value] = []
            temp[value].append(col)
    return temp


def parse_timetable():
    client.authenticate()
    for sheet in xl_workbook.sheets():
        sheet_name = sheet.name
        days_row_index = get_days(sheet)
        if "Athi" in sheet_name:
            client.create_collection("athitt")
            print("\n" + sheet_name)
            if sheet.ncols < 14:
                for row in [x for x in range(3, sheet.nrows)]:
                    for col in [x for x in range(1, sheet.ncols) if (x != 3) and (x != 8)]:
                        if sheet.cell(row, col).value:
                            for k in days_row_index.keys():
                                if col in days_row_index[k]:
                                    time = sheet.cell(2, col).value.split('-')
                                    body = dict(location=sheet.cell(row, 0).value, start_time=time[0],
                                                end_tiem=time[1], day=sheet.cell(1, col).value)
                                    title = sheet.cell(row, col).value
                                    data = dict(title="".join(title.split()), body=body)
                                    client.create_document("athitt", data)
                                    # print(sheet.cell(1, col).value+" : "+sheet.cell(row, col).value+" : "+sheet.cell(row, 0).value+" : "+sheet.cell(2, col).value)
            else:
                for row in [x for x in range(3, sheet.nrows)]:
                    for col in [x for x in range(1, sheet.ncols) if (x != 3) and (x != 8) and (x != 9)]:
                        if sheet.cell(row, col).value:
                            for k in days_row_index.keys():
                                if col in days_row_index[k]:
                                    time = sheet.cell(2, col).value.split('-')
                                    body = dict(location=sheet.cell(row, 0).value, start_time=time[0],
                                                end_tiem=time[1], day=sheet.cell(1, col).value)
                                    title = sheet.cell(row, col).value
                                    data = dict(title="".join(title.split()), body=body)
                                    client.create_document("athitt", data)
                                    # print(sheet.cell(1, col).value+" : "+sheet.cell(row, col).value + " : " + sheet.cell(row, 0).value + " : " + sheet.cell(2,col).value)
        elif "Day" in sheet_name:
            client.create_collection("nairobidaytt")
            print("\n" + sheet_name)
            for row in [x for x in range(3, sheet.nrows)]:
                for col in [x for x in range(1, sheet.ncols) if (x != 5) and (x != 9) and (x != 11)]:
                    if sheet.cell(row, col).value:
                        for k in days_row_index.keys():
                            if col in days_row_index[k]:
                                time = sheet.cell(2, col).value.split('-')
                                body = dict(location=sheet.cell(row, 0).value, start_time=time[0],
                                            end_tiem=time[1], day=sheet.cell(1, col).value)
                                title = sheet.cell(row, col).value
                                data = dict(title="".join(title.split()), body=body)
                                client.create_document("nairobidaytt", data)
                                # print(sheet.cell(1, col).value+" : "+sheet.cell(row, col).value+" : "+sheet.cell(row, 0).value+" : "+sheet.cell(2, col).value)
        elif "Evening" in sheet_name:
            client.create_collection("nairobieveningtt")
            print("\n" + sheet_name)
            for row in [x for x in range(3, sheet.nrows)]:
                for col in [x for x in range(1, sheet.ncols) if (x != 5)]:
                    if sheet.cell(row, col).value:
                        for k in days_row_index.keys():
                            if col in days_row_index[k]:
                                time = sheet.cell(2, col).value.split('-')
                                body = dict(location=sheet.cell(row, 0).value, start_time=time[0],
                                            end_tiem=time[1], day=sheet.cell(1, col).value)
                                title = sheet.cell(row, col).value
                                data = dict(title="".join(title.split()), body=body)
                                client.create_document("nairobieveningtt", data)
                                # print(sheet.cell(1, col).value+" : "+sheet.cell(row, col).value+" : "+sheet.cell(row, 0).value+" : "+sheet.cell(2, col).value)


parse_timetable()
